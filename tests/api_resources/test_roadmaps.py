# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import RoadmapGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoadmaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        roadmap = client.roadmaps.list()
        assert_matches_type(object, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.roadmaps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        roadmap = response.parse()
        assert_matches_type(object, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.roadmaps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            roadmap = response.parse()
            assert_matches_type(object, roadmap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: Resalign) -> None:
        roadmap = client.roadmaps.generate(
            analysis_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(RoadmapGenerateResponse, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: Resalign) -> None:
        response = client.roadmaps.with_raw_response.generate(
            analysis_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        roadmap = response.parse()
        assert_matches_type(RoadmapGenerateResponse, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: Resalign) -> None:
        with client.roadmaps.with_streaming_response.generate(
            analysis_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            roadmap = response.parse()
            assert_matches_type(RoadmapGenerateResponse, roadmap, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoadmaps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        roadmap = await async_client.roadmaps.list()
        assert_matches_type(object, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.roadmaps.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        roadmap = await response.parse()
        assert_matches_type(object, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.roadmaps.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            roadmap = await response.parse()
            assert_matches_type(object, roadmap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncResalign) -> None:
        roadmap = await async_client.roadmaps.generate(
            analysis_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(RoadmapGenerateResponse, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncResalign) -> None:
        response = await async_client.roadmaps.with_raw_response.generate(
            analysis_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        roadmap = await response.parse()
        assert_matches_type(RoadmapGenerateResponse, roadmap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncResalign) -> None:
        async with async_client.roadmaps.with_streaming_response.generate(
            analysis_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            roadmap = await response.parse()
            assert_matches_type(RoadmapGenerateResponse, roadmap, path=["response"])

        assert cast(Any, response.is_closed) is True
