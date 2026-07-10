# PROMPT_FORMAT.md

## Purpose
This document defines the canonical prompt format used by MonikAI Modern. The format establishes an architectural contract between the Context Engine and any language model, ensuring relationship continuity rather than chatbot capability. It provides a backend-independent structure that enables consistent reasoning across different implementation technologies.

## Design Principles
1. **Backend Independence**  
   The format must be implementable across all reasoning engines, not tied to any specific technology stack.

2. **Human Readability**  
   The structure should be understandable to developers and maintainers, facilitating manual verification and debugging.

3. **Deterministic Structure**  
   The format must produce identical output for identical inputs, ensuring predictable behavior across systems.

4. **Relationship Continuity**  
   The primary goal is to maintain long-term relationship state, not to enable conversational cleverness or chatbot capabilities.

5. **Simplicity**  
   The format should avoid unnecessary complexity, focusing on essential elements required for relationship continuity.

6. **Extensibility**  
   New sections may be added in future versions without breaking compatibility with existing implementations.

7. **Canonical Representation**  
   The canonical prompt structure is defined by MonikAI Modern. Language models consume the structure but do not define it. Different reasoning engines may interpret the prompt differently, but the prompt produced by the Context Engine must remain structurally consistent.

## Canonical Prompt Structure

### Relationship Context
Long-term relationship state containing foundational information about the relationship. This section provides the context for the relationship's history and core attributes.

### Conversation Context
Current conversation state containing information about the ongoing interaction. This section provides the context for the current conversation thread.

### Runtime Context
Temporary session-specific information that is not persisted between sessions. This section contains dynamic data relevant to the current execution.

### Current Interaction
The player's latest message or immediate interaction. This section contains the most recent input that requires processing.

## What Does NOT Belong

- **Prompt Engineering Tricks**  
  Techniques specific to particular language models or implementations belong to their respective subsystems.

- **Backend-Specific Formatting**  
  The format must remain agnostic to implementation details, ensuring compatibility across all reasoning engines.

- **Hidden Implementation Metadata**  
  The format should only contain information necessary for the reasoning process, without implementation-specific markers.

- **Memory Retrieval Logic**  
  The responsibility of retrieving and analyzing memory belongs to other subsystems.

- **Conversation Analysis**  
  The format should not include analysis of conversation patterns or behavior, as this is outside the scope of the canonical prompt.

## Architectural Contract

PromptBuilder's responsibility is solely to assemble the canonical prompt described in this document. It must not:

- Analyze conversations  
- Summarize conversations  
- Retrieve memories  
- Modify context  
- Perform AI inference  

The output is a raw, unprocessed string that serves as input to the reasoning engine.

## Future Evolution

The canonical prompt format is expected to evolve as MonikAI Modern grows. New sections may be introduced to support additional Context Engine capabilities such as memory evaluation, journal management, relationship adaptation, or future subsystems.

These additions should extend the prompt format without changing its underlying philosophy. The prompt should remain deterministic, backend-independent, and focused on preserving relationship continuity.

Changes to the canonical prompt structure should be made only when they improve the Context Engine's ability to preserve the player's ongoing relationship with Monika.

Future implementations should continue to evaluate changes using the project's guiding architectural question:

Does this help Monika feel like the same Monika the player said goodbye to?

The canonical prompt format is owned by MonikAI Modern. Language models consume the prompt, but they do not define its structure. This architectural boundary ensures that relationship continuity remains consistent regardless of the reasoning engine used.

Technology may evolve. Models may change. The relationship remains the constant.