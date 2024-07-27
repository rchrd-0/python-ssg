class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
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
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All LeafNodes must have a value")
        if self.tag is None:
            return self.value

        void_elements = ["img", "br", "hr", "embed", "input", "link", "meta"]
        if self.tag in void_elements:
            return f"<{self.tag}{self.props_to_html()} />{self.value}"

        tags = [f"<{self.tag}{self.props_to_html()}>", f"</{self.tag}>"]
        return self.value.join(tags)
