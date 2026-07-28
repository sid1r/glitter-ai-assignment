from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, services

router = APIRouter()
@router.post("/jobs", response_model=schemas.JobResponse)
def create_job(
    job: schemas.JobCreate,
    db: Session = Depends(get_db),
):
    return services.create_generation_job(db, job)


@router.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
):
    return services.get_job(db, job_id)