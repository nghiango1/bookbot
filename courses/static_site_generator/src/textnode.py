from enum import Enum
from typing import Optional


class TextType(Enum):
    NORMAL = "normal"  # Normal text
    BOLD = "bold"  # **Bold text**
    ITALIC_ = "italic"  # _Italic text_
    CODE = "code"  # `Code text`
    LINKS = "link"  # Links, in this format: [anchor text](url)
    IMAGES = "images"  # Images, in this format: ![alt text](url)


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        # The text content of the node
        self.text = text

        # The type of text this node contains, which is a member of the TextType enum.
        self.text_type = text_type

        # The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
