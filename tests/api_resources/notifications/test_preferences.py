# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types.notifications import PreferenceUpdateResponse, PreferenceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Resalign) -> None:
        preference = client.notifications.preferences.retrieve()
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Resalign) -> None:
        response = client.notifications.preferences.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Resalign) -> None:
        with client.notifications.preferences.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Resalign) -> None:
        preference = client.notifications.preferences.update(
            email_enabled=True,
            event_type="event_type",
        )
        assert_matches_type(PreferenceUpdateResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Resalign) -> None:
        response = client.notifications.preferences.with_raw_response.update(
            email_enabled=True,
            event_type="event_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceUpdateResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Resalign) -> None:
        with client.notifications.preferences.with_streaming_response.update(
            email_enabled=True,
            event_type="event_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceUpdateResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncResalign) -> None:
        preference = await async_client.notifications.preferences.retrieve()
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncResalign) -> None:
        response = await async_client.notifications.preferences.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncResalign) -> None:
        async with async_client.notifications.preferences.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncResalign) -> None:
        preference = await async_client.notifications.preferences.update(
            email_enabled=True,
            event_type="event_type",
        )
        assert_matches_type(PreferenceUpdateResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncResalign) -> None:
        response = await async_client.notifications.preferences.with_raw_response.update(
            email_enabled=True,
            event_type="event_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceUpdateResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncResalign) -> None:
        async with async_client.notifications.preferences.with_streaming_response.update(
            email_enabled=True,
            event_type="event_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceUpdateResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True
