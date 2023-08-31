from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Extra, Field, StrictStr

class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')