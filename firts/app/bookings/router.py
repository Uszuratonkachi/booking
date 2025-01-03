from datetime import date
from fastapi import APIRouter, Request
from fastapi.params import Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

# Маршрут для получения всех бронирований
@router.get("/")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)

# Маршрут для добавления нового бронирования
@router.post("/")
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user),
):
    # Добавление нового бронирования
    await BookingDAO.add(user.id, room_id, date_from, date_to)

