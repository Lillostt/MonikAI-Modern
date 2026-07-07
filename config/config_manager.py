"""Central configuration manager for MonikAI Modern.

This module is intended to become the single place that loads and saves
config.json. It keeps the existing JSON structure intact so the current
project behavior stays compatible while other modules migrate gradually.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Optional

CONFIG_FILENAME = "config.json"

DEFAULT_CONFIG: Dict[str, Any] = {
    "GAME_PATH": "",
    "WEBUI_PATH": "",
    "USE_TTS": 0,
    "LAUNCH_YOURSELF": 0,
    "LAUNCH_YOURSELF_WEBUI": 0,
    "USE_ACTIONS": 0,
    "TTS_MODEL": "Your TTS",
    "USE_SPEECH_RECOGNITION": 0,
    "VOICE_SAMPLE_TORTOISE": "Choose a Tortoise voice sample",
    "VOICE_SAMPLE_COQUI": "Choose a YourTTS voice sample",
}

_config_cache: Optional[Dict[str, Any]] = None


def get_config_path(path: Optional[str | Path] = None) -> Path:
    """Return the absolute path to config.json."""
    if path is not None:
        return Path(path).resolve()
    return (Path(__file__).resolve().parents[1] / CONFIG_FILENAME).resolve()


def _merge_with_defaults(config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Fill in any missing keys while preserving the current config format."""
    merged = deepcopy(DEFAULT_CONFIG)
    if isinstance(config, dict):
        merged.update({key: value for key, value in config.items() if key in DEFAULT_CONFIG})
    return merged


def load_config(force_reload: bool = False) -> Dict[str, Any]:
    """Load config.json from disk, or create it with defaults if missing."""
    global _config_cache

    if _config_cache is not None and not force_reload:
        return deepcopy(_config_cache)

    config_path = get_config_path()
    if config_path.exists():
        try:
            with config_path.open("r", encoding="utf-8") as handle:
                loaded = json.load(handle)
        except (json.JSONDecodeError, OSError):
            loaded = {}
    else:
        loaded = {}

    _config_cache = _merge_with_defaults(loaded)
    return deepcopy(_config_cache)


def save_config(config: Optional[Dict[str, Any]] = None, path: Optional[str | Path] = None) -> Dict[str, Any]:
    """Persist configuration to config.json using the current schema."""
    global _config_cache

    if config is None:
        config = deepcopy(_config_cache if _config_cache is not None else load_config())

    normalized = _merge_with_defaults(config)
    config_path = get_config_path(path)
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open("w", encoding="utf-8") as handle:
        json.dump(normalized, handle, indent=2)
        handle.write("\n")

    _config_cache = normalized
    return deepcopy(normalized)


def get_config_value(key: str, default: Any = None) -> Any:
    """Read a single value from the loaded configuration."""
    config = load_config()
    return config.get(key, default)


def set_config_value(key: str, value: Any, path: Optional[str | Path] = None) -> Dict[str, Any]:
    """Set a single value and save it back to disk."""
    config = load_config()
    config[key] = value
    return save_config(config, path)


def update_config(updates: Dict[str, Any], path: Optional[str | Path] = None) -> Dict[str, Any]:
    """Update multiple values at once and persist them."""
    config = load_config()
    config.update(updates)
    return save_config(config, path)
