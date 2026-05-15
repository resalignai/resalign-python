# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import AssessmentAutoAssessResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssessments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_auto_assess(self, client: Resalign) -> None:
        assessment = client.assessments.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
        )
        assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_auto_assess_with_all_params(self, client: Resalign) -> None:
        assessment = client.assessments.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
            trigger="trigger",
            x_service_key="X-Service-Key",
        )
        assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_auto_assess(self, client: Resalign) -> None:
        response = client.assessments.with_raw_response.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assessment = response.parse()
        assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_auto_assess(self, client: Resalign) -> None:
        with client.assessments.with_streaming_response.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assessment = response.parse()
            assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssessments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_auto_assess(self, async_client: AsyncResalign) -> None:
        assessment = await async_client.assessments.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
        )
        assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_auto_assess_with_all_params(self, async_client: AsyncResalign) -> None:
        assessment = await async_client.assessments.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
            trigger="trigger",
            x_service_key="X-Service-Key",
        )
        assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_auto_assess(self, async_client: AsyncResalign) -> None:
        response = await async_client.assessments.with_raw_response.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assessment = await response.parse()
        assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_auto_assess(self, async_client: AsyncResalign) -> None:
        async with async_client.assessments.with_streaming_response.auto_assess(
            job_id="job_id",
            tier="tier",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assessment = await response.parse()
            assert_matches_type(AssessmentAutoAssessResponse, assessment, path=["response"])

        assert cast(Any, response.is_closed) is True
