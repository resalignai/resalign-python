# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WeightFields"]


class WeightFields(BaseModel):
    evidence: str
    """Evidence for the weight"""

    reasoning: str
    """Reasoning for the weight"""

    weight: float
    """Weight of the category (0-1)"""
