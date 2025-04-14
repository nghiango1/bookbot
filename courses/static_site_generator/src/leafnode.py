from typing import Optional, Dict
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, tag: Optional[str], value: str, props: Optional[Dict[str, str]] = None
    ):
        super(LeafNode, self).__init__(tag, value, None, props)
        assert self.value is not None

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
