class Student:
    def __init__(self, id, name):
        if not name.strip():
            raise ValueError("Emri s'mundet...")
        
        self.id = id
        self.name = name

    def __str__(self):
        return f"Student[{self.id}]: {self.name}"

class Course:
    def __init__(self, code, title):
        if not code.strip() or not title.strip():
            raise ValueError("Kodi dhe Titulli smund...")

        self.code = code
        self.title = title

    def __str__(self):
        return f"Kursi [{self.code}]: {self.title}"


class Enrollment:
    def __init__(self, student_id, course_code, grades=None):      
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades is not None else []

        for grade in self.grades:
            if not(0 <= grade <= 100):
                raise ValueError("Notat duhet te...")
            
    def __str__(self):
        return f"{self.student_id} : {self.course_code}. Notat: {self.grades}"