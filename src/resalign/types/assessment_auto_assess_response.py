# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AssessmentAutoAssessResponse"]


class AssessmentAutoAssessResponse(BaseModel):
    status: str

    analysis_id: Optional[str] = None

    fit_score: Optional[float] = None

    reason: Optional[str] = None
