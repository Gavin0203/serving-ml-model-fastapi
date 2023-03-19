from pydantic import BaseModel


class ScoringItem(BaseModel):
    YearsAtCompany : float
    EmployeeSatisfaction : float 
    Position : str
    Salary : int