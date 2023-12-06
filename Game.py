import curses
import random
from curses.textpad import rectangle
from datetime import datetime
from run import logger


class Globals:
    """
     *  GLOBALS: Aqui guarda a maiora das informações ecenciais para
     *  o jogo, mas elas podem ser acessadas pelas outras classes.
    """

    def __init__(self):
        self.keys = {
            "left":     [ 97, 104, 260],
            "down":     [115, 106, 258],
            "up":       [119, 107, 259],
            "right":    [100, 108, 261],
            "return":   [ 32, 111,  10]
        }
        self.oposite = {
            "right": "left",    "left": "right",
            "up": "down",        "down": "up"
        }

        self.menu_list = [
            "Play", "Scoreboard", "EXIT"
        ]


class Menu(Globals):
    """
     *  MENU: Escreve as primeiras opções na tela, e guarda o valor do
     *  item selecionado em self.selected_item.
    """

    def __init__(self):
        super().__init__()

        # Guarda o index do item selecionado do menu.
        self.selected_item = 0

    @property
    def start(self):
        logger.info('MENU_OPENED', description='menu was opened')
        curses.wrapper(self._run)
        logger.info('MENU_CLOSED', description='menu was closed')

    # Tira o cursor piscando, define um par de cores e depois desenha a tela.
    def _run(self, screen):
        curses.curs_set(False)
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

        self._loop(screen)

    # screen é o objeto que desenha as informações na tela. O loop atualiza as informações a todo momento.
    def _loop(self, screen):
        while 1:
            self._y_len, self._x_len = screen.getmaxyx()
            screen.clear()

            # Desenha um retângulo na tela.
            rectangle(
                screen, 5, 12,
                self._y_len - 6, self._x_len - 15
            )

            self._show_menu(screen)

            if self._keyboard(screen):
                break
            else:
                screen.refresh()

    # Desenha os itens do menu centralizados na tela.
    def _show_menu(self, screen):
        for index, text in enumerate(self.menu_list):
            x = self._x_len // 2 - len(text) // 2
            y = self._y_len // 2 - len(self.menu_list) // 2 + index

            # Se o ítem for selecionado, ele mostra o item azul.
            if self.selected_item == index:
                screen.attron(curses.color_pair(1))

            screen.addstr(y, x, text)
            screen.attroff(curses.color_pair(1))

    # Detecta as teclas precionadas e retorna True se for uma tecla "return".
    def _keyboard(self, screen):
        key = screen.getch()

        if key in self.keys["up"] and self.selected_item > 0:
            self.selected_item -= 1

        elif key in self.keys["down"] and self.selected_item < len(self.menu_list) - 1:
            self.selected_item += 1

        elif key in self.keys["return"]:
            return True

        return False


class Play(Globals):
    """
     *  PLAY: Além de iniciar o jogo e fazer ele funcionar, essa classe
     *  guarda a pontuação da partida e a data de quando ela começou no
     *  atributo self.score (uma lista).
    """

    def __init__(self, snake_body_fill, apple_fill):
        super().__init__()

        self._snake_body_fill = snake_body_fill
        self._apple_fill = apple_fill

        self._pause = False
        self.score = None

    @property
    def start(self):
        logger.info('PLAYING_STARTED', description='playing was started')
        curses.wrapper(self._run)
        logger.info('PLAYING_ENDED', description='playing was ended')

    # Configura a taxa de atualização da tela e carrega os "sprites iniciais" na tela.
    def _run(self, screen):
        self._y_len, self._x_len = screen.getmaxyx()

        # Setup inicial para a nova screen que será carregada.
        curses.curs_set(False)
        screen.nodelay(True)
        screen.clear()

        # Desenha a área do mapa na tela.
        rectangle(
            screen, 2, 5,
            self._y_len - 3, self._x_len - 6
        )

        # Reseta a pontuação.
        self.score = [
            str( datetime.today() ),   # -> Data do começo da partida
            0                          # -> Pontuação da partida
        ]

        # Carrega os elementos e inicia o jogo.
        self._load_content(screen)
        self._loop(screen)

    def _loop(self, screen):
        while 1:
            # Se a cobra estiver subindo/descendo, ela vai mais devagar...
            if self._current_direction in ["up", "down"]:
                screen.timeout(60)
            else:
                screen.timeout(40)

            self._get_new_direction(screen)

            # Se o jogo não estiver pausado, ele continua...
            if not self._pause:
                self._move_snake_head(screen)
                self._remove_the_tail(screen)

            if self._condictions_to_lose():
                break

            screen.refresh()

    # Cira o corpo da cobra, define uma direção e spawna uma maçã.
    def _load_content(self, screen):
        self._snake_body = [
            [
                self._y_len // 2,
                self._x_len // 2
            ]
        ]

        # Agora, seta uma direção default e spawna uma maçã.
        self._current_direction = "right"
        self._spawn_apple(screen)

        # Spawna o corpo (0 e 1) da cobra, com base nas cordenadas da cabeça (0).
        screen.addstr(
            self._snake_body[0][0],
            self._snake_body[0][1],
            self._snake_body_fill
        )

    # Seleciona, aleatoriamente, uma posição na tela, baseado em seu tamanho.
    def _get_apple_position(self):
        while 1:
            apple = [
                random.randint(3, self._y_len - 4),
                random.randint(6, self._x_len - 7)
            ]

            # Se a posição cair em cima da cobra, ele gera novamente até encontrar...
            if apple not in self._snake_body:
                break
        return apple

    # Faz a maçã aparecer na tela e guarda as cordenadas dessa posição.
    def _spawn_apple(self, screen):
        self.apple = self._get_apple_position()

        screen.addstr(
            self.apple[0], self.apple[1],
            self._apple_fill
        )
        logger.info('APPLE_SPAWNED', description='apple was spawned', params={"X": self.apple[0], "Y": self.apple[1]})

    # Muda de direção, ou não, com base na tecla precionada.
    def _get_new_direction(self, screen):
        key = screen.getch()
        new_direction = None

        # Isso salva a direção da tecla precionada em new_direction...
        for i in self.keys.items():
            if key in i[1]:
                new_direction = i[0]

        # Só muda de direção se a nova direção não for a mesma ou oposta, ou se não for "return"...
        if (
            new_direction in self.keys.keys()
            and new_direction != self.oposite[self._current_direction]
            and new_direction != "return"
        ):
            logger.info('DIRECTION_CHANGED', description='snake direction was changed',
                        params={"previous": self._current_direction, "current": new_direction})
            self._current_direction = new_direction
        if new_direction == self.oposite[self._current_direction]:
            logger.warning('OPPOSITE_DIRECTION_CHANGED', description='snake cannot move backwards',
                           params={"current": self._current_direction, "opposite": new_direction})

        # Se a tecla for "return" ele troca os valores de self.__pause...
        elif new_direction == "return":
            if self._pause:
                self._pause = False
                logger.info('PLAYING_CONTINUED', description='playing was continued')
            else:
                self._pause = True
                logger.info('PLAYING_PAUSED', description='playing was paused')

    # Desenha uma nova cabeça na frente da cobra, com base na direção atual.
    def _move_snake_head(self, screen):
        self._snake_head = self._snake_body[0]

        # Pega as cordenadas da direção atual, com base nas cordenadas da cabeça da cobra.
        if self._current_direction == "right":
            self._ghost_snake_head = [self._snake_head[0], self._snake_head[1] + 1]

        elif self._current_direction == "left":
            self._ghost_snake_head = [self._snake_head[0], self._snake_head[1] - 1]

        elif self._current_direction == "up":
            self._ghost_snake_head = [self._snake_head[0] - 1, self._snake_head[1]]

        elif self._current_direction == "down":
            self._ghost_snake_head = [self._snake_head[0] + 1, self._snake_head[1]]

        # Desenha a nova cabeça com as novas cordenadas na tela.
        screen.addstr(
            self._ghost_snake_head[0],
            self._ghost_snake_head[1],
            self._snake_body_fill
        )

        # Depois, salva essas novas cordenadas na lista em memória.
        self._snake_body.insert(0, self._ghost_snake_head)

    # Remove a cauda da cobra, tanto em memória quanto em tela, e contar um ponto.
    def _remove_the_tail(self, screen):
        if self._snake_head == self.apple:
            self.score[1] += 1
            logger.info('APPLE_EATEN', description='apple was eaten, snake grew up',
                        params={"scope": self.score[1], "snake_length": len(self._snake_body)})
            self._spawn_apple(screen)

            screen.addstr(2, 7, f" Score: {self.score[1]} ")

        else:
            screen.addstr(
                self._snake_body[-1][0],
                self._snake_body[-1][1],
                " "
            )

            self._snake_body.pop()

    # Condições para perder no jogo.
    def _condictions_to_lose(self):
        if (
            # Se a cabeça da cobra bater nas quinas do mapa...
            self._snake_head[0] <= 2 or self._snake_head[0] >= self._y_len - 3
            or self._snake_head[1] <= 5 or self._snake_head[1] >= self._x_len - 6
        ):
            logger.info('SNAKE_DIED', description='snake ran into a wall',
                        params={"scope": self.score[1], "snake_length": len(self._snake_body)})
            return 1
        if (
                # Se a cabeça da cobra bater no seu próprio corpo...
                self._ghost_snake_head in self._snake_body[1:]
        ):
            logger.info('SNAKE_DIED', description='snake ran into its body part',
                        params={"scope": self.score[1], "snake_length": len(self._snake_body)})
            return 1


class ScoreBoard(Globals):
    """
     *  SCORE BOARD: Armazena todo os histórico de pontuação do jogador,
     *  junto com a data de cada partida. Também é responsável por carregar
     *  e mostrar a lista formatada na tela.
    """

    def __init__(self):
        super().__init__()
        self._score_list = list()
        # self.__score_list = [["lafjkdslfjadslf", 123], ["lafjkdslfjadslf", 123], ["lafjkdslfjadslf", 123]]
        self._y_value = 3
        self._x_value = 7

    @property
    def start(self):
        logger.info('SCORE_OPENED', description='score board was opened')
        curses.wrapper(self._run)
        logger.info('SCORE_CLOSED', description='score board was closed')

    def _run(self, screen):
        curses.curs_set(False)
        screen.clear()

        self._loop(screen)

    def _loop(self, screen):
        while 1:
            for key, value in enumerate(self._score_list):
                # Isso garante que a lista será escrita na tela toda...
                try:
                    screen.addstr(
                        self._y_value + key,
                        self._x_value,
                        f"[{value[0]}] >>> {value[1]}"
                    )
                except:
                    pass

            # Se qualquer tecla for precionada, o loop será interrompido.
            self._key = screen.getch()

            if self._key in self.keys["return"]:
                break

    def add_score(self, score):
        # Se a lista estiver vazia, basta anexar o único score registrado.
        if len(self._score_list) == 0:
            self._score_list.append(score)
            logger.info('SCORE_ADDED', description='new score was added', params={"rank": 1, "score": score[1]})
            return

        # Procura uma posição para adicionar o novo valor.
        for key, value in enumerate(self._score_list):
            if score[1] > value[1]:
                self._score_list.insert(key, score)
                logger.info('SCORE_ADDED', description='new score was added', params={"rank": key + 1, "score": score[1]})
                break

            elif score[1] == value[1]:
                self._score_list.insert(key + 1, score)
                logger.info('SCORE_ADDED', description='new score was added', params={"rank": key + 2, "score": score[1]})
                break

            elif key == len(self._score_list) - 1:
                self._score_list.append(score)
                logger.info('SCORE_ADDED', description='new score was added',
                            params={"rank": len(self._score_list), "score": score[1]})
                break

