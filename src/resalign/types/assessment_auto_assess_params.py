# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssessmentAutoAssessParams"]


class AssessmentAutoAssessParams(TypedDict, total=False):
    job_id: Required[str]

    tier: Required[str]

    user_id: Required[str]

    trigger: str

    x_service_key: Annotated[str, PropertyInfo(alias="X-Service-Key")]
