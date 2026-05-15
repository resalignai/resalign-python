# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .start import (
    StartResource,
    AsyncStartResource,
    StartResourceWithRawResponse,
    AsyncStartResourceWithRawResponse,
    StartResourceWithStreamingResponse,
    AsyncStartResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["AlignmentsResource", "AsyncAlignmentsResource"]


class AlignmentsResource(SyncAPIResource):
    @cached_property
    def start(self) -> StartResource:
        return StartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AlignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return AlignmentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        alignment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve a specific alignment with its roadmap, linked analysis data, and job
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alignment_id:
            raise ValueError(f"Expected a non-empty value for `alignment_id` but received {alignment_id!r}")
        return self._get(
            path_template("/v1/alignments/{alignment_id}", alignment_id=alignment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

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
        List all career alignment roadmaps for the authenticated user with linked
        analysis and job data.
        """
        return self._get(
            "/v1/alignments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_resources_status(
        self,
        alignment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Poll the status and results of background learning resource curation for an
        alignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alignment_id:
            raise ValueError(f"Expected a non-empty value for `alignment_id` but received {alignment_id!r}")
        return self._get(
            path_template("/v1/alignments/{alignment_id}/resources", alignment_id=alignment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAlignmentsResource(AsyncAPIResource):
    @cached_property
    def start(self) -> AsyncStartResource:
        return AsyncStartResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return AsyncAlignmentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        alignment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Retrieve a specific alignment with its roadmap, linked analysis data, and job
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alignment_id:
            raise ValueError(f"Expected a non-empty value for `alignment_id` but received {alignment_id!r}")
        return await self._get(
            path_template("/v1/alignments/{alignment_id}", alignment_id=alignment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

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
        List all career alignment roadmaps for the authenticated user with linked
        analysis and job data.
        """
        return await self._get(
            "/v1/alignments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_resources_status(
        self,
        alignment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Poll the status and results of background learning resource curation for an
        alignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alignment_id:
            raise ValueError(f"Expected a non-empty value for `alignment_id` but received {alignment_id!r}")
        return await self._get(
            path_template("/v1/alignments/{alignment_id}/resources", alignment_id=alignment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AlignmentsResourceWithRawResponse:
    def __init__(self, alignments: AlignmentsResource) -> None:
        self._alignments = alignments

        self.retrieve = to_raw_response_wrapper(
            alignments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            alignments.list,
        )
        self.get_resources_status = to_raw_response_wrapper(
            alignments.get_resources_status,
        )

    @cached_property
    def start(self) -> StartResourceWithRawResponse:
        return StartResourceWithRawResponse(self._alignments.start)


class AsyncAlignmentsResourceWithRawResponse:
    def __init__(self, alignments: AsyncAlignmentsResource) -> None:
        self._alignments = alignments

        self.retrieve = async_to_raw_response_wrapper(
            alignments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            alignments.list,
        )
        self.get_resources_status = async_to_raw_response_wrapper(
            alignments.get_resources_status,
        )

    @cached_property
    def start(self) -> AsyncStartResourceWithRawResponse:
        return AsyncStartResourceWithRawResponse(self._alignments.start)


class AlignmentsResourceWithStreamingResponse:
    def __init__(self, alignments: AlignmentsResource) -> None:
        self._alignments = alignments

        self.retrieve = to_streamed_response_wrapper(
            alignments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            alignments.list,
        )
        self.get_resources_status = to_streamed_response_wrapper(
            alignments.get_resources_status,
        )

    @cached_property
    def start(self) -> StartResourceWithStreamingResponse:
        return StartResourceWithStreamingResponse(self._alignments.start)


class AsyncAlignmentsResourceWithStreamingResponse:
    def __init__(self, alignments: AsyncAlignmentsResource) -> None:
        self._alignments = alignments

        self.retrieve = async_to_streamed_response_wrapper(
            alignments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            alignments.list,
        )
        self.get_resources_status = async_to_streamed_response_wrapper(
            alignments.get_resources_status,
        )

    @cached_property
    def start(self) -> AsyncStartResourceWithStreamingResponse:
        return AsyncStartResourceWithStreamingResponse(self._alignments.start)
