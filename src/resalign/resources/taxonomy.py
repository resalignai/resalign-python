# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import taxonomy_list_roles_params, taxonomy_search_skills_params
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
from ..types.taxonomy_list_roles_response import TaxonomyListRolesResponse
from ..types.taxonomy_search_skills_response import TaxonomySearchSkillsResponse
from ..types.taxonomy_list_functions_response import TaxonomyListFunctionsResponse

__all__ = ["TaxonomyResource", "AsyncTaxonomyResource"]


class TaxonomyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaxonomyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return TaxonomyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaxonomyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return TaxonomyResourceWithStreamingResponse(self)

    def list_functions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxonomyListFunctionsResponse:
        """Return all top-level job function keys with display labels."""
        return self._get(
            "/v1/taxonomy/functions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxonomyListFunctionsResponse,
        )

    def list_roles(
        self,
        *,
        function: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxonomyListRolesResponse:
        """
        Return canonical role names for a given job function key.

        Args:
          function: Job function key, e.g. software_engineering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/taxonomy/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"function": function}, taxonomy_list_roles_params.TaxonomyListRolesParams),
            ),
            cast_to=TaxonomyListRolesResponse,
        )

    def search_skills(
        self,
        *,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxonomySearchSkillsResponse:
        """Return skills matching the search query.

        Returns all skills when q is empty.

        Args:
          limit: Max results

          q: Partial skill name to search for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/taxonomy/skills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "q": q,
                    },
                    taxonomy_search_skills_params.TaxonomySearchSkillsParams,
                ),
            ),
            cast_to=TaxonomySearchSkillsResponse,
        )


class AsyncTaxonomyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaxonomyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaxonomyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaxonomyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncTaxonomyResourceWithStreamingResponse(self)

    async def list_functions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxonomyListFunctionsResponse:
        """Return all top-level job function keys with display labels."""
        return await self._get(
            "/v1/taxonomy/functions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxonomyListFunctionsResponse,
        )

    async def list_roles(
        self,
        *,
        function: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxonomyListRolesResponse:
        """
        Return canonical role names for a given job function key.

        Args:
          function: Job function key, e.g. software_engineering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/taxonomy/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"function": function}, taxonomy_list_roles_params.TaxonomyListRolesParams
                ),
            ),
            cast_to=TaxonomyListRolesResponse,
        )

    async def search_skills(
        self,
        *,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxonomySearchSkillsResponse:
        """Return skills matching the search query.

        Returns all skills when q is empty.

        Args:
          limit: Max results

          q: Partial skill name to search for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/taxonomy/skills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "q": q,
                    },
                    taxonomy_search_skills_params.TaxonomySearchSkillsParams,
                ),
            ),
            cast_to=TaxonomySearchSkillsResponse,
        )


class TaxonomyResourceWithRawResponse:
    def __init__(self, taxonomy: TaxonomyResource) -> None:
        self._taxonomy = taxonomy

        self.list_functions = to_raw_response_wrapper(
            taxonomy.list_functions,
        )
        self.list_roles = to_raw_response_wrapper(
            taxonomy.list_roles,
        )
        self.search_skills = to_raw_response_wrapper(
            taxonomy.search_skills,
        )


class AsyncTaxonomyResourceWithRawResponse:
    def __init__(self, taxonomy: AsyncTaxonomyResource) -> None:
        self._taxonomy = taxonomy

        self.list_functions = async_to_raw_response_wrapper(
            taxonomy.list_functions,
        )
        self.list_roles = async_to_raw_response_wrapper(
            taxonomy.list_roles,
        )
        self.search_skills = async_to_raw_response_wrapper(
            taxonomy.search_skills,
        )


class TaxonomyResourceWithStreamingResponse:
    def __init__(self, taxonomy: TaxonomyResource) -> None:
        self._taxonomy = taxonomy

        self.list_functions = to_streamed_response_wrapper(
            taxonomy.list_functions,
        )
        self.list_roles = to_streamed_response_wrapper(
            taxonomy.list_roles,
        )
        self.search_skills = to_streamed_response_wrapper(
            taxonomy.search_skills,
        )


class AsyncTaxonomyResourceWithStreamingResponse:
    def __init__(self, taxonomy: AsyncTaxonomyResource) -> None:
        self._taxonomy = taxonomy

        self.list_functions = async_to_streamed_response_wrapper(
            taxonomy.list_functions,
        )
        self.list_roles = async_to_streamed_response_wrapper(
            taxonomy.list_roles,
        )
        self.search_skills = async_to_streamed_response_wrapper(
            taxonomy.search_skills,
        )
