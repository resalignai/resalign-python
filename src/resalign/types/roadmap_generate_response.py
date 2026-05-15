# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RoadmapGenerateResponse",
    "Roadmap",
    "RoadmapATSKeywords",
    "RoadmapGapAnalysis",
    "RoadmapRoadmapSummary",
    "RoadmapStage",
    "RoadmapStageEstimatedEffort",
]


class RoadmapATSKeywords(BaseModel):
    """ATS keywords from JD"""

    must_include: List[str]
    """Terms from requirements (high ATS weight)"""

    nice_to_include: List[str]
    """Terms from role description"""

    should_include: List[str]
    """Terms from preferred qualifications"""


class RoadmapGapAnalysis(BaseModel):
    """A prioritized skill gap for the roadmap."""

    category: str
    """One of: technical_craft, domain_business, behavioral, adaptive_meta"""

    current_evidence: str
    """What the candidate currently has"""

    estimated_learning_hours: int
    """Realistic hours to close gap"""

    gap_description: str
    """Human-readable description of what's missing"""

    match_level: Literal["unmatched", "partial"]
    """unmatched or partial"""

    priority: Literal["CRITICAL", "IMPORTANT", "NICE_TO_HAVE"]
    """CRITICAL, IMPORTANT, or NICE_TO_HAVE"""

    required_level: str
    """What the JD demands for this skill"""

    score_impact_estimate: float
    """Estimated score improvement (1-20 points)"""

    skill: str
    """The specific skill or competency"""


class RoadmapRoadmapSummary(BaseModel):
    """High-level roadmap overview"""

    classification: str
    """STRONG_FIT, GOOD_FIT, LOW_FIT, or NOT_FIT"""

    critical_path: List[str]
    """Stage IDs on the critical path"""

    current_score: float
    """Current fit score"""

    estimated_timeline_weeks: str
    """Human-readable timeline range (e.g., '6-10 weeks')"""

    executive_summary: str
    """2-3 paragraph personalized summary of the roadmap"""

    knockout_applied: bool
    """Whether knockout gate fired"""

    knockout_skills: List[str]
    """CRITICAL skills that triggered knockout (empty if none)"""

    score_gap: float
    """Points needed to reach target"""

    target_score: float
    """Target score (default 85.0)"""

    total_estimated_hours_high: int
    """High end of total effort"""

    total_estimated_hours_low: int
    """Low end of total effort"""

    total_included_stages: int
    """Number of stages included"""


class RoadmapStageEstimatedEffort(BaseModel):
    """Effort estimate"""

    daily_commitment: str
    """Expected daily time (e.g., '1-2 hours/day')"""

    hours_high: int
    """High end estimate"""

    hours_low: int
    """Low end estimate"""

    weeks: str
    """Timeline range (e.g., '2-3')"""


class RoadmapStage(BaseModel):
    """A stage in the career roadmap."""

    included: bool
    """Whether this stage is included in the roadmap"""

    inclusion_rationale: str
    """1-2 sentences explaining why included/skipped"""

    stage_id: str
    """Stage identifier"""

    stage_number: int
    """Stage number (1-10)"""

    title: str
    """Human-readable stage title"""

    actionable_steps: Optional[List[str]] = None
    """3-7 specific actions to take"""

    estimated_effort: Optional[RoadmapStageEstimatedEffort] = None
    """Effort estimate"""

    intensity: Optional[Literal["light", "moderate", "comprehensive"]] = None
    """light, moderate, comprehensive"""

    objectives: Optional[List[str]] = None
    """2-5 specific objectives"""

    parallel_with: Optional[List[str]] = None
    """Stage IDs that can run concurrently"""

    prerequisites: Optional[List[str]] = None
    """Stage IDs that must come first"""

    priority: Optional[Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]] = None
    """CRITICAL, HIGH, MEDIUM, LOW"""

    resources_hint: Optional[List[str]] = None
    """Types/topics of resources to seek"""

    skills_addressed: Optional[List[str]] = None
    """Skills from gap_analysis addressed here"""

    success_criteria: Optional[List[str]] = None
    """2-5 concrete, self-assessable criteria"""


class Roadmap(BaseModel):
    """The complete roadmap"""

    ats_keywords: RoadmapATSKeywords
    """ATS keywords from JD"""

    gap_analysis: List[RoadmapGapAnalysis]
    """Prioritized skill gaps (max 7)"""

    roadmap_summary: RoadmapRoadmapSummary
    """High-level roadmap overview"""

    stages: List[RoadmapStage]
    """Exactly 10 stages"""


class RoadmapGenerateResponse(BaseModel):
    """Response after generating a career roadmap."""

    analysis_id: str
    """The source analysis ID"""

    roadmap: Roadmap
    """The complete roadmap"""

    roadmap_id: str
    """The generated roadmap ID"""
