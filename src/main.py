
from student import Student

def main():
    students = [
        Student("SV001", "Nguyen Van A", 20, 8.5),
        Student("SV002", "Tran Thi B", 21, 9.0),
        Student("SV003", "Le Van C", 19, 7.5)
    ]

    print("===== DANH SACH SINH VIEN =====")

    for student in students:
        print(student)


if __name__ == "__main__":
    main()
