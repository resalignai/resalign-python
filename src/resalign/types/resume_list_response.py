# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ResumeListResponse", "Resume"]


class Resume(BaseModel):
    """Individual resume item in the list."""

    id: str
    """Resume file ID"""

    created_at: str = FieldInfo(alias="createdAt")
    """Upload timestamp"""

    name: str
    """Original filename"""

    size: int
    """File size in bytes (0 if not stored)"""

    type: str
    """File extension (pdf, docx, etc.)"""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Last update timestamp"""

    url: str
    """Download URL for the resume"""

    json_data: Optional[Dict[str, object]] = None
    """Extracted resume data (null if pending)"""


class ResumeListResponse(BaseModel):
    """Response containing list of user's resumes."""

    resumes: List[Resume]
    """List of uploaded resumes"""
