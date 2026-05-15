# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ResumeRetryExtractionResponse"]


class ResumeRetryExtractionResponse(BaseModel):
    """Response after triggering resume extraction retry."""

    message: str
    """Status message"""

    resume_id: str
    """Resume file ID"""

    status: str
    """Extraction status (extraction_started or already_extracted)"""
