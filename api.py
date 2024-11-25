from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management API")

# Student endpoints
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Teacher endpoints
@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.get("/teachers/", response_model=List[schemas.Teacher])
def read_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teachers = db.query(models.Teacher).offset(skip).limit(limit).all()
    return teachers

@app.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# Class endpoints
@app.post("/classes/", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

@app.get("/classes/", response_model=List[schemas.Class])
def read_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = db.query(models.Class).offset(skip).limit(limit).all()
    return classes

@app.get("/classes/{class_id}", response_model=schemas.Class)
def read_class(class_id: int, db: Session = Depends(get_db)):
    class_ = db.query(models.Class).filter(models.Class.id == class_id).first()
    if class_ is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_

# Department endpoints
@app.post("/departments/", response_model=schemas.Department)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = models.Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

@app.get("/departments/", response_model=List[schemas.Department])
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = db.query(models.Department).offset(skip).limit(limit).all()
    return departments

# Subject endpoints
@app.post("/subjects/", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    db_subject = models.Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@app.get("/subjects/", response_model=List[schemas.Subject])
def read_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subjects = db.query(models.Subject).offset(skip).limit(limit).all()
    return subjects

# Guardian endpoints
@app.post("/guardians/", response_model=schemas.Guardian)
def create_guardian(guardian: schemas.GuardianCreate, db: Session = Depends(get_db)):
    db_guardian = models.Guardian(**guardian.dict())
    db.add(db_guardian)
    db.commit()
    db.refresh(db_guardian)
    return db_guardian

@app.get("/guardians/", response_model=List[schemas.Guardian])
def read_guardians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    guardians = db.query(models.Guardian).offset(skip).limit(limit).all()
    return guardians
