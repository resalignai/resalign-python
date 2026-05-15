# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union

from .._models import BaseModel

__all__ = ["CompanyResearchResultResponse"]


class CompanyResearchResultResponse(BaseModel):
    """Response containing the research output."""

    company_name: str
    """Company name"""

    company_profile_id: str
    """company_profiles row ID"""

    status: str
    """Research status"""

    output: Union[str, Dict[str, object], None] = None
    """Research output (narrative + appendix)"""
