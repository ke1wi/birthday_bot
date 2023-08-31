import csv
from datetime import date
from app.student import Student
from random import randint

class Logic:
    
    congrats_message: str
    presents: list = ["тортик🎂"]

    @staticmethod
    def _get_dm() -> str:
        today = str(date.today()).split("-")
        return ".".join([today[i] for i in range(2, 0, -1)])
    
    @classmethod            
    def get_birthday(self) -> list[Student]:
        students_to_congrates = []
        with open("table/table_for_bot.csv", "r") as upd_file:
            date = csv.reader(upd_file)
            list_of_students = [Student(row[0].split(' ')[1], row[1], row[2]) for row in date]
        for i in range(0, len(list_of_students)):
            if self._get_dm() == list_of_students[i].birthday[:5]:
                students_to_congrates.append(list_of_students[i])
        return students_to_congrates
    
    @classmethod
    def create_congrats(self, students: list[Student]) -> str:
        if len(students) == 0:
            return "Сьогодні ніхто не гуляє."
        if len(students) == 1:
            return f"Шановне панство, сьогодні {students[0].name}({students[0].tag}) святкує своє день народження.\nНумо привітаємо вельмешановного(ну).\nЯ почну. Ось Тобі {self.presents[randint(0, 0)]}"
        if len(students) == 2:
            return f"Шановне панство, яке щастя!!! Сьогодні святкує своє день народження {students[0].name}({students[0].tag}) та {students[1].name}({students[1].tag}\nНумо привітаємо вельмешановних.\nЯ почну. Ось вам {self.presents[randint(0, 0)]} на двох, бо в мене ліміт - один тортик на день."
    
    @classmethod
    def send_congrats(self):
        students = self.get_birthday()
        return self.create_congrats(students)
    
    @classmethod
    def check(self):
        if len(self.get_birthday()) != 0:
            return "Someone has bd today."
        else:
            return "Noone has bd today"
    
        
