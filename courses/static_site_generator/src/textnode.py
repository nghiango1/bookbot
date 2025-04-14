from enum import Enum
from typing import Optional
from leafnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"  # Normal text
    BOLD = "bold"  # **Bold text**
    ITALIC = "italic"  # _Italic text_
    CODE = "code"  # `Code text`
    LINKS = "link"  # Links, in this format: [anchor text](url)
    IMAGES = "images"  # Images, in this format: ![alt text](url)


class TextNode:
    @staticmethod
    def text_node_to_html_node(textnode):
        if not isinstance(textnode, TextNode):
            raise ValueError(f"Not valid TextNode, got {textnode}")
        match textnode.text_type:
            case TextType.BOLD:
                return LeafNode("b", textnode.text)
            case TextType.ITALIC:
                return LeafNode("i", textnode.text)
            case TextType.CODE:
                return LeafNode("code", textnode.text)
            case TextType.LINKS:
                props = None
                if textnode.url:
                    props = {"href": textnode.url}
                return LeafNode("a", textnode.text, props)
            case TextType.IMAGES:
                props = {"alt": textnode.text}
                if textnode.url:
                    props["src"] = textnode.url
                return LeafNode("img", "", props)
            case TextType.NORMAL:
                return LeafNode(None, textnode.text)
            case _:
                raise ValueError(f"Not valid TextType, got {textnode.text_type}")

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
