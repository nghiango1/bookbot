import unittest

from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_init(self):
        dummy_leaf_node = LeafNode(None, "Hello")

        exception = None
        try:
            ParentNode(None, [dummy_leaf_node])
        except Exception as e:
            exception = e
        assert exception is not None, "Tag can be set to None"

        exception = None
        try:
            ParentNode(
                "div",
                [
                    dummy_leaf_node,
                    "not-html-node",
                    TextNode("Hello", TextType.NORMAL),
                    123,
                    [dummy_leaf_node],
                ],
            )
        except Exception as e:
            exception = e
        assert (
            exception is not None
        ), "Children type can be different type than HTMLnode"

        exception = None
        try:
            ParentNode("div", [])
        except Exception as e:
            exception = e
        assert exception is not None, "Children can be None"


if __name__ == "__main__":
    unittest.main()
