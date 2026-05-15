# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        health,
        resume,
        profile,
        analysis,
        roadmaps,
        taxonomy,
        favorites,
        alignments,
        jobs_board,
        assessments,
        notifications,
        learning_paths,
        recommendations,
        company_research,
    )
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.resume import ResumeResource, AsyncResumeResource
    from .resources.profile import ProfileResource, AsyncProfileResource
    from .resources.analysis import AnalysisResource, AsyncAnalysisResource
    from .resources.roadmaps import RoadmapsResource, AsyncRoadmapsResource
    from .resources.taxonomy import TaxonomyResource, AsyncTaxonomyResource
    from .resources.favorites import FavoritesResource, AsyncFavoritesResource
    from .resources.assessments import AssessmentsResource, AsyncAssessmentsResource
    from .resources.recommendations import RecommendationsResource, AsyncRecommendationsResource
    from .resources.company_research import CompanyResearchResource, AsyncCompanyResearchResource
    from .resources.alignments.alignments import AlignmentsResource, AsyncAlignmentsResource
    from .resources.jobs_board.jobs_board import JobsBoardResource, AsyncJobsBoardResource
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.learning_paths.learning_paths import LearningPathsResource, AsyncLearningPathsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Resalign",
    "AsyncResalign",
    "Client",
    "AsyncClient",
]


class Resalign(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Resalign client instance.

        This automatically infers the `api_key` argument from the `RESALIGN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RESALIGN_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("RESALIGN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        custom_headers_env = os.environ.get("RESALIGN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def taxonomy(self) -> TaxonomyResource:
        from .resources.taxonomy import TaxonomyResource

        return TaxonomyResource(self)

    @cached_property
    def alignments(self) -> AlignmentsResource:
        from .resources.alignments import AlignmentsResource

        return AlignmentsResource(self)

    @cached_property
    def analysis(self) -> AnalysisResource:
        from .resources.analysis import AnalysisResource

        return AnalysisResource(self)

    @cached_property
    def roadmaps(self) -> RoadmapsResource:
        from .resources.roadmaps import RoadmapsResource

        return RoadmapsResource(self)

    @cached_property
    def learning_paths(self) -> LearningPathsResource:
        from .resources.learning_paths import LearningPathsResource

        return LearningPathsResource(self)

    @cached_property
    def company_research(self) -> CompanyResearchResource:
        from .resources.company_research import CompanyResearchResource

        return CompanyResearchResource(self)

    @cached_property
    def jobs_board(self) -> JobsBoardResource:
        from .resources.jobs_board import JobsBoardResource

        return JobsBoardResource(self)

    @cached_property
    def favorites(self) -> FavoritesResource:
        from .resources.favorites import FavoritesResource

        return FavoritesResource(self)

    @cached_property
    def resume(self) -> ResumeResource:
        from .resources.resume import ResumeResource

        return ResumeResource(self)

    @cached_property
    def profile(self) -> ProfileResource:
        from .resources.profile import ProfileResource

        return ProfileResource(self)

    @cached_property
    def recommendations(self) -> RecommendationsResource:
        from .resources.recommendations import RecommendationsResource

        return RecommendationsResource(self)

    @cached_property
    def assessments(self) -> AssessmentsResource:
        from .resources.assessments import AssessmentsResource

        return AssessmentsResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def with_raw_response(self) -> ResalignWithRawResponse:
        return ResalignWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResalignWithStreamedResponse:
        return ResalignWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncResalign(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncResalign client instance.

        This automatically infers the `api_key` argument from the `RESALIGN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("RESALIGN_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("RESALIGN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        custom_headers_env = os.environ.get("RESALIGN_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def taxonomy(self) -> AsyncTaxonomyResource:
        from .resources.taxonomy import AsyncTaxonomyResource

        return AsyncTaxonomyResource(self)

    @cached_property
    def alignments(self) -> AsyncAlignmentsResource:
        from .resources.alignments import AsyncAlignmentsResource

        return AsyncAlignmentsResource(self)

    @cached_property
    def analysis(self) -> AsyncAnalysisResource:
        from .resources.analysis import AsyncAnalysisResource

        return AsyncAnalysisResource(self)

    @cached_property
    def roadmaps(self) -> AsyncRoadmapsResource:
        from .resources.roadmaps import AsyncRoadmapsResource

        return AsyncRoadmapsResource(self)

    @cached_property
    def learning_paths(self) -> AsyncLearningPathsResource:
        from .resources.learning_paths import AsyncLearningPathsResource

        return AsyncLearningPathsResource(self)

    @cached_property
    def company_research(self) -> AsyncCompanyResearchResource:
        from .resources.company_research import AsyncCompanyResearchResource

        return AsyncCompanyResearchResource(self)

    @cached_property
    def jobs_board(self) -> AsyncJobsBoardResource:
        from .resources.jobs_board import AsyncJobsBoardResource

        return AsyncJobsBoardResource(self)

    @cached_property
    def favorites(self) -> AsyncFavoritesResource:
        from .resources.favorites import AsyncFavoritesResource

        return AsyncFavoritesResource(self)

    @cached_property
    def resume(self) -> AsyncResumeResource:
        from .resources.resume import AsyncResumeResource

        return AsyncResumeResource(self)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        from .resources.profile import AsyncProfileResource

        return AsyncProfileResource(self)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResource:
        from .resources.recommendations import AsyncRecommendationsResource

        return AsyncRecommendationsResource(self)

    @cached_property
    def assessments(self) -> AsyncAssessmentsResource:
        from .resources.assessments import AsyncAssessmentsResource

        return AsyncAssessmentsResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncResalignWithRawResponse:
        return AsyncResalignWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResalignWithStreamedResponse:
        return AsyncResalignWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ResalignWithRawResponse:
    _client: Resalign

    def __init__(self, client: Resalign) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def taxonomy(self) -> taxonomy.TaxonomyResourceWithRawResponse:
        from .resources.taxonomy import TaxonomyResourceWithRawResponse

        return TaxonomyResourceWithRawResponse(self._client.taxonomy)

    @cached_property
    def alignments(self) -> alignments.AlignmentsResourceWithRawResponse:
        from .resources.alignments import AlignmentsResourceWithRawResponse

        return AlignmentsResourceWithRawResponse(self._client.alignments)

    @cached_property
    def analysis(self) -> analysis.AnalysisResourceWithRawResponse:
        from .resources.analysis import AnalysisResourceWithRawResponse

        return AnalysisResourceWithRawResponse(self._client.analysis)

    @cached_property
    def roadmaps(self) -> roadmaps.RoadmapsResourceWithRawResponse:
        from .resources.roadmaps import RoadmapsResourceWithRawResponse

        return RoadmapsResourceWithRawResponse(self._client.roadmaps)

    @cached_property
    def learning_paths(self) -> learning_paths.LearningPathsResourceWithRawResponse:
        from .resources.learning_paths import LearningPathsResourceWithRawResponse

        return LearningPathsResourceWithRawResponse(self._client.learning_paths)

    @cached_property
    def company_research(self) -> company_research.CompanyResearchResourceWithRawResponse:
        from .resources.company_research import CompanyResearchResourceWithRawResponse

        return CompanyResearchResourceWithRawResponse(self._client.company_research)

    @cached_property
    def jobs_board(self) -> jobs_board.JobsBoardResourceWithRawResponse:
        from .resources.jobs_board import JobsBoardResourceWithRawResponse

        return JobsBoardResourceWithRawResponse(self._client.jobs_board)

    @cached_property
    def favorites(self) -> favorites.FavoritesResourceWithRawResponse:
        from .resources.favorites import FavoritesResourceWithRawResponse

        return FavoritesResourceWithRawResponse(self._client.favorites)

    @cached_property
    def resume(self) -> resume.ResumeResourceWithRawResponse:
        from .resources.resume import ResumeResourceWithRawResponse

        return ResumeResourceWithRawResponse(self._client.resume)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithRawResponse:
        from .resources.profile import ProfileResourceWithRawResponse

        return ProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def recommendations(self) -> recommendations.RecommendationsResourceWithRawResponse:
        from .resources.recommendations import RecommendationsResourceWithRawResponse

        return RecommendationsResourceWithRawResponse(self._client.recommendations)

    @cached_property
    def assessments(self) -> assessments.AssessmentsResourceWithRawResponse:
        from .resources.assessments import AssessmentsResourceWithRawResponse

        return AssessmentsResourceWithRawResponse(self._client.assessments)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)


class AsyncResalignWithRawResponse:
    _client: AsyncResalign

    def __init__(self, client: AsyncResalign) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def taxonomy(self) -> taxonomy.AsyncTaxonomyResourceWithRawResponse:
        from .resources.taxonomy import AsyncTaxonomyResourceWithRawResponse

        return AsyncTaxonomyResourceWithRawResponse(self._client.taxonomy)

    @cached_property
    def alignments(self) -> alignments.AsyncAlignmentsResourceWithRawResponse:
        from .resources.alignments import AsyncAlignmentsResourceWithRawResponse

        return AsyncAlignmentsResourceWithRawResponse(self._client.alignments)

    @cached_property
    def analysis(self) -> analysis.AsyncAnalysisResourceWithRawResponse:
        from .resources.analysis import AsyncAnalysisResourceWithRawResponse

        return AsyncAnalysisResourceWithRawResponse(self._client.analysis)

    @cached_property
    def roadmaps(self) -> roadmaps.AsyncRoadmapsResourceWithRawResponse:
        from .resources.roadmaps import AsyncRoadmapsResourceWithRawResponse

        return AsyncRoadmapsResourceWithRawResponse(self._client.roadmaps)

    @cached_property
    def learning_paths(self) -> learning_paths.AsyncLearningPathsResourceWithRawResponse:
        from .resources.learning_paths import AsyncLearningPathsResourceWithRawResponse

        return AsyncLearningPathsResourceWithRawResponse(self._client.learning_paths)

    @cached_property
    def company_research(self) -> company_research.AsyncCompanyResearchResourceWithRawResponse:
        from .resources.company_research import AsyncCompanyResearchResourceWithRawResponse

        return AsyncCompanyResearchResourceWithRawResponse(self._client.company_research)

    @cached_property
    def jobs_board(self) -> jobs_board.AsyncJobsBoardResourceWithRawResponse:
        from .resources.jobs_board import AsyncJobsBoardResourceWithRawResponse

        return AsyncJobsBoardResourceWithRawResponse(self._client.jobs_board)

    @cached_property
    def favorites(self) -> favorites.AsyncFavoritesResourceWithRawResponse:
        from .resources.favorites import AsyncFavoritesResourceWithRawResponse

        return AsyncFavoritesResourceWithRawResponse(self._client.favorites)

    @cached_property
    def resume(self) -> resume.AsyncResumeResourceWithRawResponse:
        from .resources.resume import AsyncResumeResourceWithRawResponse

        return AsyncResumeResourceWithRawResponse(self._client.resume)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithRawResponse:
        from .resources.profile import AsyncProfileResourceWithRawResponse

        return AsyncProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def recommendations(self) -> recommendations.AsyncRecommendationsResourceWithRawResponse:
        from .resources.recommendations import AsyncRecommendationsResourceWithRawResponse

        return AsyncRecommendationsResourceWithRawResponse(self._client.recommendations)

    @cached_property
    def assessments(self) -> assessments.AsyncAssessmentsResourceWithRawResponse:
        from .resources.assessments import AsyncAssessmentsResourceWithRawResponse

        return AsyncAssessmentsResourceWithRawResponse(self._client.assessments)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)


class ResalignWithStreamedResponse:
    _client: Resalign

    def __init__(self, client: Resalign) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def taxonomy(self) -> taxonomy.TaxonomyResourceWithStreamingResponse:
        from .resources.taxonomy import TaxonomyResourceWithStreamingResponse

        return TaxonomyResourceWithStreamingResponse(self._client.taxonomy)

    @cached_property
    def alignments(self) -> alignments.AlignmentsResourceWithStreamingResponse:
        from .resources.alignments import AlignmentsResourceWithStreamingResponse

        return AlignmentsResourceWithStreamingResponse(self._client.alignments)

    @cached_property
    def analysis(self) -> analysis.AnalysisResourceWithStreamingResponse:
        from .resources.analysis import AnalysisResourceWithStreamingResponse

        return AnalysisResourceWithStreamingResponse(self._client.analysis)

    @cached_property
    def roadmaps(self) -> roadmaps.RoadmapsResourceWithStreamingResponse:
        from .resources.roadmaps import RoadmapsResourceWithStreamingResponse

        return RoadmapsResourceWithStreamingResponse(self._client.roadmaps)

    @cached_property
    def learning_paths(self) -> learning_paths.LearningPathsResourceWithStreamingResponse:
        from .resources.learning_paths import LearningPathsResourceWithStreamingResponse

        return LearningPathsResourceWithStreamingResponse(self._client.learning_paths)

    @cached_property
    def company_research(self) -> company_research.CompanyResearchResourceWithStreamingResponse:
        from .resources.company_research import CompanyResearchResourceWithStreamingResponse

        return CompanyResearchResourceWithStreamingResponse(self._client.company_research)

    @cached_property
    def jobs_board(self) -> jobs_board.JobsBoardResourceWithStreamingResponse:
        from .resources.jobs_board import JobsBoardResourceWithStreamingResponse

        return JobsBoardResourceWithStreamingResponse(self._client.jobs_board)

    @cached_property
    def favorites(self) -> favorites.FavoritesResourceWithStreamingResponse:
        from .resources.favorites import FavoritesResourceWithStreamingResponse

        return FavoritesResourceWithStreamingResponse(self._client.favorites)

    @cached_property
    def resume(self) -> resume.ResumeResourceWithStreamingResponse:
        from .resources.resume import ResumeResourceWithStreamingResponse

        return ResumeResourceWithStreamingResponse(self._client.resume)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithStreamingResponse:
        from .resources.profile import ProfileResourceWithStreamingResponse

        return ProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def recommendations(self) -> recommendations.RecommendationsResourceWithStreamingResponse:
        from .resources.recommendations import RecommendationsResourceWithStreamingResponse

        return RecommendationsResourceWithStreamingResponse(self._client.recommendations)

    @cached_property
    def assessments(self) -> assessments.AssessmentsResourceWithStreamingResponse:
        from .resources.assessments import AssessmentsResourceWithStreamingResponse

        return AssessmentsResourceWithStreamingResponse(self._client.assessments)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)


class AsyncResalignWithStreamedResponse:
    _client: AsyncResalign

    def __init__(self, client: AsyncResalign) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def taxonomy(self) -> taxonomy.AsyncTaxonomyResourceWithStreamingResponse:
        from .resources.taxonomy import AsyncTaxonomyResourceWithStreamingResponse

        return AsyncTaxonomyResourceWithStreamingResponse(self._client.taxonomy)

    @cached_property
    def alignments(self) -> alignments.AsyncAlignmentsResourceWithStreamingResponse:
        from .resources.alignments import AsyncAlignmentsResourceWithStreamingResponse

        return AsyncAlignmentsResourceWithStreamingResponse(self._client.alignments)

    @cached_property
    def analysis(self) -> analysis.AsyncAnalysisResourceWithStreamingResponse:
        from .resources.analysis import AsyncAnalysisResourceWithStreamingResponse

        return AsyncAnalysisResourceWithStreamingResponse(self._client.analysis)

    @cached_property
    def roadmaps(self) -> roadmaps.AsyncRoadmapsResourceWithStreamingResponse:
        from .resources.roadmaps import AsyncRoadmapsResourceWithStreamingResponse

        return AsyncRoadmapsResourceWithStreamingResponse(self._client.roadmaps)

    @cached_property
    def learning_paths(self) -> learning_paths.AsyncLearningPathsResourceWithStreamingResponse:
        from .resources.learning_paths import AsyncLearningPathsResourceWithStreamingResponse

        return AsyncLearningPathsResourceWithStreamingResponse(self._client.learning_paths)

    @cached_property
    def company_research(self) -> company_research.AsyncCompanyResearchResourceWithStreamingResponse:
        from .resources.company_research import AsyncCompanyResearchResourceWithStreamingResponse

        return AsyncCompanyResearchResourceWithStreamingResponse(self._client.company_research)

    @cached_property
    def jobs_board(self) -> jobs_board.AsyncJobsBoardResourceWithStreamingResponse:
        from .resources.jobs_board import AsyncJobsBoardResourceWithStreamingResponse

        return AsyncJobsBoardResourceWithStreamingResponse(self._client.jobs_board)

    @cached_property
    def favorites(self) -> favorites.AsyncFavoritesResourceWithStreamingResponse:
        from .resources.favorites import AsyncFavoritesResourceWithStreamingResponse

        return AsyncFavoritesResourceWithStreamingResponse(self._client.favorites)

    @cached_property
    def resume(self) -> resume.AsyncResumeResourceWithStreamingResponse:
        from .resources.resume import AsyncResumeResourceWithStreamingResponse

        return AsyncResumeResourceWithStreamingResponse(self._client.resume)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithStreamingResponse:
        from .resources.profile import AsyncProfileResourceWithStreamingResponse

        return AsyncProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def recommendations(self) -> recommendations.AsyncRecommendationsResourceWithStreamingResponse:
        from .resources.recommendations import AsyncRecommendationsResourceWithStreamingResponse

        return AsyncRecommendationsResourceWithStreamingResponse(self._client.recommendations)

    @cached_property
    def assessments(self) -> assessments.AsyncAssessmentsResourceWithStreamingResponse:
        from .resources.assessments import AsyncAssessmentsResourceWithStreamingResponse

        return AsyncAssessmentsResourceWithStreamingResponse(self._client.assessments)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)


Client = Resalign

AsyncClient = AsyncResalign
