# MonikAI Modern Project Structure

This document summarizes the current repository layout and the role of the main modules involved in startup and backend communication.

## Repository structure

- `assets/` — static assets used by the app and UI.
- `backend/` — backend-related code and supporting modules.
- `config/` — configuration helpers and config persistence.
- `core/` — core runtime components such as startup coordination and backend detection.
- `docs/` — project documentation.
- `game/` — Monika After Story-related game integration content.
- `images/` — image assets.
- `libs/` — bundled local Python runtime files.
- `scripts/` — helper scripts for login UI, TTS, and other support features.
- `tests/` — test files.
- `tortoise_audios/`, `coquiai_audios/` — audio assets for TTS voice samples.

## Major module purposes

- `config/config_manager.py` — central place for loading and saving `config.json` with default values and simple helper functions.
- `core/backend_detector.py` — waits for an OpenAI-compatible backend to become reachable.
- `core/startup_manager.py` — placeholder module for future startup orchestration.
- `api_client.py` — thin client for sending chat completions to the configured backend API.
- `main.py` — main application entry point that initializes startup behavior, launches the backend when configured, and handles the main runtime flow.
