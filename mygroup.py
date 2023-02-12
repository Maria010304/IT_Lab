
groupmates = [
    {
        "name": "Александр",
        "surname": "Анохин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Козлов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Антон",
        "surname": "Бойченко",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Николай",
        "surname": "Барышкин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 3]

    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        marks_list = student['marks']
        result = (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
need = int(input())

print_students(groupmates)

