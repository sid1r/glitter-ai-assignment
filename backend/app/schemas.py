from pydantic import BaseModel


class JobCreate(BaseModel):
    product_name: str
    description: str
    product_image: str


class JobResponse(BaseModel):
    id: int
    product_name: str
    description: str
    product_image: str
    status: str
    image_url: str | None = None

    class Config:
        from_attributes = True