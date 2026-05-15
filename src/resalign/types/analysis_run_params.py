# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnalysisRunParams"]


class AnalysisRunParams(TypedDict, total=False):
    jd_id: Required[str]
    """Job ID from jobs_board table"""

    resume_id: Required[str]
    """Resume file_id from resumes table"""

    stream: bool
    """Return SSE stream instead of JSON"""
