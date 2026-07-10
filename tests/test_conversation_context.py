import unittest
from core.conversation_context import ConversationContext

class TestConversationContext(unittest.TestCase):
    def test_instantiation(self):
        context = ConversationContext()
        self.assertIsInstance(context, ConversationContext)

    def test_default_fields(self):
        context = ConversationContext()
        self.assertIsInstance(context.active_topic, dict)
        self.assertEqual(context.active_topic, {})
        self.assertIsInstance(context.recent_messages, dict)
        self.assertEqual(context.recent_messages, {})
        self.assertIsInstance(context.open_questions, dict)
        self.assertEqual(context.open_questions, {})
        self.assertIsInstance(context.goals, dict)
        self.assertEqual(context.goals, {})
        self.assertIsInstance(context.runtime, dict)
        self.assertEqual(context.runtime, {})
        self.assertIsInstance(context.metadata, dict)
        self.assertEqual(context.metadata, {})

    def test_immutable_defaults(self):
        context1 = ConversationContext()
        context2 = ConversationContext()
        self.assertIsNot(context1.active_topic, context2.active_topic)
        self.assertIsNot(context1.metadata, context2.metadata)