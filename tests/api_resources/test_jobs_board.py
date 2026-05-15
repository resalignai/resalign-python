# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import JobsBoardRefreshResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobsBoard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh(self, client: Resalign) -> None:
        jobs_board = client.jobs_board.refresh()
        assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh_with_all_params(self, client: Resalign) -> None:
        jobs_board = client.jobs_board.refresh(
            x_service_key="X-Service-Key",
        )
        assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh(self, client: Resalign) -> None:
        response = client.jobs_board.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jobs_board = response.parse()
        assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh(self, client: Resalign) -> None:
        with client.jobs_board.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jobs_board = response.parse()
            assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobsBoard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh(self, async_client: AsyncResalign) -> None:
        jobs_board = await async_client.jobs_board.refresh()
        assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh_with_all_params(self, async_client: AsyncResalign) -> None:
        jobs_board = await async_client.jobs_board.refresh(
            x_service_key="X-Service-Key",
        )
        assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncResalign) -> None:
        response = await async_client.jobs_board.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jobs_board = await response.parse()
        assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncResalign) -> None:
        async with async_client.jobs_board.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jobs_board = await response.parse()
            assert_matches_type(JobsBoardRefreshResponse, jobs_board, path=["response"])

        assert cast(Any, response.is_closed) is True
