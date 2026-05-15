# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import (
    ResumeListResponse,
    ResumeDeleteResponse,
    ResumeUploadResponse,
    ResumeRetryExtractionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResume:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Resalign) -> None:
        resume = client.resume.list()
        assert_matches_type(ResumeListResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Resalign) -> None:
        response = client.resume.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert_matches_type(ResumeListResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Resalign) -> None:
        with client.resume.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert_matches_type(ResumeListResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Resalign) -> None:
        resume = client.resume.delete(
            "resume_id",
        )
        assert_matches_type(ResumeDeleteResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Resalign) -> None:
        response = client.resume.with_raw_response.delete(
            "resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert_matches_type(ResumeDeleteResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Resalign) -> None:
        with client.resume.with_streaming_response.delete(
            "resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert_matches_type(ResumeDeleteResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resume_id` but received ''"):
            client.resume.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download(self, client: Resalign) -> None:
        resume = client.resume.download(
            "resume_id",
        )
        assert_matches_type(object, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: Resalign) -> None:
        response = client.resume.with_raw_response.download(
            "resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert_matches_type(object, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: Resalign) -> None:
        with client.resume.with_streaming_response.download(
            "resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert_matches_type(object, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_download(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resume_id` but received ''"):
            client.resume.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retry_extraction(self, client: Resalign) -> None:
        resume = client.resume.retry_extraction(
            "resume_id",
        )
        assert_matches_type(ResumeRetryExtractionResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retry_extraction(self, client: Resalign) -> None:
        response = client.resume.with_raw_response.retry_extraction(
            "resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert_matches_type(ResumeRetryExtractionResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retry_extraction(self, client: Resalign) -> None:
        with client.resume.with_streaming_response.retry_extraction(
            "resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert_matches_type(ResumeRetryExtractionResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retry_extraction(self, client: Resalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resume_id` but received ''"):
            client.resume.with_raw_response.retry_extraction(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Resalign) -> None:
        resume = client.resume.upload(
            resume="resume",
        )
        assert_matches_type(ResumeUploadResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Resalign) -> None:
        response = client.resume.with_raw_response.upload(
            resume="resume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert_matches_type(ResumeUploadResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Resalign) -> None:
        with client.resume.with_streaming_response.upload(
            resume="resume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert_matches_type(ResumeUploadResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResume:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncResalign) -> None:
        resume = await async_client.resume.list()
        assert_matches_type(ResumeListResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncResalign) -> None:
        response = await async_client.resume.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert_matches_type(ResumeListResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncResalign) -> None:
        async with async_client.resume.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert_matches_type(ResumeListResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncResalign) -> None:
        resume = await async_client.resume.delete(
            "resume_id",
        )
        assert_matches_type(ResumeDeleteResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncResalign) -> None:
        response = await async_client.resume.with_raw_response.delete(
            "resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert_matches_type(ResumeDeleteResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncResalign) -> None:
        async with async_client.resume.with_streaming_response.delete(
            "resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert_matches_type(ResumeDeleteResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resume_id` but received ''"):
            await async_client.resume.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncResalign) -> None:
        resume = await async_client.resume.download(
            "resume_id",
        )
        assert_matches_type(object, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncResalign) -> None:
        response = await async_client.resume.with_raw_response.download(
            "resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert_matches_type(object, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncResalign) -> None:
        async with async_client.resume.with_streaming_response.download(
            "resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert_matches_type(object, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resume_id` but received ''"):
            await async_client.resume.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retry_extraction(self, async_client: AsyncResalign) -> None:
        resume = await async_client.resume.retry_extraction(
            "resume_id",
        )
        assert_matches_type(ResumeRetryExtractionResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retry_extraction(self, async_client: AsyncResalign) -> None:
        response = await async_client.resume.with_raw_response.retry_extraction(
            "resume_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert_matches_type(ResumeRetryExtractionResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retry_extraction(self, async_client: AsyncResalign) -> None:
        async with async_client.resume.with_streaming_response.retry_extraction(
            "resume_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert_matches_type(ResumeRetryExtractionResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retry_extraction(self, async_client: AsyncResalign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resume_id` but received ''"):
            await async_client.resume.with_raw_response.retry_extraction(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncResalign) -> None:
        resume = await async_client.resume.upload(
            resume="resume",
        )
        assert_matches_type(ResumeUploadResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncResalign) -> None:
        response = await async_client.resume.with_raw_response.upload(
            resume="resume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert_matches_type(ResumeUploadResponse, resume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncResalign) -> None:
        async with async_client.resume.with_streaming_response.upload(
            resume="resume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert_matches_type(ResumeUploadResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True
