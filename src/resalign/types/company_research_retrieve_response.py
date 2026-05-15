# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyResearchRetrieveResponse"]


class CompanyResearchRetrieveResponse(BaseModel):
    """Status-only response for a company research profile."""

    company_profile_id: str
    """company_profiles row ID"""

    status: str
    """Research status: in_progress, completed, failed"""

    error: Optional[str] = None
    """Error message (present only when status is failed)"""
