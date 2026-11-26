"""A rate-limited, retrying HTTP getter for scheduled litscan runs.

Scheduled scans call Europe PMC, UniProt and QuickGO hundreds of times, so each
host gets a minimum interval between calls and 429/5xx responses are retried
with exponential backoff (honouring ``Retry-After``). Anything else raises.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable
from urllib.parse import urlparse

import requests

RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})


def retry_delay(attempt: int, backoff: float, retry_after: str | None) -> float:
    """Seconds to wait before retry ``attempt`` (1-based).

    >>> retry_delay(1, 2.0, None)
    2.0
    >>> retry_delay(3, 2.0, None)
    8.0
    >>> retry_delay(1, 2.0, "11")
    11.0
    """
    if retry_after and retry_after.strip().isdigit():
        return float(retry_after)
    return backoff * 2 ** (attempt - 1)


@dataclass
class PoliteClient:
    """GET with a per-host minimum interval and bounded retries."""

    min_intervals: dict[str, float] = field(default_factory=dict)
    max_attempts: int = 5
    backoff_seconds: float = 2.0
    timeout: float = 30.0
    sleep: Callable[[float], None] = time.sleep
    _last_call: dict[str, float] = field(default_factory=dict)
    calls: int = 0
    session: requests.Session = field(default_factory=requests.Session)

    @classmethod
    def from_config(cls, config: dict[str, Any]) -> "PoliteClient":
        """Build from the ``rate_limits``/``retry`` blocks of a GeneGapScanConfig."""
        retry = config.get("retry") or {}
        return cls(
            min_intervals={
                r["host"]: float(r["min_interval_seconds"])
                for r in config.get("rate_limits") or []
            },
            max_attempts=int(retry.get("max_attempts", 5)),
            backoff_seconds=float(retry.get("backoff_seconds", 2.0)),
        )

    def _wait_turn(self, host: str) -> None:
        interval = self.min_intervals.get(host, 0.0)
        elapsed = time.monotonic() - self._last_call.get(host, 0.0)
        if elapsed < interval:
            self.sleep(interval - elapsed)
        self._last_call[host] = time.monotonic()

    def get(
        self,
        url: str,
        params: dict[str, Any] | list[tuple[str, str]] | None = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:
        """GET ``url``, retrying transient failures; raise on anything else."""
        host = urlparse(url).netloc
        for attempt in range(1, self.max_attempts + 1):
            self._wait_turn(host)
            self.calls += 1
            try:
                response = self.session.get(
                    url, params=params, headers=headers, timeout=self.timeout
                )
            except (requests.ConnectionError, requests.Timeout):
                # A network blip at an external service: retry, then re-raise.
                if attempt == self.max_attempts:
                    raise
                self.sleep(retry_delay(attempt, self.backoff_seconds, None))
                continue
            if response.status_code not in RETRY_STATUSES:
                response.raise_for_status()
                return response
            if attempt == self.max_attempts:
                response.raise_for_status()
            self.sleep(
                retry_delay(
                    attempt, self.backoff_seconds, response.headers.get("Retry-After")
                )
            )
        raise AssertionError("unreachable")
