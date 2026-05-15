# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FavoriteAddResponse"]


class FavoriteAddResponse(BaseModel):
    """Response after successfully saving a job to favorites."""

    job_posting_id: str
    """ID of the saved job posting"""

    message: str
    """Success message"""
