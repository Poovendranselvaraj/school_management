from pydantic import BaseModel
from datetime import date, time
from typing import List, Optional

# YearLevel schemas
class YearLevelBase(BaseModel):
    level_name: str
    level_order: int

class YearLevelCreate(YearLevelBase):
    pass

class YearLevel(YearLevelBase):
    id: int
    class Config:
        orm_mode = True

# SchoolYear schemas
class SchoolYearBase(BaseModel):
    year_name: str
    start_date: date
    end_date: date

class SchoolYearCreate(SchoolYearBase):
    pass

class SchoolYear(SchoolYearBase):
    id: int
    class Config:
        orm_mode = True

# Teacher schemas
class TeacherBase(BaseModel):
    given_name: str
    surname: str
    gender: str
    email_address: str
    phone_number: Optional[str] = None

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    class Config:
        orm_mode = True

# Student schemas
class StudentBase(BaseModel):
    given_name: str
    middle_name: Optional[str] = None
    surname: str
    date_of_birth: date
    gender: str
    enrolment_date: date

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True

# Guardian schemas
class GuardianBase(BaseModel):
    given_name: str
    surname: str
    email_address: Optional[str] = None
    phone_number: Optional[str] = None

class GuardianCreate(GuardianBase):
    pass

class Guardian(GuardianBase):
    id: int
    class Config:
        orm_mode = True

# Department schemas
class DepartmentBase(BaseModel):
    department_name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

# Subject schemas
class SubjectBase(BaseModel):
    department_id: int
    subject_name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class Config:
        orm_mode = True

# Class schemas
class ClassBase(BaseModel):
    subject_id: int
    teacher_id: int
    term_id: int
    start_period_id: int
    end_period_id: int
    classroom_id: int
    name: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    class Config:
        orm_mode = True

# Classroom schemas
class ClassroomBase(BaseModel):
    room_type_id: int
    room_name: str
    capacity: int

class ClassroomCreate(ClassroomBase):
    pass

class Classroom(ClassroomBase):
    id: int
    class Config:
        orm_mode = True
