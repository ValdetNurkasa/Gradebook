from gradebook import service


def seed():
    s1 = service.add_student("Ai")
    s2 = service.add_student("Ajo")
    s3 = service.add_student("Ne/Ju")

    service.add_course("EE414", "Intro to EE")
    service.add_course("MATH408", "Basic Math")

    service.enroll(s1, "EE414")
    service.enroll(s2, "EE414")
    service.enroll(s3, "MATH408")

    service.add_grade(s1, "EE414", 90)
    service.add_grade(s1, "EE414", 85)

    service.add_grade(s2, "EE414", 75)

    service.add_grade(s3, "MATH408", 88)
    service.add_grade(s3, "MATH408", 92)

    print("Seed created")


if __name__ == "__main__":
    seed()