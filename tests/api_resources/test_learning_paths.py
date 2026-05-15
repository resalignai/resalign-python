# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLearningPaths:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Resalign) -> None:
        learning_path = client.learning_paths.retrieve(
            "path_id",
        )
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Resalign) -> None:
        response = client.learning_paths.with_raw_response.retrieve(
            "path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        learning_path = response.parse()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Resalign) -> None:
        with client.learning_paths.with_streaming_response.retrieve(
            "path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            learning_path = response.parse()
            assert_matches_type(object, learning_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.learning_paths.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        learning_path = client.learning_paths.list()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.learning_paths.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        learning_path = response.parse()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.learning_paths.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            learning_path = response.parse()
            assert_matches_type(object, learning_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enroll(self, client: Resalign) -> None:
        learning_path = client.learning_paths.enroll(
            alignment_id="alignment_id",
            skill="skill",
        )
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enroll(self, client: Resalign) -> None:
        response = client.learning_paths.with_raw_response.enroll(
            alignment_id="alignment_id",
            skill="skill",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        learning_path = response.parse()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enroll(self, client: Resalign) -> None:
        with client.learning_paths.with_streaming_response.enroll(
            alignment_id="alignment_id",
            skill="skill",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            learning_path = response.parse()
            assert_matches_type(object, learning_path, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLearningPaths:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncResalign) -> None:
        learning_path = await async_client.learning_paths.retrieve(
            "path_id",
        )
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.with_raw_response.retrieve(
            "path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        learning_path = await response.parse()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.with_streaming_response.retrieve(
            "path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            learning_path = await response.parse()
            assert_matches_type(object, learning_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.learning_paths.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        learning_path = await async_client.learning_paths.list()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        learning_path = await response.parse()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            learning_path = await response.parse()
            assert_matches_type(object, learning_path, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enroll(self, async_client: AsyncResalign) -> None:
        learning_path = await async_client.learning_paths.enroll(
            alignment_id="alignment_id",
            skill="skill",
        )
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enroll(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.with_raw_response.enroll(
            alignment_id="alignment_id",
            skill="skill",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        learning_path = await response.parse()
        assert_matches_type(object, learning_path, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enroll(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.with_streaming_response.enroll(
            alignment_id="alignment_id",
            skill="skill",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            learning_path = await response.parse()
            assert_matches_type(object, learning_path, path=["response"])

        assert cast(Any, response.is_closed) is True
