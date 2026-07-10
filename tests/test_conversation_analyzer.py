import unittest
from core.conversation_analyzer import ConversationAnalyzer
from core.conversation_context import ConversationContext

class TestConversationAnalyzer(unittest.TestCase):
    def setUp(self):
        """Create shared test fixtures"""
        self.messages = ["Hello", "World"]
        self.runtime = {"timestamp": "2026-07-08"}
        self.metadata = {"source": "test"}
        self.analyzer = ConversationAnalyzer()

    def test_can_instantiate_conversation_analyzer(self):
        """Verify ConversationAnalyzer can be instantiated"""
        self.assertIsInstance(self.analyzer, ConversationAnalyzer)

    def test_analyze_returns_conversation_context(self):
        """Verify analyze() returns a ConversationContext"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertIsInstance(result, ConversationContext)

    def test_recent_messages_are_preserved(self):
        """Verify recent_messages in the returned ConversationContext matches the input messages"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertEqual(result.recent_messages, self.messages)
    def test_runtime_is_preserved(self):
        """Verify runtime is preserved in the returned ConversationContext"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertEqual(result.runtime, self.runtime)

    def test_metadata_is_preserved(self):
        """Verify metadata is preserved in the returned ConversationContext"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertEqual(result.metadata, self.metadata)

    def test_active_topic_defaults_empty(self):
        """Verify active_topic is empty by default"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertEqual(result.active_topic, {})

    def test_open_questions_default_empty(self):
        """Verify open_questions is empty by default"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertEqual(result.open_questions, {})

    def test_goals_default_empty(self):
        """Verify goals is empty by default"""
        result = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )
        self.assertEqual(result.goals, {})

    def test_analyze_is_deterministic(self):
        """Verify analyze() produces identical output for identical input"""
        result1 = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )

        result2 = self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )

        self.assertEqual(result1, result2)

    def test_analyze_does_not_modify_input_messages(self):
        """Verify analyze() does not modify the input messages"""
        original_messages = self.messages.copy()

        self.analyzer.analyze(
            self.messages,
            runtime=self.runtime,
            metadata=self.metadata
        )

        self.assertEqual(self.messages, original_messages)