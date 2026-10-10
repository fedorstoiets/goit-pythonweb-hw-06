from sqlalchemy import func, select

from database import SessionLocal
from models import Grade, Group, Student, Subject


def select_1():
    with SessionLocal() as session:
        statement = (
            select(
                Student.name,
                func.round(func.avg(Grade.grade), 2).label("average_grade"),
            )
            .join(Grade)
            .group_by(Student.id)
            .order_by(func.avg(Grade.grade).desc())
            .limit(5)
        )
        return session.execute(statement).all()


def select_2(subject_id: int):
    with SessionLocal() as session:
        statement = (
            select(
                Student.name,
                func.round(func.avg(Grade.grade), 2).label("average_grade"),
            )
            .join(Grade)
            .where(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(func.avg(Grade.grade).desc())
            .limit(1)
        )
        return session.execute(statement).all()


def select_3(subject_id: int):
    with SessionLocal() as session:
        statement = (
            select(
                Group.name,
                func.round(func.avg(Grade.grade), 2).label("average_grade"),
            )
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .where(Grade.subject_id == subject_id)
            .group_by(Group.id)
        )
        return session.execute(statement).all()


def select_4():
    with SessionLocal() as session:
        statement = select(func.round(func.avg(Grade.grade), 2).label("average_grade"))
        return session.execute(statement).scalar()


def select_5(teacher_id: int):
    with SessionLocal() as session:
        statement = select(Subject.name).where(Subject.teacher_id == teacher_id)
        return session.execute(statement).scalars().all()


def select_6(group_id: int):
    with SessionLocal() as session:
        statement = (
            select(Student.name)
            .where(Student.group_id == group_id)
            .order_by(Student.name)
        )
        return session.execute(statement).scalars().all()


def select_7(group_id: int, subject_id: int):
    with SessionLocal() as session:
        statement = (
            select(
                Student.name,
                Grade.grade,
                Grade.date_received,
            )
            .join(Grade, Grade.student_id == Student.id)
            .where(
                Student.group_id == group_id,
                Grade.subject_id == subject_id,
            )
            .order_by(Student.name)
        )
        return session.execute(statement).all()


def select_8(teacher_id: int):
    with SessionLocal() as session:
        statement = (
            select(func.round(func.avg(Grade.grade), 2).label("average_grade"))
            .join(Subject, Grade.subject_id == Subject.id)
            .where(Subject.teacher_id == teacher_id)
        )
        return session.execute(statement).scalar()


def select_9(student_id: int):
    with SessionLocal() as session:
        statement = (
            select(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .where(Grade.student_id == student_id)
            .distinct()
            .order_by(Subject.name)
        )
        return session.execute(statement).scalars().all()


def select_10(student_id: int, teacher_id: int):
    with SessionLocal() as session:
        statement = (
            select(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .where(
                Grade.student_id == student_id,
                Subject.teacher_id == teacher_id,
            )
            .distinct()
            .order_by(Subject.name)
        )
        return session.execute(statement).scalars().all()


if __name__ == "__main__":
    print("Select 1:", select_1())
    print("Select 2:", select_2(1))
    print("Select 3:", select_3(1))
    print("Select 4:", select_4())
    print("Select 5:", select_5(1))
    print("Select 6:", select_6(1))
    print("Select 7:", select_7(1, 1))
    print("Select 8:", select_8(1))
    print("Select 9:", select_9(1))
    print("Select 10:", select_10(1, 1))
