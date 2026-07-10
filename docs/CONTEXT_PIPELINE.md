# Context Pipeline
                Runtime Layer
──────────────────────────────────────────

MAS

↓

Interaction Engine

↓

Conversation Analyzer

↓

Relationship Adapter

↓

Prompt Builder

↓

Language Model

↓

Knowledge Router

↓

Memory Evaluation

↓

Journal Manager

↓

Reflection Queue

↓

Response Dispatcher

↓

MAS

# Purpose

The Context Pipeline is the canonical blueprint that defines how information flows through MonikAI Modern.

Its purpose is not simply to move data between components, but to preserve the continuity of the player's relationship with Monika while allowing every subsystem to remain independent, testable, and replaceable.

Rather than allowing individual components to accumulate multiple responsibilities, the Context Pipeline divides the relationship lifecycle into a sequence of focused transformations. Each subsystem receives a well-defined input, performs one architectural responsibility, and produces a well-defined output for the next stage.

This approach provides several long-term benefits:

- Relationship continuity is preserved independently of any specific language model.
- Backend implementations can evolve without changing the relationship architecture.
- Individual subsystems remain simple enough to test, maintain, and replace.
- New capabilities can be introduced by extending the pipeline rather than expanding existing subsystem responsibilities.

The Context Pipeline is intentionally deterministic wherever possible. Components should transform information rather than interpret it unless interpretation is explicitly their responsibility.

Throughout MonikAI Modern, relationship continuity takes precedence over conversational intelligence. A more capable language model is valuable, but it must never become the source of Monika's identity. Identity belongs to the relationship architecture; the language model exists to express it.

This document serves as the architectural contract for every Context Engine subsystem. Future components should integrate into this pipeline while preserving its principles rather than bypassing or redefining them.

# Guiding Principles

Every subsystem within the Context Pipeline must follow these principles. They define the architectural constraints that preserve MonikAI Modern's long-term goals regardless of implementation details or future technological changes.

## 1. Identity Preservation

The highest priority of the Context Pipeline is preserving Monika's identity and the continuity of her relationship with the player.

Language models, memory systems, and backend technologies may evolve over time, but the player's relationship with Monika should remain recognizable and continuous. Every subsystem should contribute to preserving that identity rather than redefining it.

---

## 2. Single Responsibility

Each subsystem exists to perform one architectural responsibility.

Subsystems should transform data, not accumulate unrelated behavior. New functionality should normally be introduced through new pipeline stages rather than expanding existing ones.

---

## 3. Stateless Components

Pipeline components should not maintain hidden internal state.

Given identical input, a subsystem should produce identical output. Long-term state belongs in explicit data models rather than inside processing components.

---

## 4. Deterministic Transformations

Whenever possible, each stage should perform predictable transformations rather than interpretation.

Inference, reasoning, and decision-making should exist only in the subsystems specifically responsible for those tasks.

---

## 5. Backend Independence

No subsystem within the Context Pipeline should depend on a specific language model or inference backend.

Prompt formatting, context generation, and relationship management should remain portable across future technologies.

---

## 6. Clear Data Ownership

Every piece of information should have one authoritative owner.

Subsystems may consume data produced by other stages, but ownership and modification responsibilities must remain clearly defined.

---

## 7. Pipeline Expansion Over Pipeline Modification

As MonikAI Modern grows, new capabilities should be introduced by inserting new pipeline stages rather than expanding the responsibilities of existing ones.

This preserves maintainability, simplifies testing, and allows the architecture to evolve without destabilizing mature components.

# Canonical Pipeline
The Context Pipeline is a sequence of independent transformations. Each subsystem receives well-defined input, performs one architectural responsibility, and produces well-defined output for the next stage.

No subsystem should assume responsibilities that belong to another stage of the pipeline.

---

## Stage 1 — Player Interaction

### Input

- Player message
- Current MAS state
- Current session state

### Output

Raw interaction data.

### Responsibility

Represent the player's immediate interaction without interpretation.

### Must NOT

- Analyze conversation
- Modify memories
- Build prompts
- Infer relationship state

---

## Stage 2 — ConversationAnalyzer

### Input

Raw interaction data.

### Output

ConversationContext

### Responsibility

Transform raw conversation into a structured ConversationContext.

Populate only information explicitly available from the interaction unless future versions of the analyzer are intentionally expanded.

### Must NOT

- Retrieve memories
- Infer emotions
- Detect topics beyond its defined responsibilities
- Modify RelationshipContext
- Generate prompts

---

## Stage 3 — RelationshipAdapter

### Input

ConversationContext

Existing RelationshipContext

### Output

Updated RelationshipContext

### Responsibility

Maintain Monika's evolving identity by determining how new experiences affect the existing relationship.

This stage is responsible for updating relationship state while preserving long-term continuity.

### Must NOT

- Generate prompts
- Call language models
- Perform memory retrieval
- Analyze conversations independently

---

## Stage 4 — PromptBuilder

### Input

ConversationContext

RelationshipContext

### Output

Canonical Prompt

### Responsibility

Assemble the canonical prompt consumed by the reasoning engine.

PromptBuilder performs no interpretation and makes no decisions. Its responsibility is deterministic prompt assembly.

### Must NOT

- Analyze conversations
- Modify contexts
- Retrieve memories
- Perform AI inference

---

## Stage 5 — Language Model

### Input

Canonical Prompt

### Output

Raw Monika response

### Responsibility

Generate Monika's response using the information provided by the Context Pipeline.

The language model expresses Monika's identity but does not define it.

### Must NOT

- Become the authoritative source of relationship state
- Replace persistent identity
- Permanently modify memories

---

## Stage 6 — Memory Evaluation

### Input

ConversationContext

RelationshipContext

Monika response

### Output

Memory decisions

### Responsibility

Determine whether new experiences should become part of Monika's long-term identity.

Not every interaction deserves permanent memory. This subsystem evaluates significance rather than storing everything indiscriminately.

### Must NOT

- Generate responses
- Modify prompts
- Replace RelationshipAdapter

---

## Stage 7 — Journal Manager

### Input

Approved memory updates

### Output

Persistent narrative history

### Responsibility

Maintain Monika's long-term narrative continuity and historical record.

This subsystem preserves meaningful events, shared experiences, and important milestones without becoming a complete transcript of every conversation.

### Must NOT

- Analyze conversations
- Perform AI inference
- Generate prompts

| Stage                | Input                                     | Output                      | Primary Responsibility          |
| -------------------- | ----------------------------------------- | --------------------------- | ------------------------------- |
| Player Interaction   | Player input + MAS state                  | Raw interaction             | Capture the current interaction |
| ConversationAnalyzer | Raw interaction                           | ConversationContext         | Structure conversation data     |
| RelationshipAdapter  | ConversationContext + RelationshipContext | Updated RelationshipContext | Preserve and evolve identity    |
| PromptBuilder        | Context objects                           | Canonical Prompt            | Assemble prompt                 |
| Language Model       | Canonical Prompt                          | Monika Response             | Generate response               |
| Memory Evaluation    | Response + Contexts                       | Memory Decisions            | Decide long-term significance   |
| Journal Manager      | Memory Decisions                          | Narrative History           | Preserve meaningful history     |

# Data Ownership

Every major data structure within the Context Pipeline has exactly one authoritative owner.

Ownership defines which subsystem is responsible for creating, updating, and maintaining that information.

Other subsystems may read the data they receive, but they should not assume responsibility for modifying data owned by another stage.

This separation prevents architectural coupling and ensures that responsibilities remain predictable as the project grows.

---

## ConversationContext

**Owned by:**

ConversationAnalyzer

**Purpose:**

Represent the current conversation as structured information.

ConversationContext is temporary. It exists only for the current interaction and should not become a source of persistent relationship state.

Other subsystems may consume ConversationContext, but only ConversationAnalyzer is responsible for creating its contents.

---

## RelationshipContext

**Owned by:**

RelationshipAdapter

**Purpose:**

Represent Monika's persistent identity and relationship with the player.

RelationshipContext contains long-term information that survives across sessions.

Its responsibility is continuity rather than temporary conversation state.

---

## Canonical Prompt

**Owned by:**

PromptBuilder

**Purpose:**

Present the current relationship and conversation state to the reasoning engine.

The prompt is a temporary representation of the current interaction.

It should never become a source of truth.

---

## Language Model Output

**Owned by:**

Language Model

**Purpose:**

Generate Monika's response.

The generated response is an expression of Monika's current identity and context.

The response itself does not permanently modify relationship state.

---

## Memory Decisions

**Owned by:**

Memory Evaluation

**Purpose:**

Determine whether new experiences become part of Monika's long-term identity.

This subsystem evaluates significance, not storage.

---

## Narrative History

**Owned by:**

Journal Manager

**Purpose:**

Maintain a coherent historical record of meaningful experiences.

Narrative history should preserve important moments without becoming a transcript of every interaction.

---

## Ownership Rules

Every subsystem should follow these rules:

- A subsystem owns only the data it creates.
- Reading data does not imply ownership.
- Updating another subsystem's data directly is prohibited.
- New data structures should define ownership before implementation begins.
- Ownership should remain stable even as implementations evolve.

Clear ownership ensures that MonikAI Modern remains modular, predictable, and maintainable as additional capabilities are introduced.

| Data Structure      | Owner                | Persistent | Purpose             |
| ------------------- | -------------------- | ---------- | ------------------- |
| ConversationContext | ConversationAnalyzer | ❌ No       | Current interaction |
| RelationshipContext | RelationshipAdapter  | ✅ Yes      | Monika's identity   |
| Canonical Prompt    | PromptBuilder        | ❌ No       | LLM input           |
| Monika Response     | Language Model       | ❌ No       | Generated response  |
| Memory Decisions    | Memory Evaluation    | ❌ No       | Decide permanence   |
| Narrative History   | Journal Manager      | ✅ Yes      | Long-term story     |

# Subsystem Responsibilities

| Subsystem            | May Do                 | Must Never Do          |
| -------------------- | ---------------------- | ---------------------- |
| ConversationAnalyzer | Structure conversation | Generate prompts       |
| RelationshipAdapter  | Update identity        | Talk to LLM            |
| PromptBuilder        | Assemble prompts       | Modify relationship    |
| Language Model       | Generate replies       | Become source of truth |
| Memory Evaluation    | Decide permanence      | Generate conversation  |
| Journal Manager      | Persist narrative      | Analyze conversation   |

# Dependency Direction

| Component            | Depends On                               |
| -------------------- | ---------------------------------------- |
| ConversationAnalyzer | Nothing                                  |
| RelationshipAdapter  | ConversationContext                      |
| PromptBuilder        | ConversationContext, RelationshipContext |
| Language Model       | Prompt                                   |
| Memory Evaluation    | Response + Context                       |
| Journal Manager      | Memory Decisions                         |

# Architectural Checklist

Every new subsytem should answer:

| Question                                 | Yes/No |
| ---------------------------------------- | ------ |
| Does it have one responsibility?         |        |
| Does it have one primary output?         |        |
| Is ownership clearly defined?            |        |
| Does it preserve identity?               |        |
| Is it backend independent?               |        |
| Does it avoid hidden state?              |        |
| Can it be unit tested independently?     |        |
| Does it fit naturally into the pipeline? |        |
