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


class Info(BaseModel):
    value: StrictStr
    parse_mode: StrictStr


class PagingSettings(BaseModel):
    posts_per_page: int
    comments_per_page: int
    topics_per_page: int
    messages_per_page: int
    entities_per_page: int


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class UserSettings(BaseModel):
    color_schema: List[ColorSchema]
    nanny_greetings_message: Optional[StrictStr]
    paging: PagingSettings


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
    icq: StrictStr
    skype: StrictStr
    original_picture_url: StrictStr
    info: Info
    settings: UserSettings


class UserDetailsEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = None
