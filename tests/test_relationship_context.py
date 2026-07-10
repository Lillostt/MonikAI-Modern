import unittest
from core.relationship_context import RelationshipContext

class TestRelationshipContext(unittest.TestCase):
    def test_instantiation(self):
        context = RelationshipContext()
        self.assertIsInstance(context, RelationshipContext)

    def test_default_fields(self):
        context = RelationshipContext()
        self.assertIsInstance(context.relationship, dict)
        self.assertEqual(context.relationship, {})
        self.assertEqual(context.player, {})
        self.assertEqual(context.preferences, {})
        self.assertEqual(context.interests, {})
        self.assertEqual(context.goals, {})
        self.assertEqual(context.emotions, {})
        self.assertEqual(context.recent_topics, {})
        self.assertEqual(context.memories, {})
        self.assertEqual(context.journal, {})
        self.assertEqual(context.runtime, {})
        self.assertEqual(context.metadata, {})

    def test_metadata_defaults(self):
        context = RelationshipContext()
        self.assertIsInstance(context.metadata, dict)
        self.assertEqual(context.metadata, {})

    def test_immutable_defaults(self):
        context1 = RelationshipContext()
        context2 = RelationshipContext()
        self.assertIsNot(context1.relationship, context2.relationship)
        self.assertIsNot(context1.metadata, context2.metadata)