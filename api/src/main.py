import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.database import get_db


app = FastAPI()

@app.get("/")
def index():
    return { "message": "hello world" }


@app.get("/companies/")
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_companies(db=db, skip=skip, limit=limit)


@app.post("/companies/")
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = crud.get_company_by_name(db=db, name=company.name)
    if db_company:
        raise HTTPException(status_code=400, detail="Company already exists")
    
    return crud.create_company(db=db, company=company)


if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000)