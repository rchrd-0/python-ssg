from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text

        if not isinstance(text_type, TextType):
            raise TypeError(f"Invalid text_type: {text_type}")

        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{type(self).__name__}({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html(text_node):
    match text_node.text_type:
        case TextType.text:
            return LeafNode(None, text_node.text)
        case TextType.bold:
            return LeafNode("b", text_node.text)
        case TextType.italic:
            return LeafNode("i", text_node.text)
        case TextType.code:
            return LeafNode("code", text_node.text)
        case TextType.link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid text_type")
