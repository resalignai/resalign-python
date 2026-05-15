# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaxonomySearchSkillsParams"]


class TaxonomySearchSkillsParams(TypedDict, total=False):
    limit: int
    """Max results"""

    q: str
    """Partial skill name to search for"""
