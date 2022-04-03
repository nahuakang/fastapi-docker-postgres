from pydantic import BaseModel


class JobBase(BaseModel):
    title: str
    description: str


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int
    company_id: int

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    jobs: list[Job] = []

    class Config:
        orm_mode = True
