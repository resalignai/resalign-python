# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import profile_update_preferences_params, profile_save_onboarding_step_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
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
        Get current user's profile with onboarding status and career preferences.
        Creates one if it doesn't exist.
        """
        return self._get(
            "/v1/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def complete_onboarding(
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
        Mark onboarding as complete and trigger initial job recommendations computation.
        """
        return self._post(
            "/v1/profile/complete-onboarding",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def merge_resume(
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
        Reads structured data from the user's most recently extracted resume, normalises
        skills and roles against the taxonomy, and writes them into
        pending_extracted_skills / pending_extracted_roles for the user to review.
        """
        return self._post(
            "/v1/profile/merge-resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def save_onboarding_step(
        self,
        step: int,
        *,
        data: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Save data for a specific onboarding step (1, 2, or 3).

        Validates fields and
        updates profile strength.

        Args:
          data: Step-specific preference fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/v1/profile/step/{step}", step=step),
            body=maybe_transform({"data": data}, profile_save_onboarding_step_params.ProfileSaveOnboardingStepParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_preferences(
        self,
        *,
        preferences: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Merge new preferences into existing user profile.

        Recalculates profile strength.

        Args:
          preferences: Preferences to merge into existing profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/profile",
            body=maybe_transform(
                {"preferences": preferences}, profile_update_preferences_params.ProfileUpdatePreferencesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/resalignai/resalign-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/resalignai/resalign-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
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
        Get current user's profile with onboarding status and career preferences.
        Creates one if it doesn't exist.
        """
        return await self._get(
            "/v1/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def complete_onboarding(
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
        Mark onboarding as complete and trigger initial job recommendations computation.
        """
        return await self._post(
            "/v1/profile/complete-onboarding",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def merge_resume(
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
        Reads structured data from the user's most recently extracted resume, normalises
        skills and roles against the taxonomy, and writes them into
        pending_extracted_skills / pending_extracted_roles for the user to review.
        """
        return await self._post(
            "/v1/profile/merge-resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def save_onboarding_step(
        self,
        step: int,
        *,
        data: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Save data for a specific onboarding step (1, 2, or 3).

        Validates fields and
        updates profile strength.

        Args:
          data: Step-specific preference fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/v1/profile/step/{step}", step=step),
            body=await async_maybe_transform(
                {"data": data}, profile_save_onboarding_step_params.ProfileSaveOnboardingStepParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_preferences(
        self,
        *,
        preferences: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Merge new preferences into existing user profile.

        Recalculates profile strength.

        Args:
          preferences: Preferences to merge into existing profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/profile",
            body=await async_maybe_transform(
                {"preferences": preferences}, profile_update_preferences_params.ProfileUpdatePreferencesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.complete_onboarding = to_raw_response_wrapper(
            profile.complete_onboarding,
        )
        self.merge_resume = to_raw_response_wrapper(
            profile.merge_resume,
        )
        self.save_onboarding_step = to_raw_response_wrapper(
            profile.save_onboarding_step,
        )
        self.update_preferences = to_raw_response_wrapper(
            profile.update_preferences,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.complete_onboarding = async_to_raw_response_wrapper(
            profile.complete_onboarding,
        )
        self.merge_resume = async_to_raw_response_wrapper(
            profile.merge_resume,
        )
        self.save_onboarding_step = async_to_raw_response_wrapper(
            profile.save_onboarding_step,
        )
        self.update_preferences = async_to_raw_response_wrapper(
            profile.update_preferences,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.complete_onboarding = to_streamed_response_wrapper(
            profile.complete_onboarding,
        )
        self.merge_resume = to_streamed_response_wrapper(
            profile.merge_resume,
        )
        self.save_onboarding_step = to_streamed_response_wrapper(
            profile.save_onboarding_step,
        )
        self.update_preferences = to_streamed_response_wrapper(
            profile.update_preferences,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.complete_onboarding = async_to_streamed_response_wrapper(
            profile.complete_onboarding,
        )
        self.merge_resume = async_to_streamed_response_wrapper(
            profile.merge_resume,
        )
        self.save_onboarding_step = async_to_streamed_response_wrapper(
            profile.save_onboarding_step,
        )
        self.update_preferences = async_to_streamed_response_wrapper(
            profile.update_preferences,
        )
