# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NotificationDeliverResponse"]


class NotificationDeliverResponse(BaseModel):
    status: str

    claimed: Optional[int] = None

    failed: Optional[int] = None

    sent: Optional[int] = None

    skipped_disabled: Optional[int] = None

    skipped_frequency: Optional[int] = None

    skipped_preference: Optional[int] = None
