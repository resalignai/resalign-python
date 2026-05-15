# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from resalign import Resalign, AsyncResalign
from tests.utils import assert_matches_type
from resalign.types import NotificationDeliverResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deliver(self, client: Resalign) -> None:
        notification = client.notifications.deliver()
        assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deliver_with_all_params(self, client: Resalign) -> None:
        notification = client.notifications.deliver(
            x_service_key="X-Service-Key",
        )
        assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deliver(self, client: Resalign) -> None:
        response = client.notifications.with_raw_response.deliver()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deliver(self, client: Resalign) -> None:
        with client.notifications.with_streaming_response.deliver() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deliver(self, async_client: AsyncResalign) -> None:
        notification = await async_client.notifications.deliver()
        assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deliver_with_all_params(self, async_client: AsyncResalign) -> None:
        notification = await async_client.notifications.deliver(
            x_service_key="X-Service-Key",
        )
        assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deliver(self, async_client: AsyncResalign) -> None:
        response = await async_client.notifications.with_raw_response.deliver()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deliver(self, async_client: AsyncResalign) -> None:
        async with async_client.notifications.with_streaming_response.deliver() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationDeliverResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True
