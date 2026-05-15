# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Resalign) -> None:
        module = client.learning_paths.modules.retrieve(
            module_id="module_id",
            path_id="path_id",
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Resalign) -> None:
        response = client.learning_paths.modules.with_raw_response.retrieve(
            module_id="module_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        module = response.parse()
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Resalign) -> None:
        with client.learning_paths.modules.with_streaming_response.retrieve(
            module_id="module_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            module = response.parse()
            assert_matches_type(object, module, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.learning_paths.modules.with_raw_response.retrieve(
                module_id="module_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `module_id` but received ''"):
            client.learning_paths.modules.with_raw_response.retrieve(
                module_id="",
                path_id="path_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_content(self, client: Resalign) -> None:
        module = client.learning_paths.modules.get_content(
            module_id="module_id",
            path_id="path_id",
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_content_with_all_params(self, client: Resalign) -> None:
        module = client.learning_paths.modules.get_content(
            module_id="module_id",
            path_id="path_id",
            generate=True,
            topic_index=0,
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_content(self, client: Resalign) -> None:
        response = client.learning_paths.modules.with_raw_response.get_content(
            module_id="module_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        module = response.parse()
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_content(self, client: Resalign) -> None:
        with client.learning_paths.modules.with_streaming_response.get_content(
            module_id="module_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            module = response.parse()
            assert_matches_type(object, module, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_content(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.learning_paths.modules.with_raw_response.get_content(
                module_id="module_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `module_id` but received ''"):
            client.learning_paths.modules.with_raw_response.get_content(
                module_id="",
                path_id="path_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_resources(self, client: Resalign) -> None:
        module = client.learning_paths.modules.get_resources(
            module_id="module_id",
            path_id="path_id",
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_resources_with_all_params(self, client: Resalign) -> None:
        module = client.learning_paths.modules.get_resources(
            module_id="module_id",
            path_id="path_id",
            curate=True,
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_resources(self, client: Resalign) -> None:
        response = client.learning_paths.modules.with_raw_response.get_resources(
            module_id="module_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        module = response.parse()
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_resources(self, client: Resalign) -> None:
        with client.learning_paths.modules.with_streaming_response.get_resources(
            module_id="module_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            module = response.parse()
            assert_matches_type(object, module, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_resources(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.learning_paths.modules.with_raw_response.get_resources(
                module_id="module_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `module_id` but received ''"):
            client.learning_paths.modules.with_raw_response.get_resources(
                module_id="",
                path_id="path_id",
            )


class TestAsyncModules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncResalign) -> None:
        module = await async_client.learning_paths.modules.retrieve(
            module_id="module_id",
            path_id="path_id",
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.modules.with_raw_response.retrieve(
            module_id="module_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        module = await response.parse()
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.modules.with_streaming_response.retrieve(
            module_id="module_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            module = await response.parse()
            assert_matches_type(object, module, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.learning_paths.modules.with_raw_response.retrieve(
                module_id="module_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `module_id` but received ''"):
            await async_client.learning_paths.modules.with_raw_response.retrieve(
                module_id="",
                path_id="path_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_content(self, async_client: AsyncResalign) -> None:
        module = await async_client.learning_paths.modules.get_content(
            module_id="module_id",
            path_id="path_id",
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_content_with_all_params(self, async_client: AsyncResalign) -> None:
        module = await async_client.learning_paths.modules.get_content(
            module_id="module_id",
            path_id="path_id",
            generate=True,
            topic_index=0,
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_content(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.modules.with_raw_response.get_content(
            module_id="module_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        module = await response.parse()
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_content(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.modules.with_streaming_response.get_content(
            module_id="module_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            module = await response.parse()
            assert_matches_type(object, module, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_content(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.learning_paths.modules.with_raw_response.get_content(
                module_id="module_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `module_id` but received ''"):
            await async_client.learning_paths.modules.with_raw_response.get_content(
                module_id="",
                path_id="path_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_resources(self, async_client: AsyncResalign) -> None:
        module = await async_client.learning_paths.modules.get_resources(
            module_id="module_id",
            path_id="path_id",
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_resources_with_all_params(self, async_client: AsyncResalign) -> None:
        module = await async_client.learning_paths.modules.get_resources(
            module_id="module_id",
            path_id="path_id",
            curate=True,
        )
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_resources(self, async_client: AsyncResalign) -> None:
        response = await async_client.learning_paths.modules.with_raw_response.get_resources(
            module_id="module_id",
            path_id="path_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        module = await response.parse()
        assert_matches_type(object, module, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_resources(self, async_client: AsyncResalign) -> None:
        async with async_client.learning_paths.modules.with_streaming_response.get_resources(
            module_id="module_id",
            path_id="path_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            module = await response.parse()
            assert_matches_type(object, module, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_resources(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.learning_paths.modules.with_raw_response.get_resources(
                module_id="module_id",
                path_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `module_id` but received ''"):
            await async_client.learning_paths.modules.with_raw_response.get_resources(
                module_id="",
                path_id="path_id",
            )
