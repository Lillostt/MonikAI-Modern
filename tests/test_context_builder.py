import unittest

from core.context_builder import ContextBuilder
from core.relationship_context import RelationshipContext


class TestContextBuilder(unittest.TestCase):

    def test_build_returns_relationship_context(self):
        builder = ContextBuilder()
        context = builder.build()

        self.assertIsInstance(context, RelationshipContext)

    def test_metadata_exists_and_is_dict(self):
        builder = ContextBuilder()
        context = builder.build()

        self.assertIsInstance(context.metadata, dict)

    def test_schema_version_is_1(self):
        builder = ContextBuilder()
        context = builder.build()

        self.assertEqual(context.metadata["schema_version"], 1)

    def test_required_metadata_keys_exist(self):
        builder = ContextBuilder()
        context = builder.build()

        self.assertIn("schema_version", context.metadata)
        self.assertIn("created_at", context.metadata)
        self.assertIn("context_id", context.metadata)