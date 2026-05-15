# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["JobsBoardRefreshResponse"]


class JobsBoardRefreshResponse(BaseModel):
    """Response model for job refresh endpoint."""

    message: str
    """Human-readable status message"""

    report_id: str
    """Unique report ID for tracking"""

    status: str
    """Processing status"""
