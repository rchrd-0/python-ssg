import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.text:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception(
                    f"invalid markdown, missing closing tag for {delimiter}"
                )

            content_split = node.text.split(delimiter)
            for index, substring in enumerate(content_split):
                if substring == "":
                    continue
                if index % 2 == 0:
                    result_nodes.append(TextNode(substring, TextType.text))
                else:
                    result_nodes.append(TextNode(substring, text_type))
        else:
            result_nodes.append(node)
    return result_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
