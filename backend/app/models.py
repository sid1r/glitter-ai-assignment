from sqlalchemy import Integer, String, DateTime
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    product_name: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=False)

    product_image: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[str] = mapped_column(String, default="pending")

    image_url: Mapped[str | None] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)