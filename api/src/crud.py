from sqlalchemy.orm import Session

from src import schemas
from src.models.company import Company
from src.models.job import Job


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Company).offset(skip).limit(limit).all()


def get_company_by_name(db: Session, name: str):
    return db.query(Company).filter(Company.name == name).first()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Job).offset(skip).limit(limit).all()


def create_company(db: Session, company: schemas.CompanyCreate) -> Company:
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


def create_job(db: Session, job: schemas.JobCreate, company_id: int) -> Job:
    db_job = Job(**job.dict(), company_id=company_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job
