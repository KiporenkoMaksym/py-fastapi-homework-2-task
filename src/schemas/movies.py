from datetime import date

from pydantic import BaseModel

from database.models import MovieStatusEnum


class MovieBaseSchema(BaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country_id: int
    genre_ids: list[int]
    actor_ids: list[int]
    language_ids: list[int]


class MovieCreateSchema(MovieBaseSchema):
    pass


class MovieUpdateSchema(MovieBaseSchema):
    pass


class MovieReadSchema(MovieBaseSchema):
    id: int
