# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .topics import (
    TopicsResource,
    AsyncTopicsResource,
    TopicsResourceWithRawResponse,
    AsyncTopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
    AsyncTopicsResourceWithStreamingResponse,
)
from ...types import learning_path_enroll_params
from .modules import (
    ModulesResource,
    AsyncModulesResource,
    ModulesResourceWithRawResponse,
    AsyncModulesResourceWithRawResponse,
    ModulesResourceWithStreamingResponse,
    AsyncModulesResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["LearningPathsResource", "AsyncLearningPathsResource"]


class LearningPathsResource(SyncAPIResource):
    @cached_property
    def modules(self) -> ModulesResource:
        return ModulesResource(self._client)

    @cached_property
    def topics(self) -> TopicsResource:
        return TopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LearningPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return LearningPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LearningPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return LearningPathsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        path_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get detailed information about a learning path including modules.

        Returns: Learning path with module summaries and progress

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._get(
            path_template("/v1/learning-paths/{path_id}", path_id=path_id),
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
        Get all enrolled learning paths for the authenticated user.

        Returns: List of learning path summaries with job context
        """
        return self._get(
            "/v1/learning-paths",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def enroll(
        self,
        *,
        alignment_id: str,
        skill: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Enroll in a learning path from an alignment's roadmap.

        Creates:

        - Learning path record
        - Module records for each module in the skill's learning path
        - Topic records for each topic in each module

        Args: request: Contains alignment_id and skill name

        Returns: Created learning path with modules

        Args:
          alignment_id: Alignment ID to enroll from

          skill: Skill name to enroll in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/learning-paths/enroll",
            body=maybe_transform(
                {
                    "alignment_id": alignment_id,
                    "skill": skill,
                },
                learning_path_enroll_params.LearningPathEnrollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncLearningPathsResource(AsyncAPIResource):
    @cached_property
    def modules(self) -> AsyncModulesResource:
        return AsyncModulesResource(self._client)

    @cached_property
    def topics(self) -> AsyncTopicsResource:
        return AsyncTopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLearningPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLearningPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLearningPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return AsyncLearningPathsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        path_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get detailed information about a learning path including modules.

        Returns: Learning path with module summaries and progress

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._get(
            path_template("/v1/learning-paths/{path_id}", path_id=path_id),
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
        Get all enrolled learning paths for the authenticated user.

        Returns: List of learning path summaries with job context
        """
        return await self._get(
            "/v1/learning-paths",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def enroll(
        self,
        *,
        alignment_id: str,
        skill: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Enroll in a learning path from an alignment's roadmap.

        Creates:

        - Learning path record
        - Module records for each module in the skill's learning path
        - Topic records for each topic in each module

        Args: request: Contains alignment_id and skill name

        Returns: Created learning path with modules

        Args:
          alignment_id: Alignment ID to enroll from

          skill: Skill name to enroll in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/learning-paths/enroll",
            body=await async_maybe_transform(
                {
                    "alignment_id": alignment_id,
                    "skill": skill,
                },
                learning_path_enroll_params.LearningPathEnrollParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class LearningPathsResourceWithRawResponse:
    def __init__(self, learning_paths: LearningPathsResource) -> None:
        self._learning_paths = learning_paths

        self.retrieve = to_raw_response_wrapper(
            learning_paths.retrieve,
        )
        self.list = to_raw_response_wrapper(
            learning_paths.list,
        )
        self.enroll = to_raw_response_wrapper(
            learning_paths.enroll,
        )

    @cached_property
    def modules(self) -> ModulesResourceWithRawResponse:
        return ModulesResourceWithRawResponse(self._learning_paths.modules)

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        return TopicsResourceWithRawResponse(self._learning_paths.topics)


class AsyncLearningPathsResourceWithRawResponse:
    def __init__(self, learning_paths: AsyncLearningPathsResource) -> None:
        self._learning_paths = learning_paths

        self.retrieve = async_to_raw_response_wrapper(
            learning_paths.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            learning_paths.list,
        )
        self.enroll = async_to_raw_response_wrapper(
            learning_paths.enroll,
        )

    @cached_property
    def modules(self) -> AsyncModulesResourceWithRawResponse:
        return AsyncModulesResourceWithRawResponse(self._learning_paths.modules)

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        return AsyncTopicsResourceWithRawResponse(self._learning_paths.topics)


class LearningPathsResourceWithStreamingResponse:
    def __init__(self, learning_paths: LearningPathsResource) -> None:
        self._learning_paths = learning_paths

        self.retrieve = to_streamed_response_wrapper(
            learning_paths.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            learning_paths.list,
        )
        self.enroll = to_streamed_response_wrapper(
            learning_paths.enroll,
        )

    @cached_property
    def modules(self) -> ModulesResourceWithStreamingResponse:
        return ModulesResourceWithStreamingResponse(self._learning_paths.modules)

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        return TopicsResourceWithStreamingResponse(self._learning_paths.topics)


class AsyncLearningPathsResourceWithStreamingResponse:
    def __init__(self, learning_paths: AsyncLearningPathsResource) -> None:
        self._learning_paths = learning_paths

        self.retrieve = async_to_streamed_response_wrapper(
            learning_paths.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            learning_paths.list,
        )
        self.enroll = async_to_streamed_response_wrapper(
            learning_paths.enroll,
        )

    @cached_property
    def modules(self) -> AsyncModulesResourceWithStreamingResponse:
        return AsyncModulesResourceWithStreamingResponse(self._learning_paths.modules)

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        return AsyncTopicsResourceWithStreamingResponse(self._learning_paths.topics)
