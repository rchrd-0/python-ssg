class HTMLNode:
    def __init__(self,
                 tag: str | None = None,
                 value: str | None = None,
                 children: list['HTMLNode'] | None = None,
                 props: dict[str, str] | None = None
                 ) -> None:
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
