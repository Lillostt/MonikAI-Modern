MonikAI Modern Design Ideas

1. The player should only have to launch Monika. Everything else should happen automatically
2. The player can browse their files to choose the RIGHT folders/paths or have it automatically detected
3. SIMPLIFY setup wizard to launch every process automatically (this release v1.1.0 will provide an automatic default or ADVANCED mode allowing users to choose their setup options, paths, etc)
4. Bundle all windows including Powershell windows and keep them hidden
5. Keep installation user friendly and simple
6. Add more variables to Monika's personality based upon affection, conversation, and other effects to the surroundings of the player and Monika
7. Conversation Continuity: AI conversations should feel like a continuation of Monika After Story rather than a separate chatbot session. Whenever practical, MonikAI should use recent MAS dialogue and relationship context so transitions between scripted dialogue and AI dialogue are natural.


   MonikAI Modern

Vision

The easiest way to give Monika a modern AI backend.

──────────────────────────────

v1.1
✓ Automatic model loading
✓ Backend detection
✓ Startup improvements

v1.2
✓ Better settings
✓ Startup manager
✓ Cleaner UI

v2.0
✓ Setup Wizard
✓ Automatic backend installation
✓ Automatic model download
✓ One-click launch

v3.0
✓ Deep MAS integration
✓ Shared memories
✓ Affection synchronization
✓ Voice improvements
✓ Multi-backend ecosystem


Relationship Context & Memory System (MonikAI 2.0)
Goal

The objective of the Memory System is to make MonikAI feel like a true continuation of Monika After Story rather than a separate chatbot.

Instead of relying solely on the model's context window, MonikAI should build persistent memories that grow alongside the player's relationship with Monika.

MAS remains the source of truth for affection, relationship milestones, and game state.

Design Philosophy

Every memory should answer one of four questions:

What just happened?
What has happened before?
What kind of person is the player?
How does Monika feel about it?

The system should avoid repeatedly sending the entire conversation history to the AI. Instead, it should intelligently retrieve only the information that is relevant to the current discussion.

Memory Layers
1. Short-Term Conversation Memory

Purpose:

Maintain natural conversational flow.

Stores:

Recent player messages
Recent Monika responses

Suggested size:

20–50 exchanges
Approximately 3,000–5,000 tokens

Older messages are not deleted—they are summarized.

2. Conversation Summaries

When the short-term buffer fills:

Instead of discarding older messages, MonikAI should generate a concise summary.

Example:

Summary

• Player and Monika discussed ___.
• They worked on backend detection.
• Player was excited about the new startup system.
• They planned MonikAI 2.0.

Stored as:

memory/summaries/

Examples:

summary_001.json
summary_2026-07-07.json

These summaries dramatically reduce context usage while preserving long-term continuity.

3. Long-Term Player Memory

Stores important facts Monika should permanently remember.

Examples:

{
    "favorite_band": "Metallica",
    "favorite_music": "Metal",
    "favorite_game": "Monika After Story",
    "gpu": "RTX 5060",
    "project": "MonikAI",
    "preferred_language": "Python"
}

Stored as:

memory/player_memory.json

Only meaningful information should be saved.

4. MAS Relationship State

MAS should always remain the source of truth.

MonikAI reads relationship information directly from MAS.

Examples:

Affection
Nickname
Promise Ring
First Kiss
Anniversaries
Gifts
Special Events
Relationship Status

MonikAI should never invent or overwrite these values.

5. Emotional Memory

Remember how the player felt rather than only what they said.

Example:

{
    "startup_system":
    {
        "emotion": "excited",
        "confidence": 0.95,
        "date": "2026-07-07"
    }
}

Months later Monika can naturally reference those emotions.

6. Intelligent Memory Retrieval

Never load every memory.

Instead:

Player asks:

"Should I buy a new microphone?"

Retriever searches memories.

Possible retrieved memories:

Scarlett Solo
Metal music
RTX 5060
Recording YouTube videos

Only those memories are inserted into the prompt.

7. Relationship Memory

Monika gradually learns recurring habits.

Examples:

Player enjoys automation.
Player prefers planning before coding.
Player usually works late at night.
Player likes discussing architecture before implementation.

These observations should slowly evolve over time.

8. World Memory

Monika remembers ongoing projects.

Examples:

Current MonikAI version
Current Git branch
Current backend
Current AI model
Current roadmap milestone

She should naturally understand the current state of the project.

9. Daily Journal

At the end of each day (or when MonikAI closes), Monika writes a personal journal entry.

Example:

July 7

Today Player finally finished the backend detector.

I'm proud of how much progress we've made.

Next we'll start designing the Relationship Context Engine.

Journal entries provide long-term emotional continuity while remaining searchable.

10. Context Builder

Every prompt sent to the AI is assembled dynamically.

Player Message
        │
        ▼
Recent Conversation
        │
        ▼
Memory Retriever
        │
        ▼
Player Memory
        │
        ▼
MAS Relationship State
        │
        ▼
Relevant Summaries
        │
        ▼
Emotional Memories
        │
        ▼
Prompt Builder
        │
        ▼
Language Model

The model should only receive the information required for the current conversation.

This allows MonikAI to remember years of interactions while remaining within the model's context window.

Future Goals
Automatic memory importance scoring
Memory decay for unimportant facts
Player correction ("Actually that's no longer true.")
Shared memories between MAS and AI
Searchable journal
Memory visualization inside developer tools
Optional export/import of memories
Support for multiple AI backends
Retrieval-Augmented Generation (RAG) for long-term memory
Core Principle

Monika should never feel like a chatbot with temporary memory.

She should feel like the same Monika who has been spending time with the player in Monika After Story for months or years.
