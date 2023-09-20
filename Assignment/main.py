from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, id):
        self.id = id


class Repository(ABC):
    @abstractmethod
    def add(self, entity):
        print(f"Adding {entity.__class__.__name__} with ID {entity.id}")

    @abstractmethod
    def update(self, entity):
        print(f"Updating {entity.__class__.__name__} with ID {entity.id}")

    @abstractmethod
    def delete(self, entity):
        print(f"Deleting {entity.__class__.__name__} with ID {entity.id}")

    @abstractmethod
    def get_by_id(self, id):
        pass


class UnitOfWork(ABC):

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class Student(Entity):
    def __init__(self, id, name, email):
        super().__init__(id)
        self.name = name
        self.email = email


class Course(Entity):
    def __init__(self, id, title, credits):
        super().__init__(id)
        self.title = title
        self.credits = credits


class Professor(Entity):
    def __init__(self, id, name, department_id):
        super().__init__(id)
        self.name = name
        self.department_id = department_id


class Enrollment(Entity):
    def __init__(self, id, student_id, course_id):
        super().__init__(id)
        self.student_id = student_id
        self.course_id = course_id


class Department(Entity):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name


class StudentRepository(Repository):
    def __init__(self):
        self.students = []

    def add(self, student):
        super().add(student)
        self.students.append(student)

    def update(self, student):
        super().update(student)
        existing_student = self.get_by_id(student.id)
        if existing_student:
            existing_student.name = student.name
            existing_student.email = student.email

    def delete(self, student):
        super().delete(student)
        self.students.remove(student)

    def get_by_id(self, id):
        return next((s for s in self.students if s.id == id), None)


class CourseRepository(Repository):
    def __init__(self):
        self.courses = []

    def add(self, course):
        super().add(course)
        self.courses.append(course)

    def update(self, course):
        super().update(course)
        existing_course = self.get_by_id(course.id)
        if existing_course:
            existing_course.title = course.title
            existing_course.credits = course.credits

    def delete(self, course):
        super().delete(course)
        self.courses.remove(course)

    def get_by_id(self, id):
        return next((c for c in self.courses if c.id == id), None)


class ProfessorRepository(Repository):
    def __init__(self):
        self.professors = []

    def add(self, professor):
        super().add(professor)
        self.professors.append(professor)

    def update(self, professor):
        super().update(professor)
        existing_professor = self.get_by_id(professor.id)
        if existing_professor:
            existing_professor.name = professor.name
            existing_professor.department_id = professor.department_id

    def delete(self, professor):
        super().delete(professor)
        self.professors.remove(professor)

    def get_by_id(self, id):
        return next((p for p in self.professors if p.id == id), None)


class EnrollmentRepository(Repository):
    def __init__(self):
        self.enrollments = []

    def add(self, enrollment):
        super().add(enrollment)
        self.enrollments.append(enrollment)

    def update(self, enrollment):
        super().update(enrollment)
        existing_enrollment = self.get_by_id(enrollment.id)
        if existing_enrollment:
            existing_enrollment.student_id = enrollment.student_id
            existing_enrollment.course_id = enrollment.course_id

    def delete(self, enrollment):
        super().delete(enrollment)
        self.enrollments.remove(enrollment)

    def get_by_id(self, id):
        return next((e for e in self.enrollments if e.id == id), None)


class DepartmentRepository(Repository):
    def __init__(self):
        self.departments = []

    def add(self, department):
        super().add(department)
        self.departments.append(department)

    def update(self, department):
        super().update(department)
        existing_department = self.get_by_id(department.id)
        if existing_department:
            existing_department.name = department.name

    def delete(self, department):
        super().delete(department)
        self.departments.remove(department)

    def get_by_id(self, id):
        return next((d for d in self.departments if d.id == id), None)


class UniversityUnitOfWork(UnitOfWork):
    def __init__(self):
        self.student_repository = StudentRepository()
        self.course_repository = CourseRepository()
        self.professor_repository = ProfessorRepository()
        self.enrollment_repository = EnrollmentRepository()
        self.department_repository = DepartmentRepository()

    def commit(self):
        pass

    def rollback(self):
        pass


if __name__ == "__main__":
    uow = UniversityUnitOfWork()

    student1 = Student(id=1, name="Fahad Shafique", email="fahad@example.com")
    course1 = Course(id=1, title="Introduction to Computer Science", credits=3)
    professor1 = Professor(id=1, name="Dr. Madeeha", department_id=1)
    enrollment1 = Enrollment(id=1, student_id=1, course_id=1)
    department1 = Department(id=1, name="Computer Science")

    # Adding entities
    uow.student_repository.add(student1)
    uow.course_repository.add(course1)
    uow.professor_repository.add(professor1)
    uow.enrollment_repository.add(enrollment1)
    uow.department_repository.add(department1)

    # Updating entities
    student1.name = "John Smith"
    uow.student_repository.update(student1)

    # Getting entities by ID
    retrieved_student = uow.student_repository.get_by_id(1)
    if retrieved_student:
        print(f"Retrieved student: {retrieved_student.name}")

    # Deleting entities
    uow.student_repository.delete(student1)
