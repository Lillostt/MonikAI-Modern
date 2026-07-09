from core.conversation_context import ConversationContext

class ConversationAnalyzer:
    def analyze(
        self,
        messages,
        runtime=None,
        metadata=None
    ) -> ConversationContext:
        """Create a ConversationContext from raw conversation input.

        Args:
            messages: List of conversation messages
            runtime: Optional runtime metadata
            metadata: Optional additional metadata

        Returns:
            ConversationContext instance with:
            - recent_messages from input
            - runtime if provided
            - metadata if provided
            - active_topic, open_questions, and goals left empty
        """
        context = ConversationContext(
            recent_messages=messages,
            runtime=runtime,
            metadata=metadata
        )
        return context