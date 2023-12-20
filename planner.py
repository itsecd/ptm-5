import time


class Planner:
    def __init__(self):
        """
        Инициализация класса задача
        """
        self.daily_planner = {}

    def add_task(self, task: str, date=time.strftime('%Y-%m-%d', time.localtime())) -> None:
        """
        Функция для добавления дела в ежедневник

        :param task: Дело
        :param date: Дата выполнения дела
        :return: None
        """
        if date in self.daily_planner:

            self.daily_planner[date].append(task)
        else:
            self.daily_planner[date] = [task]

        print(f"Добавлено дело '{task}' на {date}")

    def remove_task(self, task: str, date=time.strftime('%Y-%m-%d', time.localtime())) -> None:
        """
        Функция для удаления дела из ежедневника

        :param task:  Дело
        :param date:  Дата выполнения дела
        :return: None
        """
        if date in self.daily_planner and task in self.daily_planner[date]:
            self.daily_planner[date].remove(task)
            print(f"Дело '{task}' удалено из {date}")
            check = ""
            for task in self.daily_planner[date]:
                check += task
            if date in self.daily_planner and len(check) == 0:
                self.daily_planner.pop(date)
        else:
            print(f"Дело '{task}' не найдено на {date}")

    def view_tasks(self, date=time.strftime('%Y-%m-%d', time.localtime())) -> str:
        """
        Функция для просмотра дел на определенную дату

        :param date: Дата
        :return: None
        """
        if date in self.daily_planner:
            result = ""
            result += f"\nДела на {date}:"
            for task in self.daily_planner[date]:
                result += f"\n- {task}"
            return result
        else:
            return f"\nНа {date} нет дел"

    def view_all_tasks(self) -> None:
        """
        Функция для просмотра всех дел в ежедневнике

        :return: None
        """
        if len(self.daily_planner) > 0:
            print("\nЕжедневник:")
            for date in self.daily_planner:
                print(f"{date}:")
                for task in self.daily_planner[date]:
                    print(f"- {task}")
        else:
            print("\nЕжедневник пуст")

    def generate_report(self, start_date: str, end_date: str) -> str:
        """
        Функция для создания отчета по делам за определенный период

        :param start_date: Дата начала периода
        :param end_date: Дата конца периода
        :return: Отчет
        """
        report = []
        for date in self.daily_planner:
            if start_date <= date <= end_date:
                report.append(date)
        if len(report) == 0:
            return f"За период с {start_date} по {end_date} нет дел\n"
        else:
            result = f"Отчет за период с {start_date} по {end_date}\n\n"
            for date in report:
                result += f"{date}:\n"
                for task in self.daily_planner[date]:
                    result += f"- {task}\n"
            return result

    @staticmethod
    def save_to_txt(filename: str, report: str) -> None:
        """
       Сохраняет отчет в txt файл

       :param filename: Имя файла для сохранения
       :param report: Отчет, сохраняемы в файл
       :return: None
        """
        with open(filename, 'w') as file:
            file.write(report)

    def load_from_txt(self, filename: str) -> None:
        """
       Загружает отчет из txt файла

       :param filename: Имя файла для сохранения
       :return: None
        """
        with open(filename, 'r') as file:
            text = file.read().split("\n\n", 1)
            str(text.pop(0))
            text = text[0].split(":")
            date = str(text[0])
            tasks = text[1].replace("\n", "").split("- ")
            tasks.pop(0)
            for task in tasks:
                self.add_task(task, date)

    def delete_all_tasks(self) -> None:
        """
        Функция очистки ежедневника

        :return: None
        """
        if len(self.daily_planner) > 0:
            self.daily_planner.clear()
            if len(self.daily_planner) == 0:
                print("\nЕжедневник пуст")
        else:
            print("\nЕжедневник пуст")


def main():
    todo = Planner()
    todo.add_task("Купить продукты", "2023-12-31")
    todo.add_task("Лекция по ТЗИ", "2023-12-31")
    todo.add_task("Сходить в спортзал","2023-12-31")
    todo.add_task("Сделать лабу по ТМП", "2023-12-31")
    todo.add_task("Встреча с другом", "2023-12-31")
    todo.add_task("Лечь спать вовремя", "2024-01-01")
    todo.remove_task("Лечь спать вовремя", "2024-01-01")
    todo.remove_task("Лечь спать вовремя", "2024-01-01")
    print(todo.view_tasks("2023-12-31"))
    print(todo.view_tasks("2024-01-01"))
    todo.view_all_tasks()
    report = todo.generate_report("2023-12-31", "2024-01-01")
    print(f"\n{report}")
    todo.save_to_txt("report_1.txt", report)
    todo.load_from_txt("report_1.txt")
    todo.delete_all_tasks()


if __name__ == "__main__":
    main()
