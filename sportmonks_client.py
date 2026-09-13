from __future__ import annotations

import os
from typing import Any

import requests


class SportmonksClient:
    BASE_URL = "https://api.sportmonks.com/v3/football"

    def __init__(
        self,
        token: str | None = None,
        timeout: int = 30,
    ) -> None:
        self.token = token or os.getenv("SPORTMONKS_API_TOKEN")
        self.timeout = timeout

        if not self.token:
            raise RuntimeError(
                "SPORTMONKS_API_TOKEN is not configured"
            )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        request_params = dict(params or {})
        request_params["api_token"] = self.token

        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"

        response = requests.get(
            url,
            params=request_params,
            timeout=self.timeout,
        )

        if not response.ok:
            raise RuntimeError(
                f"Sportmonks API error "
                f"{response.status_code}: "
                f"{response.text[:500]}"
            )

        data = response.json()

        if not isinstance(data, dict):
            raise RuntimeError(
                "Sportmonks returned an unexpected response"
            )

        return data

    def get_fixtures_between(
        self,
        start_date: str,
        end_date: str,
    ) -> dict[str, Any]:
        return self.get(
            "fixtures/between",
            {
                "start": start_date,
                "end": end_date,
                "include": "participants;scores;state",
            },
        )
