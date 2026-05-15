# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

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
from ...types.jobs_board import fetch_list_params
from ...types.jobs_board.job_posting import JobPosting
from ...types.jobs_board.fetch_list_response import FetchListResponse

__all__ = ["FetchResource", "AsyncFetchResource"]


class FetchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FetchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return FetchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FetchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return FetchResourceWithStreamingResponse(self)

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobPosting:
        """
        Retrieve a single job posting with full description and company information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/v1/jobs_board/fetch/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobPosting,
        )

    def list(
        self,
        *,
        company_size: Optional[str] | Omit = omit,
        department: Optional[str] | Omit = omit,
        employment_type: Optional[str] | Omit = omit,
        location_type: Optional[str] | Omit = omit,
        organization_type: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        salary_max: Optional[int] | Omit = omit,
        salary_min: Optional[int] | Omit = omit,
        search: Optional[str] | Omit = omit,
        sort_by: Literal["newest", "salary_high", "salary_low"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchListResponse:
        """
        List active job postings from the jobs board with optional search, filters, and
        pagination. Includes company information and user's saved status for each job.

        Args:
          company_size: Filter by company size: startup, small, medium, large, enterprise

          department: Filter by department

          employment_type: Filter by employment type: full-time, part-time, contract, internship

          location_type: Filter by location type: remote, hybrid, onsite

          organization_type: Filter by organization type: startup, scaleup, established, non-profit,
              government

          page: Page number (1-indexed)

          page_size: Items per page (max 50)

          salary_max: Maximum salary filter

          salary_min: Minimum salary filter

          search: Full-text search on title and description

          sort_by: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/jobs_board/fetch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_size": company_size,
                        "department": department,
                        "employment_type": employment_type,
                        "location_type": location_type,
                        "organization_type": organization_type,
                        "page": page,
                        "page_size": page_size,
                        "salary_max": salary_max,
                        "salary_min": salary_min,
                        "search": search,
                        "sort_by": sort_by,
                    },
                    fetch_list_params.FetchListParams,
                ),
            ),
            cast_to=FetchListResponse,
        )


class AsyncFetchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFetchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFetchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFetchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return AsyncFetchResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobPosting:
        """
        Retrieve a single job posting with full description and company information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/v1/jobs_board/fetch/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobPosting,
        )

    async def list(
        self,
        *,
        company_size: Optional[str] | Omit = omit,
        department: Optional[str] | Omit = omit,
        employment_type: Optional[str] | Omit = omit,
        location_type: Optional[str] | Omit = omit,
        organization_type: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        salary_max: Optional[int] | Omit = omit,
        salary_min: Optional[int] | Omit = omit,
        search: Optional[str] | Omit = omit,
        sort_by: Literal["newest", "salary_high", "salary_low"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FetchListResponse:
        """
        List active job postings from the jobs board with optional search, filters, and
        pagination. Includes company information and user's saved status for each job.

        Args:
          company_size: Filter by company size: startup, small, medium, large, enterprise

          department: Filter by department

          employment_type: Filter by employment type: full-time, part-time, contract, internship

          location_type: Filter by location type: remote, hybrid, onsite

          organization_type: Filter by organization type: startup, scaleup, established, non-profit,
              government

          page: Page number (1-indexed)

          page_size: Items per page (max 50)

          salary_max: Maximum salary filter

          salary_min: Minimum salary filter

          search: Full-text search on title and description

          sort_by: Sort order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/jobs_board/fetch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "company_size": company_size,
                        "department": department,
                        "employment_type": employment_type,
                        "location_type": location_type,
                        "organization_type": organization_type,
                        "page": page,
                        "page_size": page_size,
                        "salary_max": salary_max,
                        "salary_min": salary_min,
                        "search": search,
                        "sort_by": sort_by,
                    },
                    fetch_list_params.FetchListParams,
                ),
            ),
            cast_to=FetchListResponse,
        )


class FetchResourceWithRawResponse:
    def __init__(self, fetch: FetchResource) -> None:
        self._fetch = fetch

        self.retrieve = to_raw_response_wrapper(
            fetch.retrieve,
        )
        self.list = to_raw_response_wrapper(
            fetch.list,
        )


class AsyncFetchResourceWithRawResponse:
    def __init__(self, fetch: AsyncFetchResource) -> None:
        self._fetch = fetch

        self.retrieve = async_to_raw_response_wrapper(
            fetch.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            fetch.list,
        )


class FetchResourceWithStreamingResponse:
    def __init__(self, fetch: FetchResource) -> None:
        self._fetch = fetch

        self.retrieve = to_streamed_response_wrapper(
            fetch.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            fetch.list,
        )


class AsyncFetchResourceWithStreamingResponse:
    def __init__(self, fetch: AsyncFetchResource) -> None:
        self._fetch = fetch

        self.retrieve = async_to_streamed_response_wrapper(
            fetch.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            fetch.list,
        )
