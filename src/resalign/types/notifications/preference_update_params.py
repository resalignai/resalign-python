# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PreferenceUpdateParams"]


class PreferenceUpdateParams(TypedDict, total=False):
    email_enabled: Required[bool]

    event_type: Required[str]
