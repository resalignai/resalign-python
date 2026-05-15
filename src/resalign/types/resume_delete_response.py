# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ResumeDeleteResponse"]


class ResumeDeleteResponse(BaseModel):
    """Response after successfully deleting a resume."""

    message: str
    """Success message"""

    resume_id: str
    """ID of the deleted resume"""
