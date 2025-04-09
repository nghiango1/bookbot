from enum import Enum


class TextType(Enum):
    NORMAL_TEXT = "normal_text"  # Normal text
    BOLD_TEXT = "bold_text"  # **Bold text**
    ITALIC_TEXT_ = "italic_text"  # _Italic text_
    CODE_TEXT = "code_text"  # `Code text`
    LINKS = "link"  # Links, in this format: [anchor text](url)
    IMAGES = "images"  # Images, in this format: ![alt text](url)


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str):
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
