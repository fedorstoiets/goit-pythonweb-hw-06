import random

from faker import Faker

from database import SessionLocal
from models import Grade, Group, Student, Subject, Teacher


fake = Faker()


def seed_database() -> None:
    with SessionLocal() as session:
        groups = [
            Group(name="CS-101"),
            Group(name="CS-102"),
            Group(name="CS-103"),
        ]

        session.add_all(groups)
        session.flush()

        teachers = [Teacher(name=fake.name()) for _ in range(random.randint(3, 5))]

        session.add_all(teachers)
        session.flush()

        subject_names = [
            "Mathematics",
            "Physics",
            "Programming",
            "Databases",
            "Algorithms",
            "Computer Networks",
            "Web Development",
            "Data Science",
        ]

        random.shuffle(subject_names)

        selected_subject_names = subject_names[: random.randint(5, 8)]

        subjects: list[Subject] = []

        # Ensure every teacher has at least one subject
        for teacher, subject_name in zip(
            teachers,
            selected_subject_names,
        ):
            subjects.append(
                Subject(
                    name=subject_name,
                    teacher=teacher,
                )
            )

        # Distribute remaining subjects randomly
        for subject_name in selected_subject_names[len(teachers) :]:
            subjects.append(
                Subject(
                    name=subject_name,
                    teacher=random.choice(teachers),
                )
            )

        session.add_all(subjects)
        session.flush()

        students = [
            Student(
                name=fake.name(),
                group=random.choice(groups),
            )
            for _ in range(random.randint(30, 50))
        ]

        session.add_all(students)
        session.flush()

        grades: list[Grade] = []

        for student in students:
            for _ in range(random.randint(10, 20)):
                grades.append(
                    Grade(
                        student=student,
                        subject=random.choice(subjects),
                        grade=random.randint(60, 100),
                        date_received=fake.date_between(
                            start_date="-1y",
                            end_date="today",
                        ),
                    )
                )

        session.add_all(grades)
        session.commit()

        print("Database seeded successfully.")
        print(f"Groups: {len(groups)}")
        print(f"Teachers: {len(teachers)}")
        print(f"Subjects: {len(subjects)}")
        print(f"Students: {len(students)}")
        print(f"Grades: {len(grades)}")


if __name__ == "__main__":
    seed_database()
