import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        for test_type in TextType:
            node = TextNode(f"This is a {test_type.value} node", test_type)
            node2 = TextNode(f"This is a {test_type.value} node", test_type)
            self.assertEqual(node, node2)

    def test_neq(self):
        # Not the right class
        for test_type in TextType:
            node = TextNode(f"This is a {test_type.value} node", test_type)
            not_a_node = "This is just text"
            self.assertNotEqual(node, not_a_node)

        # Not the same type
        for test_type in TextType:
            for test_type_2 in TextType:
                if test_type == test_type_2:
                    continue
                node = TextNode("This is a node", test_type)
                node2 = TextNode("This is a node", test_type_2)
                self.assertNotEqual(node, node2)

        # Not the same text
        for test_type in TextType:
            node = TextNode(f"This is a {test_type.value} node", test_type)
            node2 = TextNode(f"This is a {test_type.value} node 2", test_type)
            self.assertNotEqual(node, node2)

        # Not the same url, check if default url eq None
        for test_type in [TextType.LINKS, TextType.IMAGES]:
            node = TextNode(
                f"This is a {test_type.value} node", test_type, "file://not-existed"
            )
            node2 = TextNode(f"This is a {test_type.value} node", test_type)
            self.assertEqual(node2.url, None)
            self.assertNotEqual(node.url, None)
            self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

        node = TextNode("This is a image node", TextType.IMAGES, "public/hello.png")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertNotEqual(html_node.props, None)
        assert html_node.props is not None
        self.assertDictEqual(
            html_node.props,
            {"alt": "This is a image node", "src": "public/hello.png"},
        )

        node = TextNode("This is a link node", TextType.LINKS, "#")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertNotEqual(html_node.props, None)
        assert html_node.props is not None
        self.assertDictEqual(
            html_node.props,
            {"href": "#"},
        )

        node = TextNode("This is a code node", TextType.CODE)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")


if __name__ == "__main__":
    unittest.main()
