# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CompanyResearchEnrichResponse"]


class CompanyResearchEnrichResponse(BaseModel):
    """Immediate 202 response confirming enrichment has been queued."""

    companies_queued: int
    """Number of companies queued for enrichment"""

    message: str
    """Status message"""
