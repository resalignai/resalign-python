# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompanyResearchEnrichParams"]


class CompanyResearchEnrichParams(TypedDict, total=False):
    concurrency: int
    """Max concurrent Parallel research tasks"""

    limit: Optional[int]
    """Maximum number of companies to enrich in this run"""

    stale_days: int
    """Re-enrich profiles whose updated_at is older than this many days"""

    x_service_key: Annotated[str, PropertyInfo(alias="X-Service-Key")]
