# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import RecommendationRefreshBatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecommendations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        recommendation = client.recommendations.list()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.recommendations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommendation = response.parse()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.recommendations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommendation = response.parse()
            assert_matches_type(object, recommendation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh(self, client: Resalign) -> None:
        recommendation = client.recommendations.refresh()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh(self, client: Resalign) -> None:
        response = client.recommendations.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommendation = response.parse()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh(self, client: Resalign) -> None:
        with client.recommendations.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommendation = response.parse()
            assert_matches_type(object, recommendation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh_batch(self, client: Resalign) -> None:
        recommendation = client.recommendations.refresh_batch()
        assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh_batch_with_all_params(self, client: Resalign) -> None:
        recommendation = client.recommendations.refresh_batch(
            report_id="report_id",
            tier="free",
            trigger="trigger",
            x_service_key="X-Service-Key",
        )
        assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh_batch(self, client: Resalign) -> None:
        response = client.recommendations.with_raw_response.refresh_batch()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommendation = response.parse()
        assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh_batch(self, client: Resalign) -> None:
        with client.recommendations.with_streaming_response.refresh_batch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommendation = response.parse()
            assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRecommendations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        recommendation = await async_client.recommendations.list()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.recommendations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommendation = await response.parse()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.recommendations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommendation = await response.parse()
            assert_matches_type(object, recommendation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh(self, async_client: AsyncResalign) -> None:
        recommendation = await async_client.recommendations.refresh()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncResalign) -> None:
        response = await async_client.recommendations.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommendation = await response.parse()
        assert_matches_type(object, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncResalign) -> None:
        async with async_client.recommendations.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommendation = await response.parse()
            assert_matches_type(object, recommendation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh_batch(self, async_client: AsyncResalign) -> None:
        recommendation = await async_client.recommendations.refresh_batch()
        assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh_batch_with_all_params(self, async_client: AsyncResalign) -> None:
        recommendation = await async_client.recommendations.refresh_batch(
            report_id="report_id",
            tier="free",
            trigger="trigger",
            x_service_key="X-Service-Key",
        )
        assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh_batch(self, async_client: AsyncResalign) -> None:
        response = await async_client.recommendations.with_raw_response.refresh_batch()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recommendation = await response.parse()
        assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh_batch(self, async_client: AsyncResalign) -> None:
        async with async_client.recommendations.with_streaming_response.refresh_batch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recommendation = await response.parse()
            assert_matches_type(RecommendationRefreshBatchResponse, recommendation, path=["response"])

        assert cast(Any, response.is_closed) is True
