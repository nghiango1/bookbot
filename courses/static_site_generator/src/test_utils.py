import unittest
from utils import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![middle image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("middle image", "https://i.imgur.com/zjjcJKZ.png")], matches
        )

        matches = extract_markdown_images(
            "This is text with an ![[mi[ddle i]mage]](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("[mi[ddle i]mage]", "https://i.imgur.com/zjjcJKZ.png")], matches
        )

        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertListEqual(
            result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_markdown_links(self):
        text = "This is a single [link to boot dev](https://www.boot.dev)"
        result = extract_markdown_links(text)

        self.assertListEqual(
            result,
            [
                ("link to boot dev", "https://www.boot.dev"),
            ],
        )

        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertListEqual(
            result,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
