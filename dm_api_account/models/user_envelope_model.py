from enum import Enum
from datetime import datetime
from pydantic import BaseModel, StrictStr, Field, StrictBool
from typing import List, Optional


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = None
    small_picture_url: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[datetime] = None
    name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    registration: Optional[datetime] = None


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = None

