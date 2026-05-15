# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaxonomyListRolesParams"]


class TaxonomyListRolesParams(TypedDict, total=False):
    function: Required[str]
    """Job function key, e.g. software_engineering"""
