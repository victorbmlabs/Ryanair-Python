from dataclasses import dataclass, asdict, fields
from datetime import datetime
import time
import abc


class Base(abc.ABC):

    def __init__(self):
        if type(self) is Base:  # Check if instantiated directly
            raise TypeError("Cannot instantiate the abstract 'Base' class")

    @classmethod
    def field_names(cls) -> list[str]:
        return [f.name for f in fields(cls)]

    @abc.abstractmethod
    def dict(self) -> dict:
        pass


@dataclass
class Flight(Base):
    departure_time: datetime
    flight_number: str
    price: float
    currency: str
    origin: str
    origin_city: str
    origin_country: str
    destination: str
    destination_city: str
    destination_country: str
    updated_at: datetime = None
    departure_date: str = None
    _id: str = None

    def __post_init__(self):
        if not self.departure_date:
            self.departure_date = self.departure_time.strftime("%Y/%m/%d")

        if not self._id:
            self._id = self._get_hash()

        self.updated_at = datetime.now()

    def __lt__(self, other):
        return self.price < other.price

    def _get_hash(self) -> str:
        id = (
            self.origin
            + self.destination
            + str(time.mktime(self.departure_time.timetuple()))
            + self.flight_number
        )
        return hash(id)

    def dict(self) -> dict:
        return {k: str(v) for k, v in asdict(self).items()}

    def mongo_dict(self) -> dict:
        return {
            "_id": self._id,
            "departure_time": self.departure_time,
            "departure_date": self.departure_date,
            "price": self.price,
            "flight_number": self.flight_number,
            "currency": self.currency,
            "origin": self.origin,
            "origin_city": self.origin_city,
            "origin_country": self.origin_country,
            "destination": self.destination,
            "destination_city": self.destination_city,
            "destination_country": self.destination_country,
            "updated_at": self.updated_at,
        }


@dataclass
class Trip(Base):
    total_price: float
    outbound: Flight
    inbound: Flight

    def dict(self) -> dict:
        return {k: str(v) for k, v in asdict(self).items()}
