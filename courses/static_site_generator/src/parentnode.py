from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props=None):
        super(ParentNode, self).__init__(tag, None, children, props)
        assert self.children, f"Children can't be missing, got {self.children}"
        assert isinstance(
            self.children, list
        ), f"Children need to be a list[HTMLNode], got {type(self.children).__name__}"

        for node in self.children:
            assert isinstance(
                node, HTMLNode
            ), f"Children must be HTMLNode, got {node} with type {type(node).__name__}"

        assert self.tag is not None, "Tag can't be None"

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        for node in self.children:
            if not isinstance(node, HTMLNode):
                raise ValueError("invalid HTML: children isn't valid HTML node")
        inner_html = "".join(map(lambda x: x.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
