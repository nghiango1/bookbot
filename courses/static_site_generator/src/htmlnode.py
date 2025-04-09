from typing import Dict, List, Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children=None,
        props: Optional[Dict[str, str]] = None,
    ):
        # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.tag = tag
        # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.value = value

        if children is not None:
            assert isinstance(children, List)
            for c in children:
                assert isinstance(c, HTMLNode)
        # A list of HTMLNode objects representing the children of this node
        self.children: Optional[List[HTMLNode]] = children

        # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        res = ""
        for key in self.props:
            res += f' {key}="{self.props[key]}"'

        return res

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
