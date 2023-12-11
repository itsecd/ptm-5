import logging
import csv


class To_do_list:
    def __init__(self) -> None:
        """
        initializing fields of the 'To do list' class
        """
        self.jobs = dict()
        self.logger = self.create_logger()

    def add_job(self, job: str, level: int) -> None:
        """
        Adding job and its level in dict
        """
        try:
            if self.find_job(job) == False:
                self.jobs[job] = level
                self.logger.info(f"add {job} in to-do-list")
        except Exception as e:
            self.logger.warning(
                "the occurrence of an error when deleting a job: " + f"{str(e)}")

    def delete_job(self, job: str) -> None:
        """
        Deleting job and its level from dict
        """
        try:
            if self.find_job(job) == True:
                self.jobs.pop(job)
                self.logger.info(f"delete {job} from to-do-list")
        except Exception as e:
            self.logger.warning(
                "the occurrence of an error when deleting a job: " + f"{str(e)}")

    def print_to_do_list(self) -> None:
        """
        Output a list of jobs and levels to the terminal
        """
        self.logger.info("output to-do-list")
        for job in self.jobs.keys():
            print(job, self.jobs[job])

    def count_job(self) -> int:
        """
        Calculating and output count of jobs
        """
        self.logger.info("output count of jobs")
        return len(self.jobs.keys())

    def find_job(self, job: str) -> bool:
        """
        Finding job in dict
        """
        try:
            if job in self.jobs.keys():
                self.logger.info(f"{job} was found")
                return True
            else:
                return False
        except Exception as e:
            self.logger.warning(
                "the occurrence of an error when finding a job: " + f"{str(e)}")

    def sorting_by_level(self) -> None:
        """
        Sorting dict with jobs by level
        """
        self.jobs = dict(sorted(self.jobs.items(), key=lambda x: x[1]))
        self.logger.info("to-do-list was sorted by significance level")

    def clear_list(self) -> None:
        """
        Clearing entire dict
        """
        self.jobs.clear()
        self.logger.info("clearing the entire to-do-list")

    def write_csv(self, file: str) -> None:
        """
        Writing dict with jobs in csv-file
        """
        try:
            with open(file, 'w', newline='') as name:
                writer = csv.writer(name)
                for job in self.jobs.keys():
                    writer.writerow([job])
                self.logger.info(f"writing data in: {file}")
        except FileNotFoundError:
            self.logger.warning(f"File '{file}' was not found")

    def create_logger(self) -> logging.LoggerAdapter:
        """
        Creating logger for event tracking
        """
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        file = logging.FileHandler('py_logger.log')
        file.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[%(asctime)s]: [%(name)s] - [%(levelname)s] - [%(message)s]')
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger


if __name__ == "__main__":
    try:
        to_do_list = To_do_list()
        to_do_list.add_job("Go to shop", 5)
        to_do_list.add_job("Clear room", 10)
        to_do_list.add_job("Pick up package", 9)
        to_do_list.add_job("Cook dinner", 6)
        to_do_list.add_job("Hard gym", 8)
        to_do_list.add_job("Finish lab of asm", 9)
        to_do_list.add_job("Finish lectures", 2)
        to_do_list.delete_job("Finish lectures")
        to_do_list.delete_job("Go to dance")
        print("Count of jobs = ", to_do_list.count_job())
        to_do_list.sorting_by_level()
        to_do_list.write_csv("to-do-list.csv")
        to_do_list.print_to_do_list()
        to_do_list.clear_list()
    except Exception as e:
        logging.warning("the occurrence of an error: " + f"{str(e)}")
