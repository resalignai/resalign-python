# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["TaxonomyListFunctionsResponse", "Function"]


class Function(BaseModel):
    key: str

    label: str


class TaxonomyListFunctionsResponse(BaseModel):
    functions: List[Function]
