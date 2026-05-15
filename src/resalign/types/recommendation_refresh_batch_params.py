# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecommendationRefreshBatchParams"]


class RecommendationRefreshBatchParams(TypedDict, total=False):
    report_id: Optional[str]

    tier: Literal["free", "student", "pro", "all"]

    trigger: Optional[str]

    x_service_key: Annotated[str, PropertyInfo(alias="X-Service-Key")]
