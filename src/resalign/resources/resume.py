# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import resume_upload_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.resume_list_response import ResumeListResponse
from ..types.resume_delete_response import ResumeDeleteResponse
from ..types.resume_upload_response import ResumeUploadResponse
from ..types.resume_retry_extraction_response import ResumeRetryExtractionResponse

__all__ = ["ResumeResource", "AsyncResumeResource"]


class ResumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return ResumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return ResumeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeListResponse:
        """
        Retrieve all resumes uploaded by the authenticated user, ordered by most recent.
        """
        return self._get(
            "/v1/resume/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeListResponse,
        )

    def delete(
        self,
        resume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeDeleteResponse:
        """Delete a resume file from storage and database.

        Removes both the stored file and
        its metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resume_id:
            raise ValueError(f"Expected a non-empty value for `resume_id` but received {resume_id!r}")
        return self._delete(
            path_template("/v1/resume/delete/{resume_id}", resume_id=resume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeDeleteResponse,
        )

    def download(
        self,
        resume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Securely download the resume file content from Supabase Storage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resume_id:
            raise ValueError(f"Expected a non-empty value for `resume_id` but received {resume_id!r}")
        return self._get(
            path_template("/v1/resume/download/{resume_id}", resume_id=resume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retry_extraction(
        self,
        resume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeRetryExtractionResponse:
        """
        Manually trigger re-extraction for a resume that failed or is missing extracted
        data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resume_id:
            raise ValueError(f"Expected a non-empty value for `resume_id` but received {resume_id!r}")
        return self._post(
            path_template("/v1/resume/retry-extraction/{resume_id}", resume_id=resume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeRetryExtractionResponse,
        )

    def upload(
        self,
        *,
        resume: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeUploadResponse:
        """Upload a resume to Supabase Storage with content-based deduplication.

        Supports
        PDF, DOCX, DOC, MD, MDX, and TXT formats. Extraction happens asynchronously in
        the background.

        Args:
          resume: Resume file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/resume/upload",
            body=maybe_transform({"resume": resume}, resume_upload_params.ResumeUploadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeUploadResponse,
        )


class AsyncResumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncResumeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeListResponse:
        """
        Retrieve all resumes uploaded by the authenticated user, ordered by most recent.
        """
        return await self._get(
            "/v1/resume/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeListResponse,
        )

    async def delete(
        self,
        resume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeDeleteResponse:
        """Delete a resume file from storage and database.

        Removes both the stored file and
        its metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resume_id:
            raise ValueError(f"Expected a non-empty value for `resume_id` but received {resume_id!r}")
        return await self._delete(
            path_template("/v1/resume/delete/{resume_id}", resume_id=resume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeDeleteResponse,
        )

    async def download(
        self,
        resume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Securely download the resume file content from Supabase Storage.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resume_id:
            raise ValueError(f"Expected a non-empty value for `resume_id` but received {resume_id!r}")
        return await self._get(
            path_template("/v1/resume/download/{resume_id}", resume_id=resume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retry_extraction(
        self,
        resume_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeRetryExtractionResponse:
        """
        Manually trigger re-extraction for a resume that failed or is missing extracted
        data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not resume_id:
            raise ValueError(f"Expected a non-empty value for `resume_id` but received {resume_id!r}")
        return await self._post(
            path_template("/v1/resume/retry-extraction/{resume_id}", resume_id=resume_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeRetryExtractionResponse,
        )

    async def upload(
        self,
        *,
        resume: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeUploadResponse:
        """Upload a resume to Supabase Storage with content-based deduplication.

        Supports
        PDF, DOCX, DOC, MD, MDX, and TXT formats. Extraction happens asynchronously in
        the background.

        Args:
          resume: Resume file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/resume/upload",
            body=await async_maybe_transform({"resume": resume}, resume_upload_params.ResumeUploadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeUploadResponse,
        )


class ResumeResourceWithRawResponse:
    def __init__(self, resume: ResumeResource) -> None:
        self._resume = resume

        self.list = to_raw_response_wrapper(
            resume.list,
        )
        self.delete = to_raw_response_wrapper(
            resume.delete,
        )
        self.download = to_raw_response_wrapper(
            resume.download,
        )
        self.retry_extraction = to_raw_response_wrapper(
            resume.retry_extraction,
        )
        self.upload = to_raw_response_wrapper(
            resume.upload,
        )


class AsyncResumeResourceWithRawResponse:
    def __init__(self, resume: AsyncResumeResource) -> None:
        self._resume = resume

        self.list = async_to_raw_response_wrapper(
            resume.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resume.delete,
        )
        self.download = async_to_raw_response_wrapper(
            resume.download,
        )
        self.retry_extraction = async_to_raw_response_wrapper(
            resume.retry_extraction,
        )
        self.upload = async_to_raw_response_wrapper(
            resume.upload,
        )


class ResumeResourceWithStreamingResponse:
    def __init__(self, resume: ResumeResource) -> None:
        self._resume = resume

        self.list = to_streamed_response_wrapper(
            resume.list,
        )
        self.delete = to_streamed_response_wrapper(
            resume.delete,
        )
        self.download = to_streamed_response_wrapper(
            resume.download,
        )
        self.retry_extraction = to_streamed_response_wrapper(
            resume.retry_extraction,
        )
        self.upload = to_streamed_response_wrapper(
            resume.upload,
        )


class AsyncResumeResourceWithStreamingResponse:
    def __init__(self, resume: AsyncResumeResource) -> None:
        self._resume = resume

        self.list = async_to_streamed_response_wrapper(
            resume.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resume.delete,
        )
        self.download = async_to_streamed_response_wrapper(
            resume.download,
        )
        self.retry_extraction = async_to_streamed_response_wrapper(
            resume.retry_extraction,
        )
        self.upload = async_to_streamed_response_wrapper(
            resume.upload,
        )
