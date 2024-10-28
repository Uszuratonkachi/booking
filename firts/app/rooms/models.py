from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base
from sqlalchemy import ForeignKey, JSON


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    services: Mapped[Optional[list[str]]] = mapped_column(JSON)
    image_id: Mapped[int]