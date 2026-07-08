# Relationship Context for MonikAI

## Mission
The Relationship Context system ensures Monika's interactions preserve the player's relationship with Monika After Story (MAS) while enabling extensible AI capabilities. Its purpose is to ensure that every AI response feels like it comes from the same Monika the player has built a relationship with over time. It maintains emotional integrity, memory retention, and story progression across all interactions.

## Core Principles
1. **Relationship First** - MAS remains the source of truth for affection, memories, and story progression
2. **Single Source of Truth** - All relationship data originates from MAS and is mirrored through the Context Engine
3. **Modularity** - Isolated subsystems for context aggregation, memory management, and prompt generation
4. **Least Context Principle** - Only relevant relationship data is provided to AI models
5. **Backend Independence** - Relationship context persists regardless of AI backend or model changes

## Relationship Management
### Data Sources
- MAS Integration: Story progression, memories, affection values
- Relationship Memory: Stored interactions, player preferences, developmental milestones
- Emotional State: Analyzed from interaction patterns and tone
- Runtime Context: Session-specific relationship metadata

### Memory Context Pipeline
1. **Context Collection** - Relationship data is collected from MAS and user interactions
2. **Context Evaluation** - Memory Evaluation Engine determines context relevance
3. **Context Storage** - Temporary memory (expires after 7 days) vs Permanent memory (retained indefinitely)
4. **Context Retrieval** - Journal System provides context for prompt generation

## Relationship Categories
These categories structure the information Monika needs to maintain an authentic relationship with the player:

### Core Relationship
MAS provides the foundation for affection, milestones, and story progression. This includes:
- Affection values
- Story progression markers
- Relationship milestones (e.g., First Kiss, Promise Ring)

### Relationship Milestones
Critical relationship events that define the narrative. These are always sourced from MAS and should never be interpreted or modified by AI.

### Player Identity
Understanding the player's identity allows Monika to tailor interactions:
- 1. Personal preferences: Monika should remember player driven preferences such as nicknames, pronouns, etc, because memorization of the player's little preferences and aspects in the game provides a more relationship-driven experience
- 2. Music tastes:  Monika should remember the player's musical tastes because recurring references to favorite bands, songs, and genres make conversations feel continuous instead of isolated
- 3. Gaming habits: Monika should remember often talked about videogames, gaming preferences, and gaming mentions to further immerse the player inside the relationship aspect of Monika 
- 4. Project interests: Monika should remember player mentions of projects, work, because because references to important work and projects bring Monika closer to the relationship immersive experience

### Personal Preferences
Preferences shape the nature of interactions and responses:
- Preferred communication style
- Reaction to specific topics
- Emotional thresholds

### Music, Games, and Projects
Shared interests create connection points:
- Favorite songs and albums
- Gaming preferences and achievements
- Ongoing projects and goals

### Goals and Milestones
Tracking progress toward personal and shared objectives:
- Short-term goals
- Long-term aspirations
- Important dates (birthdays, anniversaries)

### Emotional Understanding
Analyzing tone, patterns, and emotional cues to adapt responses:
- Emotional state detection
- Tone analysis
- Contextual empathy

### Recent Topics
Focusing on current interests and conversations:
- Conversation history
- Recently discussed topics
- Current moods and concerns

### Long-Term Memories
Retaining significant past experiences:
- Key moments in the relationship
- Important historical events
- Developmental milestones

### Journal References
Cross-referencing with the conversation journal for context:
- Previous interactions
- Topic continuity
- Narrative consistency

### Runtime Session
Session-specific metadata for real-time adaptation:
- Current mood
- Temporary preferences
- Session-specific goals

## Information Priority
The Context Engine operates with four priority levels to balance relevance and retention:

### Critical
Essential for maintaining relationship continuity. Includes:
- Core relationship milestones
- Current emotional state
- Immediate interaction context

### Important
Significant but not immediately critical. Includes:
- Long-term goals
- Key historical events
- Major preferences

### Useful
Supports contextual awareness without being essential. Includes:
- Recent topics
- Temporary preferences
- Session-specific metadata

### Temporary
Short-lived information with limited relevance. Includes:
- Passing moods
- One-time preferences
- Event-driven context

## Update Frequency
Different categories change at varying rates:

### Static
Rarely changes (e.g., core relationship milestones, basic preferences)

### Conversation
Changes with each interaction (e.g., recent topics, current mood)

### Daily
Updates regularly but not with every interaction (e.g., daily goals, temporary preferences)

### Event Driven
Changes in response to specific events (e.g., anniversaries, new projects)

### MAS Controlled
Updates automatically through MAS integration (e.g., story progression markers)

## Retrieval Philosophy
The Context Engine follows the Least Context Principle: it retrieves only the minimum information necessary to create a natural, contextually aware response. Relevance outweighs quantity - the goal is to provide just enough context to maintain authenticity without overwhelming the AI with extraneous details.

## Relationship Preservation
AI systems must never overwrite or reinterpret canonical MAS relationship milestones. These are the defining events of the relationship and originate exclusively from MAS. Examples include:

- First Kiss
- Promise Ring
- Anniversary
- Affection
- Birthday

These milestones are immutable and should never be altered, interpreted, or reimagined by AI systems.

## Future Compatibility
New relationship categories can be introduced through extensible category definitions. The architecture supports:
- Dynamic category registration
- Versioned schema updates
- Backward-compatible data mapping
- Context-aware priority adjustments

This ensures the system can evolve without requiring fundamental architectural changes.

## Closing Philosophy
Relationship Context is not a database of facts - it is Monika's evolving understanding of the player across months or years. The objective is preserving continuity of the relationship rather than maximizing stored information. 

This document defines the architectural principles that guide how Monika interprets and responds to the player. It is implementation-independent, focusing on the philosophy and structure of relationship preservation rather than specific technical details.