import unittest
from core.prompt_builder import PromptBuilder
from core.relationship_context import RelationshipContext
from core.conversation_context import ConversationContext

class TestPromptBuilder(unittest.TestCase):
    def setUp(self):
        """Create test fixtures for all tests"""
        self.relationship_data = {
            "relationship": "friend",
            "player": "Alice",
            "preferences": ["music"],
            "interests": ["reading"],
            "goals": ["write book"],
            "emotions": ["happy"],
            "recent_topics": ["AI"],
            "memories": ["past projects"],
            "journal": ["daily entries"],
            "runtime": "2026-07-08",
            "metadata": {"key": "value"}
        }
        self.conversation_data = {
            "active_topic": "AI ethics",
            "recent_messages": ["Hello", "How are you?"],
            "open_questions": ["What is AI ethics?"],
            "goals": ["discuss ethics"],
            "runtime": "2026-07-08",
            "metadata": {"key": "value"}
        }
        self.relationship = RelationshipContext(**self.relationship_data)
        self.conversation = ConversationContext(**self.conversation_data)
        self.builder = PromptBuilder()

    def test_can_instantiate_prompt_builder(self):
        """PromptBuilder can be instantiated with valid contexts"""
        self.assertIsInstance(self.builder, PromptBuilder)

    def test_build_returns_string(self):
        """build() returns a string"""
        result = self.builder.build(self.relationship, self.conversation)
        self.assertIsInstance(result, str)

    def test_contains_relationship_section(self):
        """Prompt contains 'Relationship Context' section"""
        result = self.builder.build(self.relationship, self.conversation)
        self.assertIn("Relationship Context", result)

    def test_contains_conversation_section(self):
        """Prompt contains 'Conversation Context' section"""
        result = self.builder.build(self.relationship, self.conversation)
        self.assertIn("Conversation Context", result)

    def test_relationship_before_conversation(self):
        """Relationship Context appears before Conversation Context"""
        result = self.builder.build(self.relationship, self.conversation)
        self.assertTrue(result.startswith("Relationship Context"))

    def test_relationship_fields_order(self):
        """Relationship fields appear in canonical order"""
        result = self.builder.build(self.relationship, self.conversation)
        relationship_section = result.split("Relationship Context")[1].split("Conversation Context")[0]
        expected_order = [
            "relationship", "player", "preferences", "interests",
            "goals", "emotions", "recent_topics", "memories",
            "journal", "runtime", "metadata"
        ]
        actual_order = [
            line.split(": ")[0] for line in 
            relationship_section.strip().split("\n")
        ]
        self.assertEqual(actual_order, expected_order)

    def test_conversation_fields_order(self):
        """Conversation fields appear in canonical order"""
        result = self.builder.build(self.relationship, self.conversation)
        conversation_section = result.split("Conversation Context")[1]
        expected_order = [
            "active_topic", "recent_messages", "open_questions",
            "goals", "runtime", "metadata"
        ]
        actual_order = [
            line.split(": ")[0] for line in 
            conversation_section.strip().split("\n")
        ]
        self.assertEqual(actual_order, expected_order)

    def test_build_is_deterministic(self):
        """build() is deterministic"""
        result1 = self.builder.build(self.relationship, self.conversation)
        result2 = self.builder.build(self.relationship, self.conversation)
        self.assertEqual(result1, result2)

    def test_build_does_not_mutate_contexts(self):
        """build() does not modify the context objects"""
        original_relationship = self.relationship_data.copy()
        original_conversation = self.conversation_data.copy()
        self.builder.build(self.relationship, self.conversation)
        self.assertEqual(self.relationship.__dict__, original_relationship)
        self.assertEqual(self.conversation.__dict__, original_conversation)