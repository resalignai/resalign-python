# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["PreferenceRetrieveResponse", "Preference"]


class Preference(BaseModel):
    email_enabled: bool

    event_type: str


class PreferenceRetrieveResponse(BaseModel):
    preferences: List[Preference]
