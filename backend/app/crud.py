from sqlalchemy.orm import Session

from app import models, schemas

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        product_name=job.product_name,
        description=job.description,
        product_image=job.product_image,
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def get_job(db: Session, job_id: int) -> models.Job | None:
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def update_job_status(db: Session, job_id: int, status: str) -> models.Job | None:
    job = get_job(db, job_id)

    if job:
        job.status = status
        db.commit()
        db.refresh(job)

    return job

def update_image_url(db: Session, job_id: int, image_url: str):
    job = get_job(db, job_id)

    if job:
        job.image_url = image_url
        db.commit()
        db.refresh(job)

    return job