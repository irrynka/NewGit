import sqlite3
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    instructor TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses (
    student_id,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id),
    PRIMARY KEY (student_id,course_id)
)
''')

while(True):
    print("\n1.Додати нового студента")
    print("\2.Додати новий курс")
    print("\n3.Показати список студентів")
    print("\n4.Показати список курсів")
    print("\n5.Зареєструвати студента на курс")
    print("\n6.Показати студентів на конкретному курсі")
    print("\n7.Вийти")
    choise = input("Оберіть опцію 1-7")
    if choise =="1":
        name = input("Введіть ім'я студента")
        age = int(input("Введіть вік"))
        major = input("Введіть спеціальність студента")
        cursor.execute("INSERT INTO students(name,age,major) VALUES (?,?,?)", (name,age,major))
        conn.commit()
    elif choise == "2":
        course=input("Введіть назву курсу")
        instructor=input("Введіть викладача курсу")
        cursor.execute("INSERT INTO courses(course,instructor) VALUES (?,?)", (course,instructor))
        conn.commit()
    elif choise == "3":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if not students:
            print("База порожня")
        else:
            print("\nСписок студентів")
            for i in students:
                print(f"ID: {i[0]}, Ім'я: {i[1]}, Вік: {i[2]}, Спеціальність: {i[3]}")
    elif choise == "4":
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        if not courses:
            print("База порожня")
        else:
            print("\nСписок курсів")
            for i in courses:
                print(f"ID: {i[0]}, Назва курсу: {i[1]}, Викладач: {i[2]}")
    elif choise == "5":
        student_id= int(input("Введіть ID студенту"))
        course_id= int(input("Введіть ID курсу"))
        cursor.execute("INSERT INTO courses(student_id,course_id) VALUES (?,?)", (student_id,course_id))
        conn.commit()
    elif choise == "6":
        course_id= int(input("Введіть ID курсу"))
        cursor.execute('''SELECT student.id, student.name, student.age, student.major
                    FROM students, student_courses
                    WHERE students.id = student_courses.student.id
                    AND student_courses.course_id = ?''', (course_id))
        students_on_course.fetchall()
        if not students_on_course:
            print("На цьому курсі немає студентів")
        else:
            print("Список студентів на курсі")
            for i in students_on_course:
                print(f"ID: {i[0]}, Ім'я: {i[1]}, Вік: {i[2]}, Спеціальність: {i[3]}")
    elif choise == "7":
        break
    else:
        print("Оберіть опцію 1-7")



conn.close()