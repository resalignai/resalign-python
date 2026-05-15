# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .job_posting import JobPosting

__all__ = ["FetchListResponse"]


class FetchListResponse(BaseModel):
    """Paginated list of job postings."""

    has_more: bool
    """Whether more pages are available"""

    items: List[JobPosting]
    """List of job postings"""

    page: int
    """Current page number"""

    page_size: int
    """Number of items per page"""

    total: int
    """Total number of jobs matching filters"""
