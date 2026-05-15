# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompanyResearchRunParams"]


class CompanyResearchRunParams(TypedDict, total=False):
    company_name: Required[str]
    """Name of the company to research"""

    stream: bool
    """Return SSE stream instead of JSON"""

    company_directory_id: Optional[str]
    """UUID from companies_directory for idempotency"""

    linkedin_url: Optional[str]
    """Company LinkedIn page URL"""

    website_url: Optional[str]
    """Company website URL"""
