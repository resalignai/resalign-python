# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.learning_paths import module_get_content_params, module_get_resources_params

__all__ = ["ModulesResource", "AsyncModulesResource"]


class ModulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return ModulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return ModulesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        module_id: str,
        *,
        path_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get detailed module information with topics.

        Returns: Module with all topics and their completion status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not module_id:
            raise ValueError(f"Expected a non-empty value for `module_id` but received {module_id!r}")
        return self._get(
            path_template("/v1/learning-paths/{path_id}/modules/{module_id}", path_id=path_id, module_id=module_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_content(
        self,
        module_id: str,
        *,
        path_id: str,
        generate: bool | Omit = omit,
        topic_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get or generate content for a specific topic in a module.

        If content hasn't been generated yet and generate=True, it will be generated
        on-demand.

        Args: path_id: Learning path ID module_id: Module ID topic_index: Index of the
        topic (0-based) generate: If True, generate content if not already generated

        Returns: Topic content (text, examples, key takeaways)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not module_id:
            raise ValueError(f"Expected a non-empty value for `module_id` but received {module_id!r}")
        return self._get(
            path_template(
                "/v1/learning-paths/{path_id}/modules/{module_id}/content", path_id=path_id, module_id=module_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "generate": generate,
                        "topic_index": topic_index,
                    },
                    module_get_content_params.ModuleGetContentParams,
                ),
            ),
            cast_to=object,
        )

    def get_resources(
        self,
        module_id: str,
        *,
        path_id: str,
        curate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get curated external resources for a module.

        If resources haven't been curated yet and curate=True, curates them on-demand.

        Args: path_id: Learning path ID module_id: Module ID curate: If True, curate
        resources if not already done

        Returns: List of curated resources (Coursera, YouTube, etc.)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not module_id:
            raise ValueError(f"Expected a non-empty value for `module_id` but received {module_id!r}")
        return self._get(
            path_template(
                "/v1/learning-paths/{path_id}/modules/{module_id}/resources", path_id=path_id, module_id=module_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"curate": curate}, module_get_resources_params.ModuleGetResourcesParams),
            ),
            cast_to=object,
        )


class AsyncModulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncModulesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        module_id: str,
        *,
        path_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get detailed module information with topics.

        Returns: Module with all topics and their completion status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not module_id:
            raise ValueError(f"Expected a non-empty value for `module_id` but received {module_id!r}")
        return await self._get(
            path_template("/v1/learning-paths/{path_id}/modules/{module_id}", path_id=path_id, module_id=module_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_content(
        self,
        module_id: str,
        *,
        path_id: str,
        generate: bool | Omit = omit,
        topic_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get or generate content for a specific topic in a module.

        If content hasn't been generated yet and generate=True, it will be generated
        on-demand.

        Args: path_id: Learning path ID module_id: Module ID topic_index: Index of the
        topic (0-based) generate: If True, generate content if not already generated

        Returns: Topic content (text, examples, key takeaways)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not module_id:
            raise ValueError(f"Expected a non-empty value for `module_id` but received {module_id!r}")
        return await self._get(
            path_template(
                "/v1/learning-paths/{path_id}/modules/{module_id}/content", path_id=path_id, module_id=module_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "generate": generate,
                        "topic_index": topic_index,
                    },
                    module_get_content_params.ModuleGetContentParams,
                ),
            ),
            cast_to=object,
        )

    async def get_resources(
        self,
        module_id: str,
        *,
        path_id: str,
        curate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get curated external resources for a module.

        If resources haven't been curated yet and curate=True, curates them on-demand.

        Args: path_id: Learning path ID module_id: Module ID curate: If True, curate
        resources if not already done

        Returns: List of curated resources (Coursera, YouTube, etc.)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        if not module_id:
            raise ValueError(f"Expected a non-empty value for `module_id` but received {module_id!r}")
        return await self._get(
            path_template(
                "/v1/learning-paths/{path_id}/modules/{module_id}/resources", path_id=path_id, module_id=module_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"curate": curate}, module_get_resources_params.ModuleGetResourcesParams
                ),
            ),
            cast_to=object,
        )


class ModulesResourceWithRawResponse:
    def __init__(self, modules: ModulesResource) -> None:
        self._modules = modules

        self.retrieve = to_raw_response_wrapper(
            modules.retrieve,
        )
        self.get_content = to_raw_response_wrapper(
            modules.get_content,
        )
        self.get_resources = to_raw_response_wrapper(
            modules.get_resources,
        )


class AsyncModulesResourceWithRawResponse:
    def __init__(self, modules: AsyncModulesResource) -> None:
        self._modules = modules

        self.retrieve = async_to_raw_response_wrapper(
            modules.retrieve,
        )
        self.get_content = async_to_raw_response_wrapper(
            modules.get_content,
        )
        self.get_resources = async_to_raw_response_wrapper(
            modules.get_resources,
        )


class ModulesResourceWithStreamingResponse:
    def __init__(self, modules: ModulesResource) -> None:
        self._modules = modules

        self.retrieve = to_streamed_response_wrapper(
            modules.retrieve,
        )
        self.get_content = to_streamed_response_wrapper(
            modules.get_content,
        )
        self.get_resources = to_streamed_response_wrapper(
            modules.get_resources,
        )


class AsyncModulesResourceWithStreamingResponse:
    def __init__(self, modules: AsyncModulesResource) -> None:
        self._modules = modules

        self.retrieve = async_to_streamed_response_wrapper(
            modules.retrieve,
        )
        self.get_content = async_to_streamed_response_wrapper(
            modules.get_content,
        )
        self.get_resources = async_to_streamed_response_wrapper(
            modules.get_resources,
        )
