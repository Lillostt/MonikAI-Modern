"""
Canonical Relationship Context model.

This dataclass represents the relationship state shared between
the Context Engine and future MonikAI subsystems.

It intentionally contains no business logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

@dataclass
class RelationshipContext:
    """Canonical data model for relationship state management"""
    relationship:  dict[str, Any] = field(default_factory=dict)
    """Stores core relationship data from MAS including affection values and story progression"""
    
    player:  dict[str, Any] = field(default_factory=dict)
    """Contains player characteristics for personalized interactions"""
    
    preferences:  dict[str, Any] = field(default_factory=dict)
    """Defines interaction style and response characteristics"""
    
    interests:  dict[str, Any] = field(default_factory=dict)
    """Tracks player interests in music, gaming, and projects"""
    
    goals:  dict[str, Any] = field(default_factory=dict)
    """Stores short-term and long-term goals"""
    
    emotions:  dict[str, Any] = field(default_factory=dict)
    """Captures current emotional state and tone analysis"""
    
    recent_topics:  dict[str, Any] = field(default_factory=dict)
    """Tracks recent conversation topics and concerns"""
    
    memories:  dict[str, Any] = field(default_factory=dict)
    """Retains significant past experiences and milestones"""
    
    journal:  dict[str, Any] = field(default_factory=dict)
    """Maintains narrative consistency through conversation history"""
    
    runtime:  dict[str, Any] = field(default_factory=dict)
    """Supports real-time adaptation with session-specific data"""
    
    metadata:  dict[str, Any] = field(default_factory=dict)
    """Stores schema version, timestamps, context identifiers, and internal generation metadata."""