import unittest
from graph import SocialGraph

class TestSocialGraph(unittest.TestCase):
    def setUp(self):
        self.social_graph = SocialGraph()

    def test_add_user_valid(self):
        self.social_graph.add_user("Alice")
        self.assertEqual(len(self.social_graph), 1)

    def test_add_user_invalid(self):
        with self.assertRaises(ValueError):
            self.social_graph.add_user("")

    def test_remove_user_valid(self):
        self.social_graph.add_user("Alice")
        self.social_graph.remove_user("Alice")
        self.assertEqual(len(self.social_graph), 0)

    def test_remove_user_invalid(self):
        with self.assertRaises(ValueError):
            self.social_graph.remove_user("Bob")

    def test_add_relationship_invalid_users(self):
        with self.assertRaises(ValueError):
            self.social_graph.add_relationship("Alice", "Bob")

    def test_add_relationship_same_user(self):
        self.social_graph.add_user("Alice")
        with self.assertRaises(ValueError):
            self.social_graph.add_relationship("Alice", "Alice")

    def test_add_relationship_existing_relationship(self):
        self.social_graph.add_user("Alice")
        self.social_graph.add_user("Bob")
        self.social_graph.add_relationship("Alice", "Bob")
        with self.assertRaises(ValueError):
            self.social_graph.add_relationship("Alice", "Bob")


if __name__ == "__main__":
    unittest.main()
