class PromptBuilder:
    def build(
        self,
        relationship_context,
        conversation_context
    ) -> str:
        """Serialize context objects into a deterministic prompt with fixed section order."""
        # Relationship Context sections
        relationship = str(relationship_context.relationship)
        player = str(relationship_context.player)
        preferences = str(relationship_context.preferences)
        interests = str(relationship_context.interests)
        goals = str(relationship_context.goals)
        emotions = str(relationship_context.emotions)
        recent_topics = str(relationship_context.recent_topics)
        memories = str(relationship_context.memories)
        journal = str(relationship_context.journal)
        runtime = str(relationship_context.runtime)
        metadata = str(relationship_context.metadata)
        
        # Conversation Context sections
        active_topic = str(conversation_context.active_topic)
        recent_messages = str(conversation_context.recent_messages)
        open_questions = str(conversation_context.open_questions)
        conversation_goals = str(conversation_context.goals)
        conversation_runtime = str(conversation_context.runtime)
        conversation_metadata = str(conversation_context.metadata)
        
        # Construct the prompt with fixed section order
        prompt = (
            f"Relationship Context\n"
            f"relationship: {relationship}\n"
            f"player: {player}\n"
            f"preferences: {preferences}\n"
            f"interests: {interests}\n"
            f"goals: {goals}\n"
            f"emotions: {emotions}\n"
            f"recent_topics: {recent_topics}\n"
            f"memories: {memories}\n"
            f"journal: {journal}\n"
            f"runtime: {runtime}\n"
            f"metadata: {metadata}\n"
            f"\n"
            f"Conversation Context\n"
            f"active_topic: {active_topic}\n"
            f"recent_messages: {recent_messages}\n"
            f"open_questions: {open_questions}\n"
            f"goals: {conversation_goals}\n"
            f"runtime: {conversation_runtime}\n"
            f"metadata: {conversation_metadata}"
        )
        
        return prompt