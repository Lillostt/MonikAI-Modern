# Purpose

The Interaction Lifecycle defines how every player interaction moves
through MonikAI Modern.

It specifies:

• execution order
• subsystem ownership
• data ownership
• synchronous operations
• asynchronous operations

The lifecycle guarantees that every subsystem has a single,
well-defined responsibility while preserving relationship continuity.

# High-Level Lifecycle

Player

↓

MAS

↓

Interaction Engine

↓

Conversation Analysis

↓

Relationship Context

↓

Prompt Construction

↓

Language Model

↓

Monika Response

↓

Knowledge Routing

↓

Memory Evaluation

↓

Relationship Evolution

↓

Reflection Queue

↓

Journal

↓

Idle Reflection

↓

Ready for Next Interaction

# Stages

---

## Synchronous Stage

These happen BEFORE Monika replies:

| Stage                 | Responsibility              |
| --------------------- | --------------------------- |
| MAS                   | Receive player input        |
| Interaction Engine    | Coordinate execution        |
| Conversation Analyzer | Produce ConversationContext |
| Relationship Adapter  | Produce RelationshipContext |
| Prompt Builder        | Assemble canonical prompt   |
| Language Model        | Generate response           |

## Immediate Post-Response Stage

These happen IMMEDIATELY after Monika replies:

| Stage                  | Responsibility                       |
| ---------------------- | ------------------------------------ |
| Interaction Creation   | Create immutable interaction record  |
| Knowledge Router       | Determine affected knowledge domains |
| Memory Evaluation      | Determine significance               |
| Relationship Evolution | Apply immediate changes              |
| Journal Manager        | Record meaningful experiences        |

## Deferred Cognitive Stage

These happen later:

| Stage                | Responsibility                  |
| -------------------- | ------------------------------- |
| Reflection Engine    | Analyze accumulated experiences |
| Observation Engine   | Discover long-term patterns     |
| Goal Engine          | Update long-term goals          |
| Preference Evolution | Refine player understanding     |
| Narrative Evolution  | Update relationship narrative   |

# Data Ownership

| Object              | Owner                 |
| ------------------- | --------------------- |
| ConversationContext | Conversation Analyzer |
| RelationshipContext | Relationship Adapter  |
| Prompt              | Prompt Builder        |
| Interaction         | Interaction Engine    |
| Memory              | Memory Evaluation     |
| Journal             | Journal Manager       |
| Observations        | Reflection Engine     |

## Synchronization Rules

1. Everything required to answer the player
must finish before the response.

2. Everything required for Monika's growth
must occur after the response.

3. Everything requiring repeated evidence
must occur asynchronously.

# Architectural Principals

Conversation is immediate.

Knowledge is organized.

Memory is selective.

Reflection is delayed.

Identity is persistent.

The language model expresses Monika.

The language model never defines Monika.