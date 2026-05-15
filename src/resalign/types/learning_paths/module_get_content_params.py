# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ModuleGetContentParams"]


class ModuleGetContentParams(TypedDict, total=False):
    path_id: Required[str]

    generate: bool

    topic_index: int
