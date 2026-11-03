
from student import Student

students = [
    Student("SV001", "Nguyen Van A", 20, 8.5),
    Student("SV002", "Tran Thi B", 21, 9.0),
    Student("SV003", "Le Van C", 19, 7.5)
]


def add_student(student):
    students.append(student)
    print("Them sinh vien thanh cong!")


def main():
    print("===== DANH SACH SINH VIEN =====")

    for student in students:
        print(student)

    print("\n===== THEM SINH VIEN =====")
    new_student = Student("SV004", "Pham Van D", 20, 8.0)
    add_student(new_student)

    print("\n===== DANH SACH SAU KHI THEM =====")
    for student in students:
        print(student)


if __name__ == "__main__":
    main()
