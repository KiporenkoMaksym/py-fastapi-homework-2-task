from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.session_sqlite import sqlite_engine
from src.routes import movie_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await sqlite_engine.dispose()


app = FastAPI(
    title="Movies homework",
    description="Description of project",
    lifespan=lifespan
)

api_version_prefix = "/api/v1"

app.include_router(movie_router, prefix=f"{api_version_prefix}/theater", tags=["theater"])
