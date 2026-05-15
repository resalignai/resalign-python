# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import company_research_run_params, company_research_enrich_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.company_research_enrich_response import CompanyResearchEnrichResponse
from ..types.company_research_result_response import CompanyResearchResultResponse
from ..types.company_research_retrieve_response import CompanyResearchRetrieveResponse

__all__ = ["CompanyResearchResource", "AsyncCompanyResearchResource"]


class CompanyResearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompanyResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return CompanyResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompanyResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return CompanyResearchResourceWithStreamingResponse(self)

    def retrieve(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyResearchRetrieveResponse:
        """
        Check the status of a company research profile.

        Returns the current status from the database. No external provider calls.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            path_template("/v1/company_research/retrieve/{identifier}", identifier=identifier),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResearchRetrieveResponse,
        )

    def enrich(
        self,
        *,
        concurrency: int | Omit = omit,
        limit: Optional[int] | Omit = omit,
        stale_days: int | Omit = omit,
        x_service_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyResearchEnrichResponse:
        """
        Queue re-enrichment of stale and failed company profiles.

        Selects profiles where:

        - `research_status = 'completed'` AND `updated_at < now() - stale_days`, OR
        - `research_status IN ('failed', 'cancelled')`

        Returns immediately (HTTP 202) and runs enrichment as a background task.

        Args:
          concurrency: Max concurrent Parallel research tasks

          limit: Maximum number of companies to enrich in this run

          stale_days: Re-enrich profiles whose updated_at is older than this many days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Service-Key": x_service_key}), **(extra_headers or {})}
        return self._post(
            "/v1/company_research/enrich",
            body=maybe_transform(
                {
                    "concurrency": concurrency,
                    "limit": limit,
                    "stale_days": stale_days,
                },
                company_research_enrich_params.CompanyResearchEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResearchEnrichResponse,
        )

    def result(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyResearchResultResponse:
        """
        Fetch the research output for a company profile.

        Accepts a company_profiles UUID as the identifier. Returns the persisted
        research output from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            path_template("/v1/company_research/result/{identifier}", identifier=identifier),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResearchResultResponse,
        )

    def run(
        self,
        *,
        company_name: str,
        stream: bool | Omit = omit,
        company_directory_id: Optional[str] | Omit = omit,
        linkedin_url: Optional[str] | Omit = omit,
        website_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Run deep company research via E2B sandbox with Claude Code + Exa MCP.

        With stream=true: returns SSE event stream with real-time progress. With
        stream=false (default): returns JSON response when complete.

        If the company has already been researched, returns the cached result.

        Args:
          company_name: Name of the company to research

          stream: Return SSE stream instead of JSON

          company_directory_id: UUID from companies_directory for idempotency

          linkedin_url: Company LinkedIn page URL

          website_url: Company website URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/company_research/run",
            body=maybe_transform(
                {
                    "company_name": company_name,
                    "company_directory_id": company_directory_id,
                    "linkedin_url": linkedin_url,
                    "website_url": website_url,
                },
                company_research_run_params.CompanyResearchRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, company_research_run_params.CompanyResearchRunParams),
            ),
            cast_to=object,
        )


class AsyncCompanyResearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompanyResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompanyResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompanyResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncCompanyResearchResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyResearchRetrieveResponse:
        """
        Check the status of a company research profile.

        Returns the current status from the database. No external provider calls.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            path_template("/v1/company_research/retrieve/{identifier}", identifier=identifier),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResearchRetrieveResponse,
        )

    async def enrich(
        self,
        *,
        concurrency: int | Omit = omit,
        limit: Optional[int] | Omit = omit,
        stale_days: int | Omit = omit,
        x_service_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyResearchEnrichResponse:
        """
        Queue re-enrichment of stale and failed company profiles.

        Selects profiles where:

        - `research_status = 'completed'` AND `updated_at < now() - stale_days`, OR
        - `research_status IN ('failed', 'cancelled')`

        Returns immediately (HTTP 202) and runs enrichment as a background task.

        Args:
          concurrency: Max concurrent Parallel research tasks

          limit: Maximum number of companies to enrich in this run

          stale_days: Re-enrich profiles whose updated_at is older than this many days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Service-Key": x_service_key}), **(extra_headers or {})}
        return await self._post(
            "/v1/company_research/enrich",
            body=await async_maybe_transform(
                {
                    "concurrency": concurrency,
                    "limit": limit,
                    "stale_days": stale_days,
                },
                company_research_enrich_params.CompanyResearchEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResearchEnrichResponse,
        )

    async def result(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompanyResearchResultResponse:
        """
        Fetch the research output for a company profile.

        Accepts a company_profiles UUID as the identifier. Returns the persisted
        research output from the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            path_template("/v1/company_research/result/{identifier}", identifier=identifier),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyResearchResultResponse,
        )

    async def run(
        self,
        *,
        company_name: str,
        stream: bool | Omit = omit,
        company_directory_id: Optional[str] | Omit = omit,
        linkedin_url: Optional[str] | Omit = omit,
        website_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Run deep company research via E2B sandbox with Claude Code + Exa MCP.

        With stream=true: returns SSE event stream with real-time progress. With
        stream=false (default): returns JSON response when complete.

        If the company has already been researched, returns the cached result.

        Args:
          company_name: Name of the company to research

          stream: Return SSE stream instead of JSON

          company_directory_id: UUID from companies_directory for idempotency

          linkedin_url: Company LinkedIn page URL

          website_url: Company website URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/company_research/run",
            body=await async_maybe_transform(
                {
                    "company_name": company_name,
                    "company_directory_id": company_directory_id,
                    "linkedin_url": linkedin_url,
                    "website_url": website_url,
                },
                company_research_run_params.CompanyResearchRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"stream": stream}, company_research_run_params.CompanyResearchRunParams
                ),
            ),
            cast_to=object,
        )


class CompanyResearchResourceWithRawResponse:
    def __init__(self, company_research: CompanyResearchResource) -> None:
        self._company_research = company_research

        self.retrieve = to_raw_response_wrapper(
            company_research.retrieve,
        )
        self.enrich = to_raw_response_wrapper(
            company_research.enrich,
        )
        self.result = to_raw_response_wrapper(
            company_research.result,
        )
        self.run = to_raw_response_wrapper(
            company_research.run,
        )


class AsyncCompanyResearchResourceWithRawResponse:
    def __init__(self, company_research: AsyncCompanyResearchResource) -> None:
        self._company_research = company_research

        self.retrieve = async_to_raw_response_wrapper(
            company_research.retrieve,
        )
        self.enrich = async_to_raw_response_wrapper(
            company_research.enrich,
        )
        self.result = async_to_raw_response_wrapper(
            company_research.result,
        )
        self.run = async_to_raw_response_wrapper(
            company_research.run,
        )


class CompanyResearchResourceWithStreamingResponse:
    def __init__(self, company_research: CompanyResearchResource) -> None:
        self._company_research = company_research

        self.retrieve = to_streamed_response_wrapper(
            company_research.retrieve,
        )
        self.enrich = to_streamed_response_wrapper(
            company_research.enrich,
        )
        self.result = to_streamed_response_wrapper(
            company_research.result,
        )
        self.run = to_streamed_response_wrapper(
            company_research.run,
        )


class AsyncCompanyResearchResourceWithStreamingResponse:
    def __init__(self, company_research: AsyncCompanyResearchResource) -> None:
        self._company_research = company_research

        self.retrieve = async_to_streamed_response_wrapper(
            company_research.retrieve,
        )
        self.enrich = async_to_streamed_response_wrapper(
            company_research.enrich,
        )
        self.result = async_to_streamed_response_wrapper(
            company_research.result,
        )
        self.run = async_to_streamed_response_wrapper(
            company_research.run,
        )
