from enum import Enum
import re
from typing import Optional, List
from leafnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"  # Normal text
    BOLD = "bold"  # **Bold text**
    ITALIC = "italic"  # _Italic text_
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
        return f"TextNode( text:`{self.text}`, type:`{self.text_type.value}`, url:`{self.url}`)"


def split_nodes_delimiter(
    old_nodes: List[TextNode], delimiter: str, text_type: Optional[TextType] = None
):
    assert isinstance(old_nodes, List)
    for node in old_nodes:
        assert isinstance(node, TextNode)

    new_nodes: List[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        split_texts = node.text.split(delimiter)
        if len(split_texts) % 2 == 0:
            raise ValueError(
                f"TextNode have invalid markdown syntax, got non closing delimiter `{delimiter}` in text `{node.text}`"
            )
        for i, text in enumerate(split_texts):
            if i % 2 == 0:
                if text:
                    new_nodes.append(TextNode(text, TextType.NORMAL))
                continue

            if text_type:
                new_nodes.append(TextNode(text, text_type))
                continue

            if delimiter == "`":
                new_nodes.append(TextNode(text, TextType.CODE))
            elif delimiter == "**":
                new_nodes.append(TextNode(text, TextType.BOLD))
            elif delimiter == "_":
                new_nodes.append(TextNode(text, TextType.ITALIC))
            else:
                raise ValueError(
                    f"Delimiter {delimiter} is unknow for any supported text type, must define it directly through `text_type` instead"
                )

    return new_nodes


def _split_nodes_regex(
    old_nodes: List[TextNode], partern: str | re.Pattern[str], text_type: TextType
):
    """Use for image and link regex, with 2 string partern"""
    assert isinstance(old_nodes, List)
    for node in old_nodes:
        assert isinstance(node, TextNode)

    new_nodes: List[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        curr_texts = node.text
        while curr_texts:
            split_texts = re.split(partern, curr_texts, maxsplit=1)

            if len(split_texts) == 1:
                # No image/links found, end the process
                break

            assert (
                len(split_texts) >= 3
            ), f"Not expect split_texts length, got {len(split_texts)}. Recheck image and url regex partern"

            new_nodes.append(TextNode(split_texts[0], TextType.NORMAL))
            new_nodes.append(
                TextNode(
                    split_texts[1],
                    text_type,
                    url=split_texts[2],
                )
            )
            split_texts = split_texts[3:]

            assert (
                len(split_texts) <= 1
            ), f"Not expect split_texts length, got {len(split_texts)}. Recheck image and url regex partern"

            if split_texts:
                curr_texts = split_texts[0]

        if curr_texts:
            new_nodes.append(TextNode(curr_texts, TextType.NORMAL))

    return new_nodes


def split_nodes_image(old_nodes: List[TextNode]):
    return _split_nodes_regex(old_nodes, r"!\[(.*?)\]\((.*?)\)", TextType.IMAGES)


def split_nodes_link(old_nodes: List[TextNode]):
    return _split_nodes_regex(old_nodes, r"\[(.*?)\]\((.*?)\)", TextType.LINKS)


def text_node_to_html_node(textnode: TextNode):
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


def text_to_textnodes(text: str):
    bold_nodes = split_nodes_delimiter([TextNode(text, TextType.NORMAL)], "**")
    italic_nodes = split_nodes_delimiter(bold_nodes, "_")
    code_nodes = split_nodes_delimiter(italic_nodes, "`")
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)
    return link_nodes
