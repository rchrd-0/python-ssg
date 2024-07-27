from typing import TypeVar

VOID_ELEMENTS = {"img", "br", "hr", "embed", "input", "link", "meta"}
T = TypeVar("T", bound="HTMLNode")


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[T] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        attributes = ""
        for key, value in self.props.items():
            attributes += f' {key}="{value}"'
        return attributes

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag is None:
            return self.value

        if self.tag in VOID_ELEMENTS:
            return f"<{self.tag}{self.props_to_html()} />{self.value}"

        tags = [f"<{self.tag}{self.props_to_html()}>", f"</{self.tag}>"]
        return self.value.join(tags)


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[T],
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        # really should be doing these in the constructor

        parent_tags = [
            f"<{self.tag}{self.props_to_html()}>",
            f"</{self.tag}>",
        ]

        children_html = "".join([child.to_html() for child in self.children])

        return children_html.join(parent_tags)
