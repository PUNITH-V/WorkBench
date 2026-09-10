from pydantic import BaseModel
from typing import Literal


class SupportTicket(BaseModel):
    customer_name: str
    issue_category: Literal["billing", "technical", "account", "other"]
    sentiment: Literal["positive", "neutral", "negative"]

