# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.alignments import start_create_params, start_create_with_streaming_params

__all__ = ["StartResource", "AsyncStartResource"]


class StartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return StartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return StartResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        analysis_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Create a new career alignment from a completed analysis.

        Generates a
        personalized skill-gap roadmap and triggers background resource curation.

        Args:
          analysis_id: ID of a completed analysis to build roadmap from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alignments/start",
            body=maybe_transform({"analysis_id": analysis_id}, start_create_params.StartCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_with_streaming(
        self,
        *,
        analysis_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a new alignment and generate a roadmap with real-time progress via SSE.
        Streams progress events: creating_record, generating_roadmap, roadmap_complete,
        done.

        Args:
          analysis_id: ID of a completed analysis to build roadmap from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alignments/start/stream",
            body=maybe_transform(
                {"analysis_id": analysis_id}, start_create_with_streaming_params.StartCreateWithStreamingParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncStartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncStartResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        analysis_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Create a new career alignment from a completed analysis.

        Generates a
        personalized skill-gap roadmap and triggers background resource curation.

        Args:
          analysis_id: ID of a completed analysis to build roadmap from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alignments/start",
            body=await async_maybe_transform({"analysis_id": analysis_id}, start_create_params.StartCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_with_streaming(
        self,
        *,
        analysis_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Create a new alignment and generate a roadmap with real-time progress via SSE.
        Streams progress events: creating_record, generating_roadmap, roadmap_complete,
        done.

        Args:
          analysis_id: ID of a completed analysis to build roadmap from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alignments/start/stream",
            body=await async_maybe_transform(
                {"analysis_id": analysis_id}, start_create_with_streaming_params.StartCreateWithStreamingParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class StartResourceWithRawResponse:
    def __init__(self, start: StartResource) -> None:
        self._start = start

        self.create = to_raw_response_wrapper(
            start.create,
        )
        self.create_with_streaming = to_raw_response_wrapper(
            start.create_with_streaming,
        )


class AsyncStartResourceWithRawResponse:
    def __init__(self, start: AsyncStartResource) -> None:
        self._start = start

        self.create = async_to_raw_response_wrapper(
            start.create,
        )
        self.create_with_streaming = async_to_raw_response_wrapper(
            start.create_with_streaming,
        )


class StartResourceWithStreamingResponse:
    def __init__(self, start: StartResource) -> None:
        self._start = start

        self.create = to_streamed_response_wrapper(
            start.create,
        )
        self.create_with_streaming = to_streamed_response_wrapper(
            start.create_with_streaming,
        )


class AsyncStartResourceWithStreamingResponse:
    def __init__(self, start: AsyncStartResource) -> None:
        self._start = start

        self.create = async_to_streamed_response_wrapper(
            start.create,
        )
        self.create_with_streaming = async_to_streamed_response_wrapper(
            start.create_with_streaming,
        )
