# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PreferenceUpdateResponse"]


class PreferenceUpdateResponse(BaseModel):
    email_enabled: bool

    event_type: str

    updated: bool
