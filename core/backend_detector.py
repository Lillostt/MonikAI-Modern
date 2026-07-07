"""Backend availability detection for MonikAI Modern.

This module provides a small helper that waits until an OpenAI-compatible
backend is reachable. It is intentionally isolated so it can be integrated
later without changing the rest of the startup flow.
"""

from __future__ import annotations

import time

import requests

DEFAULT_API_BASE_URL: str = "http://127.0.0.1:5000"
DEFAULT_MODELS_ENDPOINT: str = "/v1/models"
DEFAULT_RETRY_SECONDS: float = 2.0


def wait_for_backend(
    api_base_url: str = DEFAULT_API_BASE_URL,
    models_endpoint: str = DEFAULT_MODELS_ENDPOINT,
    retry_seconds: float = DEFAULT_RETRY_SECONDS,
    timeout: float = 5.0,
) -> bool:
    """Wait indefinitely until an OpenAI-compatible backend responds.

    Args:
        api_base_url: Base URL for the backend, such as http://127.0.0.1:5000.
        models_endpoint: Path used for availability checks; defaults to /v1/models.
        retry_seconds: Delay between attempts.
        timeout: Per-request timeout in seconds.

    Returns:
        True once a successful response is received.
    """
    endpoint_url = f"{api_base_url.rstrip('/')}{models_endpoint}"

    while True:
        try:
            response = requests.get(endpoint_url, timeout=timeout)
            if response.ok:
                print(f"[backend] Backend available at {endpoint_url}")
                return True

            print(
                f"[backend] Waiting for backend at {endpoint_url} "
                f"(status {response.status_code}). Retrying in {retry_seconds} seconds..."
            )
        except KeyboardInterrupt:
            print("\n[backend] Backend detection cancelled by user.")
            raise
        except requests.RequestException as exc:
            print(
                f"[backend] Waiting for backend at {endpoint_url}: {exc}. "
                f"Retrying in {retry_seconds} seconds..."
            )

        time.sleep(retry_seconds)
