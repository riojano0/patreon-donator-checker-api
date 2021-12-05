from enum import Enum

from pydantic import BaseModel


class Tier(str, Enum):
    TIER_1 = "Tier 1"
    TIER_2 = "Tier 2"
    TIER_3 = "Tier 3"


class Status(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class PatreonResponse:

    def __init__(self, patron_id, username, status=Status.INACTIVE, mail="", tier=None, total_amount=0):
        self.id = patron_id
        self.username = username
        self.mail = mail
        self.status = status
        self.tier = tier
        self.total_amount = total_amount


class PatreonModel(BaseModel):
    id: str
    user_name: str
    mail: str
    status: Status
    tier: Tier
    total_amount: int
