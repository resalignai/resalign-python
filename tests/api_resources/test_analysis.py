# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import AnalysisRunResponse, AnalysisGetQuotaResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalysis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        analysis = client.analysis.list()
        assert_matches_type(object, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.analysis.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = response.parse()
        assert_matches_type(object, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.analysis.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = response.parse()
            assert_matches_type(object, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_quota(self, client: Resalign) -> None:
        analysis = client.analysis.get_quota()
        assert_matches_type(AnalysisGetQuotaResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_quota(self, client: Resalign) -> None:
        response = client.analysis.with_raw_response.get_quota()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisGetQuotaResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_quota(self, client: Resalign) -> None:
        with client.analysis.with_streaming_response.get_quota() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisGetQuotaResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Resalign) -> None:
        analysis = client.analysis.run(
            jd_id="jd_id",
            resume_id="resume_id",
        )
        assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Resalign) -> None:
        analysis = client.analysis.run(
            jd_id="jd_id",
            resume_id="resume_id",
            stream=True,
        )
        assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Resalign) -> None:
        response = client.analysis.with_raw_response.run(
            jd_id="jd_id",
            resume_id="resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Resalign) -> None:
        with client.analysis.with_streaming_response.run(
            jd_id="jd_id",
            resume_id="resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalysis:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        analysis = await async_client.analysis.list()
        assert_matches_type(object, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.analysis.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = await response.parse()
        assert_matches_type(object, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.analysis.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = await response.parse()
            assert_matches_type(object, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_quota(self, async_client: AsyncResalign) -> None:
        analysis = await async_client.analysis.get_quota()
        assert_matches_type(AnalysisGetQuotaResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_quota(self, async_client: AsyncResalign) -> None:
        response = await async_client.analysis.with_raw_response.get_quota()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisGetQuotaResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_quota(self, async_client: AsyncResalign) -> None:
        async with async_client.analysis.with_streaming_response.get_quota() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisGetQuotaResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncResalign) -> None:
        analysis = await async_client.analysis.run(
            jd_id="jd_id",
            resume_id="resume_id",
        )
        assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncResalign) -> None:
        analysis = await async_client.analysis.run(
            jd_id="jd_id",
            resume_id="resume_id",
            stream=True,
        )
        assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncResalign) -> None:
        response = await async_client.analysis.with_raw_response.run(
            jd_id="jd_id",
            resume_id="resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncResalign) -> None:
        async with async_client.analysis.with_streaming_response.run(
            jd_id="jd_id",
            resume_id="resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisRunResponse, analysis, path=["response"])

        assert cast(Any, response.is_closed) is True
