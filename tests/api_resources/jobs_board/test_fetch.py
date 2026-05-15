# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types.jobs_board import JobPosting, FetchListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFetch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Resalign) -> None:
        fetch = client.jobs_board.fetch.retrieve(
            "job_id",
        )
        assert_matches_type(JobPosting, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Resalign) -> None:
        response = client.jobs_board.fetch.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = response.parse()
        assert_matches_type(JobPosting, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Resalign) -> None:
        with client.jobs_board.fetch.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = response.parse()
            assert_matches_type(JobPosting, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs_board.fetch.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        fetch = client.jobs_board.fetch.list()
        assert_matches_type(FetchListResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Resalign) -> None:
        fetch = client.jobs_board.fetch.list(
            company_size="company_size",
            department="department",
            employment_type="employment_type",
            location_type="location_type",
            organization_type="organization_type",
            page=1,
            page_size=1,
            salary_max=0,
            salary_min=0,
            search="search",
            sort_by="newest",
        )
        assert_matches_type(FetchListResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.jobs_board.fetch.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = response.parse()
        assert_matches_type(FetchListResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.jobs_board.fetch.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = response.parse()
            assert_matches_type(FetchListResponse, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFetch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncResalign) -> None:
        fetch = await async_client.jobs_board.fetch.retrieve(
            "job_id",
        )
        assert_matches_type(JobPosting, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncResalign) -> None:
        response = await async_client.jobs_board.fetch.with_raw_response.retrieve(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = await response.parse()
        assert_matches_type(JobPosting, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncResalign) -> None:
        async with async_client.jobs_board.fetch.with_streaming_response.retrieve(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = await response.parse()
            assert_matches_type(JobPosting, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs_board.fetch.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        fetch = await async_client.jobs_board.fetch.list()
        assert_matches_type(FetchListResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncResalign) -> None:
        fetch = await async_client.jobs_board.fetch.list(
            company_size="company_size",
            department="department",
            employment_type="employment_type",
            location_type="location_type",
            organization_type="organization_type",
            page=1,
            page_size=1,
            salary_max=0,
            salary_min=0,
            search="search",
            sort_by="newest",
        )
        assert_matches_type(FetchListResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.jobs_board.fetch.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fetch = await response.parse()
        assert_matches_type(FetchListResponse, fetch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.jobs_board.fetch.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fetch = await response.parse()
            assert_matches_type(FetchListResponse, fetch, path=["response"])

        assert cast(Any, response.is_closed) is True
