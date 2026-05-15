# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RoadmapGenerateParams"]


class RoadmapGenerateParams(TypedDict, total=False):
    analysis_id: Required[str]
    """The analysis ID (contains fit assessment and JD)"""
