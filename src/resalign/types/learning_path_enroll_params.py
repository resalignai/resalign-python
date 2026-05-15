# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LearningPathEnrollParams"]


class LearningPathEnrollParams(TypedDict, total=False):
    alignment_id: Required[str]
    """Alignment ID to enroll from"""

    skill: Required[str]
    """Skill name to enroll in"""
