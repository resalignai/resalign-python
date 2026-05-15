# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FavoriteListResponse", "Item"]


class Item(BaseModel):
    """Individual saved job item in the favorites list."""

    id: str
    """Job posting ID"""

    company_id: str
    """Company ID"""

    company_name: str
    """Company name"""

    created_at: str
    """Timestamp when job was saved"""

    job_title: str
    """Job title"""

    apply_url: Optional[str] = None
    """Application URL"""

    company_logo: Optional[str] = None
    """Company logo URL"""

    department: Optional[str] = None
    """Department"""

    employment_type: Optional[str] = None
    """Employment type"""

    first_seen_at: Optional[str] = None
    """First seen timestamp"""

    is_saved: Optional[bool] = None
    """Whether the job is saved"""

    job_description_text: Optional[str] = None
    """Job description"""

    location: Optional[str] = None
    """Job location"""

    location_type: Optional[str] = None
    """Location type"""

    salary_currency: Optional[str] = None
    """Salary currency"""

    salary_interval: Optional[str] = None
    """Salary interval"""

    salary_max: Optional[int] = None
    """Maximum salary"""

    salary_min: Optional[int] = None
    """Minimum salary"""


class FavoriteListResponse(BaseModel):
    """Response containing list of saved jobs."""

    items: List[Item]
    """List of saved job postings"""
