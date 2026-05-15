# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import FavoriteAddResponse, FavoriteListResponse, FavoriteDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFavorites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        favorite = client.favorites.list()
        assert_matches_type(FavoriteListResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.favorites.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = response.parse()
        assert_matches_type(FavoriteListResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.favorites.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = response.parse()
            assert_matches_type(FavoriteListResponse, favorite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Resalign) -> None:
        favorite = client.favorites.delete(
            "job_posting_id",
        )
        assert_matches_type(FavoriteDeleteResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Resalign) -> None:
        response = client.favorites.with_raw_response.delete(
            "job_posting_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = response.parse()
        assert_matches_type(FavoriteDeleteResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Resalign) -> None:
        with client.favorites.with_streaming_response.delete(
            "job_posting_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = response.parse()
            assert_matches_type(FavoriteDeleteResponse, favorite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_posting_id` but received ''"):
            client.favorites.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Resalign) -> None:
        favorite = client.favorites.add(
            "job_posting_id",
        )
        assert_matches_type(FavoriteAddResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Resalign) -> None:
        response = client.favorites.with_raw_response.add(
            "job_posting_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = response.parse()
        assert_matches_type(FavoriteAddResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Resalign) -> None:
        with client.favorites.with_streaming_response.add(
            "job_posting_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = response.parse()
            assert_matches_type(FavoriteAddResponse, favorite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_posting_id` but received ''"):
            client.favorites.with_raw_response.add(
                "",
            )


class TestAsyncFavorites:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        favorite = await async_client.favorites.list()
        assert_matches_type(FavoriteListResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.favorites.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = await response.parse()
        assert_matches_type(FavoriteListResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.favorites.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = await response.parse()
            assert_matches_type(FavoriteListResponse, favorite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncResalign) -> None:
        favorite = await async_client.favorites.delete(
            "job_posting_id",
        )
        assert_matches_type(FavoriteDeleteResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncResalign) -> None:
        response = await async_client.favorites.with_raw_response.delete(
            "job_posting_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = await response.parse()
        assert_matches_type(FavoriteDeleteResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncResalign) -> None:
        async with async_client.favorites.with_streaming_response.delete(
            "job_posting_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = await response.parse()
            assert_matches_type(FavoriteDeleteResponse, favorite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_posting_id` but received ''"):
            await async_client.favorites.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncResalign) -> None:
        favorite = await async_client.favorites.add(
            "job_posting_id",
        )
        assert_matches_type(FavoriteAddResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncResalign) -> None:
        response = await async_client.favorites.with_raw_response.add(
            "job_posting_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = await response.parse()
        assert_matches_type(FavoriteAddResponse, favorite, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncResalign) -> None:
        async with async_client.favorites.with_streaming_response.add(
            "job_posting_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = await response.parse()
            assert_matches_type(FavoriteAddResponse, favorite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_posting_id` but received ''"):
            await async_client.favorites.with_raw_response.add(
                "",
            )
