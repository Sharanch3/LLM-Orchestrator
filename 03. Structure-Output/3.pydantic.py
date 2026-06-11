from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Nitish"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt = 10, default=5, description="A decimal value representation the cgpa of student")

new_student = {'age': '32','email':'abc@gmail.com'}  #pydantic is smart enough to do type conversion behind the scene or type coercion 

student = Student(**new_student)

print(student.age)

student_json = student.model_dump_json()