from .storage import load_data, save_data
import logging

def add_student(name):
    data = load_data()

    new_id = 1 if not data["students"] else max(s["id"] for s in data["students"]) + 1

    student = {"id": new_id, "name": name}
    data["students"].append(student)

    save_data(data)
    logging.info(f"Student added: {name} (ID: {new_id})")
    return new_id

def add_course(code, title):
    data = load_data()
    if any(c["code"] == code for c in data["courses"]):
        raise ValueError("Ekziston...")
    
    data["courses"].append({"code": code, "title": title})
    save_data(data)

def enroll(student_id, course_id):
    data = load_data()
    if not any(s["id"] == student_id for s in data["students"]):
        raise ValueError("Ska student...")
    
    if not any(c["code"] == course_id for c in data["courses"]):
        raise ValueError("Ska course...")
    
    if any(e["student_id"] == student_id and e["course_id"] == course_id
           for e in data["enrollments"]):
        raise ValueError("Regjistruar...")
    
    data["enrollments"].append({
        "student_id": student_id,
        "course_id": course_id,
        "grades": []
    })

    save_data(data)

def add_grade(student_id, course_id, grade):
    if not(0 <= grade <=100):
        raise ValueError("0-100...")

    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_id"] == course_id:
            e["grades"].append(grade)
            save_data(data)
            logging.info(f"Grade {grade} added for student {student_id}")
            return
        
    raise ValueError("Ska regjistrim")

def list_students(sort_by=None):
    data = load_data()
    students = data["students"]

    if sort_by == "name":
        students = sorted(students, key=lambda s: s["name"])

    return students

def list_courses(sort_by=None):
    data = load_data()
    courses = data["courses"]

    if sort_by == "code":
        courses = sorted(courses, key=lambda c: c["code"]) 

    return courses

def list_enrollments(sort_by=None):
    data = load_data()
    return data["enrollments"]

def compute_average(student_id, course_id):
    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_id"] == course_id:
            if not e["grades"]:
                return 0 
            return sum(e["grades"]) / len(e["grades"])
        
    raise ValueError("Ska regjistrim...")

def compute_gpa(student_id):
    data = load_data()

    averages = [
        sum(e["grades"]) / len(e["grades"])
        for e in data["enrollments"]
        if e["student_id"] == student_id and e["grades"]
    ]

    if not averages:
        return 0 
    
    return sum(averages) / len(averages)