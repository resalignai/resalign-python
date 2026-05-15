# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import (
    TaxonomyListRolesResponse,
    TaxonomySearchSkillsResponse,
    TaxonomyListFunctionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaxonomy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_functions(self, client: Resalign) -> None:
        taxonomy = client.taxonomy.list_functions()
        assert_matches_type(TaxonomyListFunctionsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_functions(self, client: Resalign) -> None:
        response = client.taxonomy.with_raw_response.list_functions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taxonomy = response.parse()
        assert_matches_type(TaxonomyListFunctionsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_functions(self, client: Resalign) -> None:
        with client.taxonomy.with_streaming_response.list_functions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taxonomy = response.parse()
            assert_matches_type(TaxonomyListFunctionsResponse, taxonomy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_roles(self, client: Resalign) -> None:
        taxonomy = client.taxonomy.list_roles(
            function="function",
        )
        assert_matches_type(TaxonomyListRolesResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_roles(self, client: Resalign) -> None:
        response = client.taxonomy.with_raw_response.list_roles(
            function="function",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taxonomy = response.parse()
        assert_matches_type(TaxonomyListRolesResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_roles(self, client: Resalign) -> None:
        with client.taxonomy.with_streaming_response.list_roles(
            function="function",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taxonomy = response.parse()
            assert_matches_type(TaxonomyListRolesResponse, taxonomy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_skills(self, client: Resalign) -> None:
        taxonomy = client.taxonomy.search_skills()
        assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_skills_with_all_params(self, client: Resalign) -> None:
        taxonomy = client.taxonomy.search_skills(
            limit=1,
            q="q",
        )
        assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_skills(self, client: Resalign) -> None:
        response = client.taxonomy.with_raw_response.search_skills()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taxonomy = response.parse()
        assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_skills(self, client: Resalign) -> None:
        with client.taxonomy.with_streaming_response.search_skills() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taxonomy = response.parse()
            assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTaxonomy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_functions(self, async_client: AsyncResalign) -> None:
        taxonomy = await async_client.taxonomy.list_functions()
        assert_matches_type(TaxonomyListFunctionsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_functions(self, async_client: AsyncResalign) -> None:
        response = await async_client.taxonomy.with_raw_response.list_functions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taxonomy = await response.parse()
        assert_matches_type(TaxonomyListFunctionsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_functions(self, async_client: AsyncResalign) -> None:
        async with async_client.taxonomy.with_streaming_response.list_functions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taxonomy = await response.parse()
            assert_matches_type(TaxonomyListFunctionsResponse, taxonomy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_roles(self, async_client: AsyncResalign) -> None:
        taxonomy = await async_client.taxonomy.list_roles(
            function="function",
        )
        assert_matches_type(TaxonomyListRolesResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_roles(self, async_client: AsyncResalign) -> None:
        response = await async_client.taxonomy.with_raw_response.list_roles(
            function="function",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taxonomy = await response.parse()
        assert_matches_type(TaxonomyListRolesResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_roles(self, async_client: AsyncResalign) -> None:
        async with async_client.taxonomy.with_streaming_response.list_roles(
            function="function",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taxonomy = await response.parse()
            assert_matches_type(TaxonomyListRolesResponse, taxonomy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_skills(self, async_client: AsyncResalign) -> None:
        taxonomy = await async_client.taxonomy.search_skills()
        assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_skills_with_all_params(self, async_client: AsyncResalign) -> None:
        taxonomy = await async_client.taxonomy.search_skills(
            limit=1,
            q="q",
        )
        assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_skills(self, async_client: AsyncResalign) -> None:
        response = await async_client.taxonomy.with_raw_response.search_skills()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        taxonomy = await response.parse()
        assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_skills(self, async_client: AsyncResalign) -> None:
        async with async_client.taxonomy.with_streaming_response.search_skills() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            taxonomy = await response.parse()
            assert_matches_type(TaxonomySearchSkillsResponse, taxonomy, path=["response"])

        assert cast(Any, response.is_closed) is True
