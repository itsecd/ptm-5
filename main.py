import csv


class StudentJournal:
    def __init__(self):
        self.students = []

    def check_student_by_id(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return True
        return False

    def add_student(
        self,
        student_id,
        date_of_birth,
        average_grade,
        attended_lectures,
        total_lectures,
        passed_exam,
    ):
        new_student = {
            "id": student_id,
            "date_of_birth": date_of_birth,
            "average_grade": average_grade,
            "attended_lectures": attended_lectures,
            "total_lectures": total_lectures,
            "passed_exam": passed_exam,
        }
        self.students.append(new_student)

    def remove_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                return

    def sort_by_average_grade(self, reverse=True):
        self.students.sort(key=lambda x: x["average_grade"], reverse=reverse)

    def sort_by_attended_lectures(self, reverse=True):
        self.students.sort(key=lambda x: x["attended_lectures"], reverse=reverse)

    def is_allowed_to_exam(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                if (
                    student["passed_exam"]
                    and student["average_grade"] >= 3.5
                    and student["attended_lectures"] / student["total_lectures"] >= 0.5
                ):
                    return True
                else:
                    return False
        return False

    def update_average_grade(self, student_id, new_grade):
        for student in self.students:
            if student["id"] == student_id:
                student["average_grade"] = new_grade
                return

    def read_from_csv(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.students.append(row)

    def write_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            fieldnames = [
                "id",
                "date_of_birth",
                "average_grade",
                "attended_lectures",
                "total_lectures",
                "passed_exam",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow(student)


if __name__ == "__main__":
    journal = StudentJournal()

    journal.add_student("1", "2000-01-01", 3.8, 20, 30, True)
    journal.add_student("2", "1999-05-15", 2.5, 15, 30, False)
    journal.add_student("3", "2001-11-30", 4.0, 25, 30, True)
    journal.add_student("4", "1998-03-20", 3.2, 18, 30, True)
    journal.add_student("5", "2002-07-10", 3.7, 22, 30, True)
    journal.add_student("6", "1997-09-25", 2.9, 17, 30, False)
    journal.add_student("7", "2003-12-05", 3.5, 21, 30, True)
    journal.add_student("8", "1996-04-12", 4.0, 28, 30, True)
    journal.add_student("9", "2004-08-18", 2.0, 12, 30, False)
    journal.add_student("10", "1995-10-29", 3.9, 27, 30, True)

    journal.remove_student(102)
    journal.sort_by_average_grade()
    journal.sort_by_attended_lectures()
    print(journal.is_allowed_to_exam("1"))
    print(journal.is_allowed_to_exam("2"))
    print(journal.is_allowed_to_exam("3"))

    journal.write_to_csv("students.csv")