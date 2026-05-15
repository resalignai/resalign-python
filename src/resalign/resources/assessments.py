# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import assessment_auto_assess_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.assessment_auto_assess_response import AssessmentAutoAssessResponse

__all__ = ["AssessmentsResource", "AsyncAssessmentsResource"]


class AssessmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssessmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AssessmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssessmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AssessmentsResourceWithStreamingResponse(self)

    def auto_assess(
        self,
        *,
        job_id: str,
        tier: str,
        user_id: str,
        trigger: str | Omit = omit,
        x_service_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssessmentAutoAssessResponse:
        """
        Run auto-assessment for a single (user_id, job_id) pair.

        Called by Cloud Tasks after batch refresh. Service-key protected. Does NOT count
        against user's on-demand assessment quota.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Service-Key": x_service_key}), **(extra_headers or {})}
        return self._post(
            "/v1/assessments/auto-assess",
            body=maybe_transform(
                {
                    "job_id": job_id,
                    "tier": tier,
                    "user_id": user_id,
                    "trigger": trigger,
                },
                assessment_auto_assess_params.AssessmentAutoAssessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssessmentAutoAssessResponse,
        )


class AsyncAssessmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssessmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssessmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssessmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/resalign-python#with_streaming_response
        """
        return AsyncAssessmentsResourceWithStreamingResponse(self)

    async def auto_assess(
        self,
        *,
        job_id: str,
        tier: str,
        user_id: str,
        trigger: str | Omit = omit,
        x_service_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssessmentAutoAssessResponse:
        """
        Run auto-assessment for a single (user_id, job_id) pair.

        Called by Cloud Tasks after batch refresh. Service-key protected. Does NOT count
        against user's on-demand assessment quota.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Service-Key": x_service_key}), **(extra_headers or {})}
        return await self._post(
            "/v1/assessments/auto-assess",
            body=await async_maybe_transform(
                {
                    "job_id": job_id,
                    "tier": tier,
                    "user_id": user_id,
                    "trigger": trigger,
                },
                assessment_auto_assess_params.AssessmentAutoAssessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssessmentAutoAssessResponse,
        )


class AssessmentsResourceWithRawResponse:
    def __init__(self, assessments: AssessmentsResource) -> None:
        self._assessments = assessments

        self.auto_assess = to_raw_response_wrapper(
            assessments.auto_assess,
        )


class AsyncAssessmentsResourceWithRawResponse:
    def __init__(self, assessments: AsyncAssessmentsResource) -> None:
        self._assessments = assessments

        self.auto_assess = async_to_raw_response_wrapper(
            assessments.auto_assess,
        )


class AssessmentsResourceWithStreamingResponse:
    def __init__(self, assessments: AssessmentsResource) -> None:
        self._assessments = assessments

        self.auto_assess = to_streamed_response_wrapper(
            assessments.auto_assess,
        )


class AsyncAssessmentsResourceWithStreamingResponse:
    def __init__(self, assessments: AsyncAssessmentsResource) -> None:
        self._assessments = assessments

        self.auto_assess = async_to_streamed_response_wrapper(
            assessments.auto_assess,
        )
