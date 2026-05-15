# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import analysis_run_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.analysis_run_response import AnalysisRunResponse
from ..types.analysis_get_quota_response import AnalysisGetQuotaResponse

__all__ = ["AnalysisResource", "AsyncAnalysisResource"]


class AnalysisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AnalysisResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve all completed analyses for the authenticated user, sorted by completion
        date.
        """
        return self._get(
            "/v1/analysis/fetch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_quota(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisGetQuotaResponse:
        """
        Returns the current user's assessment usage and remaining quota for the billing
        period.
        """
        return self._get(
            "/v1/analysis/quota",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisGetQuotaResponse,
        )

    def run(
        self,
        *,
        jd_id: str,
        resume_id: str,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisRunResponse:
        """
        Analyze a resume against a job description to produce fit scoring, skill gap
        analysis, and category-weighted assessments. Supports both synchronous JSON and
        SSE streaming modes.

        Args:
          jd_id: Job ID from jobs_board table

          resume_id: Resume file_id from resumes table

          stream: Return SSE stream instead of JSON

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/analysis/run",
            body=maybe_transform(
                {
                    "jd_id": jd_id,
                    "resume_id": resume_id,
                },
                analysis_run_params.AnalysisRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, analysis_run_params.AnalysisRunParams),
            ),
            cast_to=AnalysisRunResponse,
        )


class AsyncAnalysisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalysisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncAnalysisResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve all completed analyses for the authenticated user, sorted by completion
        date.
        """
        return await self._get(
            "/v1/analysis/fetch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_quota(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisGetQuotaResponse:
        """
        Returns the current user's assessment usage and remaining quota for the billing
        period.
        """
        return await self._get(
            "/v1/analysis/quota",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisGetQuotaResponse,
        )

    async def run(
        self,
        *,
        jd_id: str,
        resume_id: str,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisRunResponse:
        """
        Analyze a resume against a job description to produce fit scoring, skill gap
        analysis, and category-weighted assessments. Supports both synchronous JSON and
        SSE streaming modes.

        Args:
          jd_id: Job ID from jobs_board table

          resume_id: Resume file_id from resumes table

          stream: Return SSE stream instead of JSON

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/analysis/run",
            body=await async_maybe_transform(
                {
                    "jd_id": jd_id,
                    "resume_id": resume_id,
                },
                analysis_run_params.AnalysisRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"stream": stream}, analysis_run_params.AnalysisRunParams),
            ),
            cast_to=AnalysisRunResponse,
        )


class AnalysisResourceWithRawResponse:
    def __init__(self, analysis: AnalysisResource) -> None:
        self._analysis = analysis

        self.list = to_raw_response_wrapper(
            analysis.list,
        )
        self.get_quota = to_raw_response_wrapper(
            analysis.get_quota,
        )
        self.run = to_raw_response_wrapper(
            analysis.run,
        )


class AsyncAnalysisResourceWithRawResponse:
    def __init__(self, analysis: AsyncAnalysisResource) -> None:
        self._analysis = analysis

        self.list = async_to_raw_response_wrapper(
            analysis.list,
        )
        self.get_quota = async_to_raw_response_wrapper(
            analysis.get_quota,
        )
        self.run = async_to_raw_response_wrapper(
            analysis.run,
        )


class AnalysisResourceWithStreamingResponse:
    def __init__(self, analysis: AnalysisResource) -> None:
        self._analysis = analysis

        self.list = to_streamed_response_wrapper(
            analysis.list,
        )
        self.get_quota = to_streamed_response_wrapper(
            analysis.get_quota,
        )
        self.run = to_streamed_response_wrapper(
            analysis.run,
        )


class AsyncAnalysisResourceWithStreamingResponse:
    def __init__(self, analysis: AsyncAnalysisResource) -> None:
        self._analysis = analysis

        self.list = async_to_streamed_response_wrapper(
            analysis.list,
        )
        self.get_quota = async_to_streamed_response_wrapper(
            analysis.get_quota,
        )
        self.run = async_to_streamed_response_wrapper(
            analysis.run,
        )
