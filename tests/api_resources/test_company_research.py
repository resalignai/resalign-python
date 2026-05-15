# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import (
    CompanyResearchEnrichResponse,
    CompanyResearchResultResponse,
    CompanyResearchRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanyResearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Resalign) -> None:
        company_research = client.company_research.retrieve(
            "identifier",
        )
        assert_matches_type(CompanyResearchRetrieveResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Resalign) -> None:
        response = client.company_research.with_raw_response.retrieve(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = response.parse()
        assert_matches_type(CompanyResearchRetrieveResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Resalign) -> None:
        with client.company_research.with_streaming_response.retrieve(
            "identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = response.parse()
            assert_matches_type(CompanyResearchRetrieveResponse, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.company_research.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enrich(self, client: Resalign) -> None:
        company_research = client.company_research.enrich()
        assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enrich_with_all_params(self, client: Resalign) -> None:
        company_research = client.company_research.enrich(
            concurrency=1,
            limit=1,
            stale_days=1,
            x_service_key="X-Service-Key",
        )
        assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enrich(self, client: Resalign) -> None:
        response = client.company_research.with_raw_response.enrich()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = response.parse()
        assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enrich(self, client: Resalign) -> None:
        with client.company_research.with_streaming_response.enrich() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = response.parse()
            assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_result(self, client: Resalign) -> None:
        company_research = client.company_research.result(
            "identifier",
        )
        assert_matches_type(CompanyResearchResultResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_result(self, client: Resalign) -> None:
        response = client.company_research.with_raw_response.result(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = response.parse()
        assert_matches_type(CompanyResearchResultResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_result(self, client: Resalign) -> None:
        with client.company_research.with_streaming_response.result(
            "identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = response.parse()
            assert_matches_type(CompanyResearchResultResponse, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_result(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.company_research.with_raw_response.result(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Resalign) -> None:
        company_research = client.company_research.run(
            company_name="x",
        )
        assert_matches_type(object, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Resalign) -> None:
        company_research = client.company_research.run(
            company_name="x",
            stream=True,
            company_directory_id="company_directory_id",
            linkedin_url="linkedin_url",
            website_url="website_url",
        )
        assert_matches_type(object, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Resalign) -> None:
        response = client.company_research.with_raw_response.run(
            company_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = response.parse()
        assert_matches_type(object, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Resalign) -> None:
        with client.company_research.with_streaming_response.run(
            company_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = response.parse()
            assert_matches_type(object, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompanyResearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncResalign) -> None:
        company_research = await async_client.company_research.retrieve(
            "identifier",
        )
        assert_matches_type(CompanyResearchRetrieveResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncResalign) -> None:
        response = await async_client.company_research.with_raw_response.retrieve(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = await response.parse()
        assert_matches_type(CompanyResearchRetrieveResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncResalign) -> None:
        async with async_client.company_research.with_streaming_response.retrieve(
            "identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = await response.parse()
            assert_matches_type(CompanyResearchRetrieveResponse, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.company_research.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enrich(self, async_client: AsyncResalign) -> None:
        company_research = await async_client.company_research.enrich()
        assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enrich_with_all_params(self, async_client: AsyncResalign) -> None:
        company_research = await async_client.company_research.enrich(
            concurrency=1,
            limit=1,
            stale_days=1,
            x_service_key="X-Service-Key",
        )
        assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enrich(self, async_client: AsyncResalign) -> None:
        response = await async_client.company_research.with_raw_response.enrich()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = await response.parse()
        assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enrich(self, async_client: AsyncResalign) -> None:
        async with async_client.company_research.with_streaming_response.enrich() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = await response.parse()
            assert_matches_type(CompanyResearchEnrichResponse, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_result(self, async_client: AsyncResalign) -> None:
        company_research = await async_client.company_research.result(
            "identifier",
        )
        assert_matches_type(CompanyResearchResultResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_result(self, async_client: AsyncResalign) -> None:
        response = await async_client.company_research.with_raw_response.result(
            "identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = await response.parse()
        assert_matches_type(CompanyResearchResultResponse, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_result(self, async_client: AsyncResalign) -> None:
        async with async_client.company_research.with_streaming_response.result(
            "identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = await response.parse()
            assert_matches_type(CompanyResearchResultResponse, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_result(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.company_research.with_raw_response.result(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncResalign) -> None:
        company_research = await async_client.company_research.run(
            company_name="x",
        )
        assert_matches_type(object, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncResalign) -> None:
        company_research = await async_client.company_research.run(
            company_name="x",
            stream=True,
            company_directory_id="company_directory_id",
            linkedin_url="linkedin_url",
            website_url="website_url",
        )
        assert_matches_type(object, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncResalign) -> None:
        response = await async_client.company_research.with_raw_response.run(
            company_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company_research = await response.parse()
        assert_matches_type(object, company_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncResalign) -> None:
        async with async_client.company_research.with_streaming_response.run(
            company_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company_research = await response.parse()
            assert_matches_type(object, company_research, path=["response"])

        assert cast(Any, response.is_closed) is True
