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


if __name__ == "__main__":
    unittest.main()
