# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JobPosting"]


class JobPosting(BaseModel):
    """Serialized job posting with company name and saved status."""

    id: str
    """Unique job posting ID"""

    company_id: str
    """Company ID"""

    company_name: str
    """Company name"""

    first_seen_at: str
    """Timestamp when job was first seen"""

    job_title: str
    """Job title"""

    apply_url: Optional[str] = None
    """URL to apply for the job"""

    company_logo: Optional[str] = None
    """Company logo URL"""

    company_size: Optional[str] = None
    """Company size category"""

    department: Optional[str] = None
    """Department or team"""

    employment_type: Optional[str] = None
    """Employment type (full-time, part-time, etc.)"""

    is_saved: Optional[bool] = None
    """Whether user has saved this job"""

    job_description_text: Optional[str] = None
    """Full job description"""

    location: Optional[str] = None
    """Job location"""

    location_type: Optional[str] = None
    """Location type (remote, hybrid, onsite)"""

    organization_type: Optional[str] = None
    """Organization type"""

    salary_currency: Optional[str] = None
    """Salary currency code"""

    salary_interval: Optional[str] = None
    """Salary interval (yearly, hourly, etc.)"""

    salary_max: Optional[int] = None
    """Maximum salary"""

    salary_min: Optional[int] = None
    """Minimum salary"""
