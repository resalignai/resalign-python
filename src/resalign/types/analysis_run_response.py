# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .weight_fields import WeightFields

__all__ = [
    "AnalysisRunResponse",
    "FitAssessment",
    "FitScore",
    "FitScoreCategoryBreakdown",
    "FitScoreCategoryMatches",
    "FitScoreCategoryWeights",
]


class FitAssessment(BaseModel):
    """LLM-generated fit assessment with strengths/weaknesses"""

    rationale: str
    """Rationale for the fit assessment for the candidate"""

    strengths: List[str]
    """Strengths of the candidate"""

    summary: str
    """Summary of the fit assessment for the candidate"""

    weaknesses: List[str]
    """Weaknesses of the candidate"""


class FitScoreCategoryBreakdown(BaseModel):
    """Detailed breakdown for a single category's score."""

    category: str
    """Category name"""

    match_ratio: float
    """Match ratio (matched/required, 0-1)"""

    matched_count: int
    """Number of matched skills"""

    required_count: int
    """Number of required skills"""

    weight: float
    """Category weight (0-1)"""

    weighted_score: float
    """Contribution to overall score"""

    matched_skills: Optional[List[str]] = None
    """List of matched skills"""


class FitScoreCategoryMatches(BaseModel):
    """Category wise matching skills"""

    adaptive_meta: Optional[List[str]] = None
    """Matched adaptive/meta skills"""

    behavioral: Optional[List[str]] = None
    """Matched behavioral skills"""

    domain_business: Optional[List[str]] = None
    """Matched domain/business skills"""

    technical_craft: Optional[List[str]] = None
    """Matched technical/craft skills"""


class FitScoreCategoryWeights(BaseModel):
    """Category weights with reasoning and evidence"""

    adaptive_meta: WeightFields
    """Weight of the adaptive and meta category"""

    behavioral: WeightFields
    """Weight of the behavioral category"""

    domain_business: WeightFields
    """Weight of the domain and business category"""

    technical_craft: WeightFields
    """Weight of the technical craft category"""


class FitScore(BaseModel):
    """Calculated fit score with category breakdowns"""

    category_breakdown: List[FitScoreCategoryBreakdown]
    """Detailed breakdown per category"""

    category_matches: FitScoreCategoryMatches
    """Category wise matching skills"""

    category_weights: FitScoreCategoryWeights
    """Category weights with reasoning and evidence"""

    classification: Literal["STRONG_FIT", "GOOD_FIT", "LOW_FIT", "NOT_FIT"]
    """Fit classification based on the overall score"""

    overall_score: float
    """Overall fit score (0-100)"""


class AnalysisRunResponse(BaseModel):
    """Response model for analyze endpoint.

    Contains the analysis results including fit score breakdown
    and LLM-generated assessment, along with references to the
    source documents.
    """

    analysis_id: str
    """Unique ID for this analysis session"""

    fit_assessment: FitAssessment
    """LLM-generated fit assessment with strengths/weaknesses"""

    fit_score: FitScore
    """Calculated fit score with category breakdowns"""

    jd_id: str
    """Job ID from jobs_board that was analyzed"""

    resume_id: str
    """Resume file_id that was analyzed"""
