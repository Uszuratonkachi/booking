from app.hotels.models import Hotels
from app.dao.base import BaseDAO


class HotelDAO(BaseDAO):
    model = Hotels


