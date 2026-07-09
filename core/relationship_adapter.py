class RelationshipAdapter:
    def adapt(
        self,
        relationship_context,
        conversation_context
    ) -> "RelationshipContext":
        """Adapt relationship context using conversation context data.
        
        Returns the existing RelationshipContext instance unchanged.
        """
        return relationship_context