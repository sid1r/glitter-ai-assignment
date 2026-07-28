import time

from sqlalchemy.orm import Session

from app import crud, schemas
from fastapi import HTTPException


def create_generation_job(db: Session, job: schemas.JobCreate):
    db_job = crud.create_job(db, job)

    crud.update_job_status(db, db_job.id, "processing")

    time.sleep(10)

    image_url = "https://placehold.co/600x400/png?text=Generated+Image"

    crud.update_image_url(db, db_job.id, image_url)

    crud.update_job_status(db, db_job.id, "completed")

    return db_job

def get_job(db: Session, job_id: int):
    job = crud.get_job(db, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job