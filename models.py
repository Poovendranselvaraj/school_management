from sqlalchemy import (
    Column, String, Integer, Float, Date, ForeignKey, Time
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Models
class YearLevel(Base):
    __tablename__ = 'year_level'
    id = Column(Integer, primary_key=True)
    level_name = Column(String, nullable=False)
    level_order = Column(Integer, nullable=False)
    students = relationship("StudentYearLevel", back_populates="year_level")

class SchoolYear(Base):
    __tablename__ = 'school_year'
    id = Column(Integer, primary_key=True)
    year_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    terms = relationship("Term", back_populates="school_year")

class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer, primary_key=True)
    year_id = Column(Integer, ForeignKey('school_year.id'), nullable=False)
    term_number = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    school_year = relationship("SchoolYear", back_populates="terms")
    classes = relationship("Class", back_populates="term")

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    given_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    classes = relationship("Class", back_populates="teacher")

class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    term_id = Column(Integer, ForeignKey('term.id'), nullable=False)
    start_period_id = Column(Integer, nullable=False)
    end_period_id = Column(Integer, nullable=False)
    classroom_id = Column(Integer, ForeignKey('classroom.id'), nullable=False)
    name = Column(String, nullable=False)
    teacher = relationship("Teacher", back_populates="classes")
    term = relationship("Term", back_populates="classes")
    subject = relationship("Subject", back_populates="classes")
    classroom = relationship("Classroom", back_populates="classes")
    students = relationship("StudentClass", back_populates="class_")

class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    subject_name = Column(String, nullable=False)
    department = relationship("Department", back_populates="subjects")
    classes = relationship("Class", back_populates="subject")

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    department_name = Column(String, nullable=False)
    subjects = relationship("Subject", back_populates="department")

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    given_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    surname = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    enrolment_date = Column(Date, nullable=False)
    year_levels = relationship("StudentYearLevel", back_populates="student")
    guardians = relationship("StudentGuardian", back_populates="student")
    classes = relationship("StudentClass", back_populates="student")

class StudentYearLevel(Base):
    __tablename__ = 'student_year_level'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    level_id = Column(Integer, ForeignKey('year_level.id'), primary_key=True)
    year_id = Column(Integer, ForeignKey('school_year.id'), primary_key=True)
    score = Column(Float, nullable=False)
    student = relationship("Student", back_populates="year_levels")
    year_level = relationship("YearLevel", back_populates="students")

class StudentClass(Base):
    __tablename__ = 'student_class'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.id'), primary_key=True)
    score = Column(Float, nullable=False)
    student = relationship("Student", back_populates="classes")
    class_ = relationship("Class", back_populates="students")

class ScoreRange(Base):
    __tablename__ = 'score_range'
    id = Column(Integer, primary_key=True)
    min_score = Column(Float, nullable=False)
    max_score = Column(Float, nullable=False)
    grade = Column(String, nullable=False)

class Guardian(Base):
    __tablename__ = 'guardian'
    id = Column(Integer, primary_key=True)
    given_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email_address = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    guardianship = relationship("StudentGuardian", back_populates="guardian")

class GuardianType(Base):
    __tablename__ = 'guardian_type'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    guardianships = relationship("StudentGuardian", back_populates="guardian_type")

class StudentGuardian(Base):
    __tablename__ = 'student_guardian'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    guardian_type_id = Column(Integer, ForeignKey('guardian_type.id'), primary_key=True)
    guardian_id = Column(Integer, ForeignKey('guardian.id'), primary_key=True)
    student = relationship("Student", back_populates="guardians")
    guardian = relationship("Guardian", back_populates="guardianship")
    guardian_type = relationship("GuardianType", back_populates="guardianships")

class Classroom(Base):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)
    room_type = Column(Integer, ForeignKey('classroom_types.id'), nullable=False)
    room_name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    classes = relationship("Class", back_populates="classroom")

class ClassroomTypes(Base):
    __tablename__ = 'classroom_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    classrooms = relationship("Classroom", back_populates="room_type")

class Period(Base):
    __tablename__ = 'period'
    id = Column(Integer, primary_key=True)
    year_id = Column(Integer, ForeignKey('school_year.id'), nullable=False)
    name = Column(String, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
