import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_init(self):
        exception = None
        try:
            node = LeafNode(None, None)
        except Exception as e:
            exception = e
        assert exception is not None, "Still able to create LeafNode without Value"

        node = LeafNode(None, "Value_Mock")
        assert isinstance(node, LeafNode), "Can't set tag to be None"

    def test_to_html(self):
        node = LeafNode(None, "Value_Mock")
        node.value = None  # Force node.value to be None

        exception = None
        try:
            node.to_html()
        except ValueError as e:
            exception = e
        except Exception as e:
            print("Got expected error")
            raise e
        assert exception is not None, "node.to_html() mustnot work with node.value None"


if __name__ == "__main__":
    unittest.main()
