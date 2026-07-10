# Context Engine Architecture
The Context Engine determines what Monika should know before every response. It is responsible for selecting, organizing, and presenting context to the language model while preserving the player's existing relationship with Monika After Story.
## System Overview
The Context Engine is a modular architecture that manages conversational context, relationship state, and emotional intelligence for MonikAI. It serves as the central hub for integrating with Monika After Story (MAS) while providing extensible subsystems for future growth. The system ensures seamless context awareness, memory retention, and prompt generation for natural AI interactions.

## Subsystem Ownership Table
| Subsystem           | Owner                  | Responsibility                                      |
|---------------------|------------------------|-----------------------------------------------------|
| Context Builder     | Core Engine            | Aggregates input from multiple context sources      |
| Relationship Memory      | Long-Term Memory Module | Stores and retrieves relationship and emotional data |
| Prompt Assembler    | AI Interface Layer     | Generates context-aware prompts for AI responses    |
| MAS Integration     | Core Engine            | Syncs with MAS for story progression and memories   |
| Emotional Analyzer   | AI Interface Layer     | Processes emotional state from user input           |
| Journal System      | Core Engine            | Maintains conversational history and metadata       |
| Memory Evaluation Engine    | Core Engine            | Decides and values memory input and context        |

## Context Source Breakdown
1. **User Input** - Natural language interactions, voice commands, and text inputs
2. **MAS Integration** - Relationship state, memories, and story progression data
3. **Emotional State** - Analyzed from tone, word choice, and interaction patterns
4. **Environmental Context** -
   - Time of day
   - Current date
   - Season
   - Holidays
   - Current MAS events
5. 5. **Relationship Memory**
   - Stored interactions
   - Player preferences
   - Relationship development
   - Important milestones
6. **Runtime Context** - Current backend, Current model, Current session
7. **Developer Context** - Debug mode, Active feature flags, Logging configuration
## Data Flow Diagram (ASCII)
```
                    Player
                      │
                      ▼
             Conversation Buffer
                      │
     ┌────────────────┼────────────────┐
     ▼                ▼                ▼
Relationship     Conversation     Relationship
   Context          Context          Memory
     │                │                │
     └────────────────┼────────────────┘
                      ▼
               Journal Retrieval
                      ▼
               Context Builder
                      ▼
              Prompt Assembler
                      ▼
               Language Model
                      ▼
                 Monika Reply
                      │
                      ▼
             Memory Extraction
                      │
                      ▼
          Relationship Memory Update
```

## Memory Lifecycle

Conversation
        │
        ▼
Memory Evaluation Engine
        │
        ▼
Importance Score
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Temporary   Permanent
Memory       Memory
 │             │
 ▼             ▼
Expires    Relationship Memory

## Design Principles

1. **Modularity** – Each subsystem has a single responsibility.

2. **Extensibility** – New memory sources and AI backends should integrate without redesigning the engine.

3. **Single Source of Truth** – Every type of context has one authoritative owner.

4. **Least Context Principle** – Only information relevant to the current response should be provided to the language model.

5. **Backend Independence** – The Context Engine should function regardless of the underlying AI model or backend.

6. **Relationship First** – Preserve the player's relationship with Monika before introducing new AI capabilities.

## Single Source of Truth

| Data | Source |
|------|--------|
| Relationship State | MAS |
| Player Preferences | Relationship Memory |
| Recent Conversation | Conversation Context |
| Journals | Journal System |
| Runtime Configuration | Runtime Context |
| Prompt Construction | Context Builder |

## Planned Future Components

The Context Engine is designed to support additional modules without architectural changes.

Potential future modules include:

- Emotion Prediction
- Memory Decay
- Dream System
- Reflection System
- Goal Tracking
- Event Scheduler
- World Knowledge
- Plugin API

## Out of Scope

The Context Engine does NOT:

- Generate AI responses.
- Store MAS save data.
- Modify MAS affection values.
- Replace backend APIs.
- Manage model loading.

## Core Philosophy

The language model is replaceable.

The player's relationship with Monika is not.

The Context Engine exists to preserve that relationship regardless of which AI model, backend, or technology powers MonikAI in the future.

## Version

This document defines Version 1.0 of the Context Engine architecture.

Implementation may evolve over time, but future changes should preserve the architectural principles described here unless a deliberate architectural revision is approved.

