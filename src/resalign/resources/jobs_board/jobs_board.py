# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .fetch import (
    FetchResource,
    AsyncFetchResource,
    FetchResourceWithRawResponse,
    AsyncFetchResourceWithRawResponse,
    FetchResourceWithStreamingResponse,
    AsyncFetchResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.jobs_board_refresh_response import JobsBoardRefreshResponse

__all__ = ["JobsBoardResource", "AsyncJobsBoardResource"]


class JobsBoardResource(SyncAPIResource):
    @cached_property
    def fetch(self) -> FetchResource:
        return FetchResource(self._client)

    @cached_property
    def with_raw_response(self) -> JobsBoardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return JobsBoardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsBoardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return JobsBoardResourceWithStreamingResponse(self)

    def refresh(
        self,
        *,
        x_service_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobsBoardRefreshResponse:
        """Trigger asynchronous synchronization of job postings from all ATS sources.

        This
        endpoint returns 202 Accepted immediately and processes sync in background.
        Protected endpoint requiring valid service key. Returns report_id for tracking
        the sync operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Service-Key": x_service_key}), **(extra_headers or {})}
        return self._post(
            "/v1/jobs_board/refresh_jobs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobsBoardRefreshResponse,
        )


class AsyncJobsBoardResource(AsyncAPIResource):
    @cached_property
    def fetch(self) -> AsyncFetchResource:
        return AsyncFetchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsBoardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsBoardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsBoardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return AsyncJobsBoardResourceWithStreamingResponse(self)

    async def refresh(
        self,
        *,
        x_service_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobsBoardRefreshResponse:
        """Trigger asynchronous synchronization of job postings from all ATS sources.

        This
        endpoint returns 202 Accepted immediately and processes sync in background.
        Protected endpoint requiring valid service key. Returns report_id for tracking
        the sync operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Service-Key": x_service_key}), **(extra_headers or {})}
        return await self._post(
            "/v1/jobs_board/refresh_jobs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobsBoardRefreshResponse,
        )


class JobsBoardResourceWithRawResponse:
    def __init__(self, jobs_board: JobsBoardResource) -> None:
        self._jobs_board = jobs_board

        self.refresh = to_raw_response_wrapper(
            jobs_board.refresh,
        )

    @cached_property
    def fetch(self) -> FetchResourceWithRawResponse:
        return FetchResourceWithRawResponse(self._jobs_board.fetch)


class AsyncJobsBoardResourceWithRawResponse:
    def __init__(self, jobs_board: AsyncJobsBoardResource) -> None:
        self._jobs_board = jobs_board

        self.refresh = async_to_raw_response_wrapper(
            jobs_board.refresh,
        )

    @cached_property
    def fetch(self) -> AsyncFetchResourceWithRawResponse:
        return AsyncFetchResourceWithRawResponse(self._jobs_board.fetch)


class JobsBoardResourceWithStreamingResponse:
    def __init__(self, jobs_board: JobsBoardResource) -> None:
        self._jobs_board = jobs_board

        self.refresh = to_streamed_response_wrapper(
            jobs_board.refresh,
        )

    @cached_property
    def fetch(self) -> FetchResourceWithStreamingResponse:
        return FetchResourceWithStreamingResponse(self._jobs_board.fetch)


class AsyncJobsBoardResourceWithStreamingResponse:
    def __init__(self, jobs_board: AsyncJobsBoardResource) -> None:
        self._jobs_board = jobs_board

        self.refresh = async_to_streamed_response_wrapper(
            jobs_board.refresh,
        )

    @cached_property
    def fetch(self) -> AsyncFetchResourceWithStreamingResponse:
        return AsyncFetchResourceWithStreamingResponse(self._jobs_board.fetch)
