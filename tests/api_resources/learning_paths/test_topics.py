# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete(self, client: Resalign) -> None:
        topic = client.learning_paths.topics.complete(
            topic_id="topic_id",
            path_id="path_id",
        )
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: Resalign) -> None:
        response = client.learning_paths.topics.with_raw_response.complete(
            topic_id="topic_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: Resalign) -> None:
        with client.learning_paths.topics.with_streaming_response.complete(
            topic_id="topic_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(object, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.learning_paths.topics.with_raw_response.complete(
                topic_id="topic_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.learning_paths.topics.with_raw_response.complete(
                topic_id="",
                path_id="path_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_uncomplete(self, client: Resalign) -> None:
        topic = client.learning_paths.topics.uncomplete(
            topic_id="topic_id",
            path_id="path_id",
        )
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_uncomplete(self, client: Resalign) -> None:
        response = client.learning_paths.topics.with_raw_response.uncomplete(
            topic_id="topic_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_uncomplete(self, client: Resalign) -> None:
        with client.learning_paths.topics.with_streaming_response.uncomplete(
            topic_id="topic_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(object, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_uncomplete(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.learning_paths.topics.with_raw_response.uncomplete(
                topic_id="topic_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.learning_paths.topics.with_raw_response.uncomplete(
                topic_id="",
                path_id="path_id",
            )


class TestAsyncTopics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncResalign) -> None:
        topic = await async_client.learning_paths.topics.complete(
            topic_id="topic_id",
            path_id="path_id",
        )
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.topics.with_raw_response.complete(
            topic_id="topic_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.topics.with_streaming_response.complete(
            topic_id="topic_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(object, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.learning_paths.topics.with_raw_response.complete(
                topic_id="topic_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.learning_paths.topics.with_raw_response.complete(
                topic_id="",
                path_id="path_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_uncomplete(self, async_client: AsyncResalign) -> None:
        topic = await async_client.learning_paths.topics.uncomplete(
            topic_id="topic_id",
            path_id="path_id",
        )
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_uncomplete(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.topics.with_raw_response.uncomplete(
            topic_id="topic_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(object, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_uncomplete(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.topics.with_streaming_response.uncomplete(
            topic_id="topic_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(object, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_uncomplete(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.learning_paths.topics.with_raw_response.uncomplete(
                topic_id="topic_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.learning_paths.topics.with_raw_response.uncomplete(
                topic_id="",
                path_id="path_id",
            )
