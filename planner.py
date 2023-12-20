import time


class Planner:
    def __init__(self):
        """
        Инициализация класса задача
        """
        self.daily_planner = {}

    def add_task(self, task, date=time.strftime('%Y-%m-%d', time.localtime())):
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

    def remove_task(self, task, date=time.strftime('%Y-%m-%d', time.localtime())):
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

    def view_tasks(self, date=time.strftime('%Y-%m-%d', time.localtime())):
        """
        Функция для просмотра дел на определенную дату

        :param date: Дата
        :return: None
        """
        if date in self.daily_planner:
            print(f"\nДела на {date}:")
            for task in self.daily_planner[date]:
                print(f"- {task}")
        else:
            print(f"\nНа {date} нет дел")

    def view_all_tasks(self):
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

    def generate_report(self, start_date, end_date):
        """
        Функция для создания отчета по делам за определенный период

        :param start_date: Дата начала периода
        :param end_date: Дата конца периода
        :return: None
        """
        report = {}
        for date in self.daily_planner:
            if start_date <= date <= end_date:
                report[date] = self.daily_planner[date]
        if len(report) > 0:
            print(f"\nОтчет за период с {start_date} по {end_date}:")
            for date in report:
                print(f"{date}:")
                for task in report[date]:
                    print(f"- {task}")
        else:
            print(f"\nЗа период с {start_date} по {end_date} нет дел")


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
    todo.view_tasks("2023-12-31")
    todo.view_tasks("2024-01-01")
    todo.view_all_tasks()
    todo.generate_report("2023-12-31", "2024-01-01")


if __name__ == "__main__":
    main()
