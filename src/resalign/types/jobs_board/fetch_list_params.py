# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FetchListParams"]


class FetchListParams(TypedDict, total=False):
    company_size: Optional[str]
    """Filter by company size: startup, small, medium, large, enterprise"""

    department: Optional[str]
    """Filter by department"""

    employment_type: Optional[str]
    """Filter by employment type: full-time, part-time, contract, internship"""

    location_type: Optional[str]
    """Filter by location type: remote, hybrid, onsite"""

    organization_type: Optional[str]
    """
    Filter by organization type: startup, scaleup, established, non-profit,
    government
    """

    page: int
    """Page number (1-indexed)"""

    page_size: int
    """Items per page (max 50)"""

    salary_max: Optional[int]
    """Maximum salary filter"""

    salary_min: Optional[int]
    """Minimum salary filter"""

    search: Optional[str]
    """Full-text search on title and description"""

    sort_by: Literal["newest", "salary_high", "salary_low"]
    """Sort order"""
