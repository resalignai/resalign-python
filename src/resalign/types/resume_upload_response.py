# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ResumeUploadResponse"]


class ResumeUploadResponse(BaseModel):
    """Response after successfully uploading a resume."""

    id: str
    """Unique file ID"""

    name: str
    """Original filename"""

    size: int
    """File size in bytes"""

    type: str
    """File extension"""

    url: str
    """Download URL for the resume"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Creation timestamp"""

    json_data: None = None
    """Extracted data (null initially, populated asynchronously)"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Last update timestamp"""
