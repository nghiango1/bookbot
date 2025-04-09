import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        example_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        expected_result = ' href="https://www.google.com" target="_blank"'
        html_node = HTMLNode(props=example_props)
        self.assertEqual(expected_result, html_node.props_to_html())


if __name__ == "__main__":
    unittest.main()
