# app/config.py

import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env="DATABASE_URL")
    token_secret: str = Field(..., env="JWT_SECRET")


settings = Settings()
