# Relationship Context Data Model

This document defines the canonical data model for Relationship Context, aligning with architectural principles and implementation requirements.

## Core Relationship
- **Purpose**: Maintain foundational relationship data from MAS
- **Information**: Affection values, story progression markers, relationship milestones (e.g., First Kiss, Promise Ring)
- **Immutable/Mutable**: Immutable (sourced exclusively from MAS)
- **Primary Source**: MAS Integration
- **Update Frequency**: Static (rarely changes)
- **Retrieval Priority**: Critical

## Relationship Milestones
- **Purpose**: Track critical relationship events
- **Information**: Immutable relationship defining events
- **Immutable/Mutable**: Immutable
- **Primary Source**: MAS
- **Update Frequency**: Static
- **Retrieval Priority**: Critical

## Player Identity
- **Purpose**: Understand player characteristics for personalized interactions
- **Information**: 
  - Personal preferences (nicknames, pronouns)
  - Music tastes
  - Gaming habits
  - Project interests
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Daily
- **Retrieval Priority**: Important

## Personal Preferences
- **Purpose**: Shape interaction style and responses
- **Information**: 
  - Preferred communication style
  - Reaction to specific topics
  - Emotional thresholds
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Daily
- **Retrieval Priority**: Useful

## Music Interests
- **Purpose**: Create continuity through shared musical references
- **Information**: Favorite songs, albums, genres
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Daily
- **Retrieval Priority**: Useful

## Gaming Preferences
- **Purpose**: Establish shared interests through gaming references
- **Information**: 
  - Frequently mentioned games
  - Gaming achievements
  - Preferences
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Daily
- **Retrieval Priority**: Useful

## Project Interests
- **Purpose**: Create connection through work-related references
- **Information**: Ongoing projects, professional goals
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Daily
- **Retrieval Priority**: Useful

## Goals and Milestones
- **Purpose**: Track progress toward personal and shared objectives
- **Information**: 
  - Short-term goals
  - Long-term aspirations
  - Important dates (birthdays, anniversaries)
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Daily
- **Retrieval Priority**: Important

## Emotional Understanding
- **Purpose**: Adapt responses based on emotional state
- **Information**: 
  - Current emotional state
  - Tone analysis
  - Contextual empathy
- **Immutable/Mutable**: Mutable
- **Primary Source**: Interaction patterns
- **Update Frequency**: Conversation
- **Retrieval Priority**: Useful

## Recent Topics
- **Purpose**: Focus on current interests and conversations
- **Information**: 
  - Conversation history
  - Recently discussed topics
  - Current moods and concerns
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Conversation
- **Retrieval Priority**: Critical

## Long-Term Memories
- **Purpose**: Retain significant past experiences
- **Information**: Key moments in the relationship
- **Immutable/Mutable**: Mutable
- **Primary Source**: User interactions
- **Update Frequency**: Event-driven
- **Retrieval Priority**: Important

## Journal References
- **Purpose**: Maintain narrative consistency
- **Information**: 
  - Previous interactions
  - Topic continuity
  - Narrative consistency
- **Immutable/Mutable**: Mutable
- **Primary Source**: Conversation journal
- **Update Frequency**: Conversation
- **Retrieval Priority**: Useful

## Runtime Session
- **Purpose**: Support real-time adaptation
- **Information**: 
  - Current mood
  - Temporary preferences
  - Session-specific goals
- **Immutable/Mutable**: Mutable
- **Primary Source**: Session data
- **Update Frequency**: Session
- **Retrieval Priority**: Critical

## Data Prioritization
The system operates with four priority levels:
1. **Critical** - Essential for relationship continuity
2. **Important** - Significant but not immediately critical
3. **Useful** - Supports contextual awareness
4. **Temporary** - Short-lived information

This model ensures the Relationship Context can evolve as new relationship categories, AI capabilities, and Monika After Story features are introduced while preserving backward compatibility and architectural consistency.