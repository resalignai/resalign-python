# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import roadmap_generate_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.roadmap_generate_response import RoadmapGenerateResponse

__all__ = ["RoadmapsResource", "AsyncRoadmapsResource"]


class RoadmapsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoadmapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return RoadmapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoadmapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return RoadmapsResourceWithStreamingResponse(self)

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
        Retrieve all completed roadmaps for the authenticated user, sorted by newest
        first.
        """
        return self._get(
            "/v1/roadmaps/fetch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def generate(
        self,
        *,
        analysis_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoadmapGenerateResponse:
        """Generate a personalized career roadmap from a completed analysis.

        Produces
        stage-by-stage guidance on skill acquisition, resume optimization, interview
        prep, and application strategy.

        Args:
          analysis_id: The analysis ID (contains fit assessment and JD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/roadmaps/generate",
            body=maybe_transform({"analysis_id": analysis_id}, roadmap_generate_params.RoadmapGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoadmapGenerateResponse,
        )


class AsyncRoadmapsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoadmapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoadmapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoadmapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncRoadmapsResourceWithStreamingResponse(self)

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
        Retrieve all completed roadmaps for the authenticated user, sorted by newest
        first.
        """
        return await self._get(
            "/v1/roadmaps/fetch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def generate(
        self,
        *,
        analysis_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoadmapGenerateResponse:
        """Generate a personalized career roadmap from a completed analysis.

        Produces
        stage-by-stage guidance on skill acquisition, resume optimization, interview
        prep, and application strategy.

        Args:
          analysis_id: The analysis ID (contains fit assessment and JD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/roadmaps/generate",
            body=await async_maybe_transform(
                {"analysis_id": analysis_id}, roadmap_generate_params.RoadmapGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoadmapGenerateResponse,
        )


class RoadmapsResourceWithRawResponse:
    def __init__(self, roadmaps: RoadmapsResource) -> None:
        self._roadmaps = roadmaps

        self.list = to_raw_response_wrapper(
            roadmaps.list,
        )
        self.generate = to_raw_response_wrapper(
            roadmaps.generate,
        )


class AsyncRoadmapsResourceWithRawResponse:
    def __init__(self, roadmaps: AsyncRoadmapsResource) -> None:
        self._roadmaps = roadmaps

        self.list = async_to_raw_response_wrapper(
            roadmaps.list,
        )
        self.generate = async_to_raw_response_wrapper(
            roadmaps.generate,
        )


class RoadmapsResourceWithStreamingResponse:
    def __init__(self, roadmaps: RoadmapsResource) -> None:
        self._roadmaps = roadmaps

        self.list = to_streamed_response_wrapper(
            roadmaps.list,
        )
        self.generate = to_streamed_response_wrapper(
            roadmaps.generate,
        )


class AsyncRoadmapsResourceWithStreamingResponse:
    def __init__(self, roadmaps: AsyncRoadmapsResource) -> None:
        self._roadmaps = roadmaps

        self.list = async_to_streamed_response_wrapper(
            roadmaps.list,
        )
        self.generate = async_to_streamed_response_wrapper(
            roadmaps.generate,
        )
