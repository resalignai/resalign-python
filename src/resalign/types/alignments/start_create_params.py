# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StartCreateParams"]


class StartCreateParams(TypedDict, total=False):
    analysis_id: Required[str]
    """ID of a completed analysis to build roadmap from"""
