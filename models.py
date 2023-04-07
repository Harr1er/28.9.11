from pydantic import BaseModel, Field


class Period(BaseModel):
    checkin: str = Field(...)
    checkout: str = Field(...)


class BookingModel(BaseModel):
    bookingid: int = Field(None)
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    bookingdates: Period = Field(None)
    state: str = Field(None)


class PeriodLite(BaseModel):
    checkin: str = Field(None)
    checkout: str = Field(None)


class LiteBookingModel(BaseModel):
    firstname: str = Field(None)
    lastname: str = Field(None)
    totalprice: int = Field(None)
    depositpaid: bool = Field(None)
    bookingdates: PeriodLite = Field(None)
    state: str = Field(None)


class Token(BaseModel):
    token: str = Field(...)


class FilterModel(BaseModel):
    firstname: str = Field(None)
    lastname: str = Field(None)
    checkin: str = Field(None)
    checkout: str = Field(None)