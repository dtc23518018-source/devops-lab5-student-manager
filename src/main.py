
from student import Student

# Danh sách sinh viên
students = [
    Student("SV001", "Nguyen Van A", 20, 8.5),
    Student("SV002", "Tran Thi B", 21, 9.0),
    Student("SV003", "Le Van C", 19, 7.5)
]


# Chức năng thêm sinh viên
def add_student(student):
    students.append(student)
    print("Them sinh vien thanh cong!")


# Chức năng tìm kiếm sinh viên
def search_student(student_id):
    for student in students:
        if student.student_id == student_id:
            return student

    return None


# Chương trình chính
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

    print("\n===== TIM KIEM SINH VIEN =====")
    search_id = input("Nhap ma sinh vien can tim: ")

    result = search_student(search_id)

    if result:
        print("Tim thay sinh vien:")
        print(result)
    else:
        print("Khong tim thay sinh vien!")


if __name__ == "__main__":
    main()
