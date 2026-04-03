import argparse
from gradebook import service
from gradebook.utils import parse_grade, validate_empty


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add-student
    p1 = subparsers.add_parser("add-student")
    p1.add_argument("--name", required=True)

    # add-course
    p2 = subparsers.add_parser("add-course")
    p2.add_argument("--code", required=True)
    p2.add_argument("--title", required=True)

    # enroll
    p3 = subparsers.add_parser("enroll")
    p3.add_argument("--student-id", type=int, required=True)
    p3.add_argument("--course", required=True)

    # add-grade
    p4 = subparsers.add_parser("add-grade")
    p4.add_argument("--student-id", type=int, required=True)
    p4.add_argument("--course", required=True)
    p4.add_argument("--grade", required=True)  # ndryshuar (pa type=int)

    # list
    p5 = subparsers.add_parser("list")
    p5.add_argument("type", choices=["students", "courses", "enrollments"])
    p5.add_argument("--sort", choices=["name", "code"])

    # avg
    p6 = subparsers.add_parser("avg")
    p6.add_argument("--student-id", type=int, required=True)
    p6.add_argument("--course", required=True)

    # gpa
    p7 = subparsers.add_parser("gpa")
    p7.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            name = validate_empty(args.name, "Name")
            sid = service.add_student(name)
            print(f"Student added with ID: {sid}")

        elif args.command == "add-course":
            code = validate_empty(args.code, "Course code")
            title = validate_empty(args.title, "Title")
            service.add_course(code, title)
            print("Course added")

        elif args.command == "enroll":
            service.enroll(args.student_id, args.course)
            print("Enrollment successful")

        elif args.command == "add-grade":
            grade = parse_grade(args.grade)
            service.add_grade(args.student_id, args.course, grade)
            print("Grade added")

        elif args.command == "list":
            if args.type == "students":
                for s in service.list_students(args.sort):
                    print(s)

            elif args.type == "courses":
                for c in service.list_courses(args.sort):
                    print(c)

            elif args.type == "enrollments":
                for e in service.list_enrollments():
                    print(e)

        elif args.command == "avg":
            avg = service.compute_average(args.student_id, args.course)
            print(f"Average: {avg:.2f}")

        elif args.command == "gpa":
            gpa = service.compute_gpa(args.student_id)
            print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()