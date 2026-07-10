"""
Canonical Conversation Context model.

This dataclass represents the current conversation state shared
between the Context Engine and future MonikAI subsystems.

It intentionally contains no business logic.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ConversationContext:
    # Tracks the current subject of discussion.
    active_topic: dict[str, Any] = field(default_factory=dict)
    # Stores the latest messages for immediate reference.
    recent_messages: dict[str, Any] = field(default_factory=dict)
    # Tracks unanswered questions to ensure completeness.
    open_questions: dict[str, Any] = field(default_factory=dict)
    # Documents the objectives being pursued.
    goals: dict[str, Any] = field(default_factory=dict)
    # Records timing information for conversation duration.
    runtime: dict[str, Any] = field(default_factory=dict)
    # Stores additional context-specific information.
    metadata: dict[str, Any] = field(default_factory=dict)