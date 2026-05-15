# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FavoriteDeleteResponse"]


class FavoriteDeleteResponse(BaseModel):
    """Response after successfully removing a job from favorites."""

    job_posting_id: str
    """ID of the removed job posting"""

    message: str
    """Success message"""
