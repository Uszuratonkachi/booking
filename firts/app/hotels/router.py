from fastapi import APIRouter, Depends

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel, HotelSearchArgs

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)

@router.get("", response_model=list[SHotel])  # Используем список объектов SHotel
async def get_hotels():
    return await HotelDAO.find_all()

@router.get("/search")
async def search_hotels(args: HotelSearchArgs = Depends()):
    # args содержит аргументы поиска отелей
    return await HotelDAO.search_hotels(args)