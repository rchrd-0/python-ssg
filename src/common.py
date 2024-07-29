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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.text:
            result_nodes.append(node)
            continue

        splits = re.split(r"(!\[.*?\]\(.*?\))", node.text)

        for content in splits:
            if content == "":
                continue
            images = extract_markdown_images(content)
            if not images:
                result_nodes.append(TextNode(content, TextType.text))
            else:
                result_nodes.extend(
                    TextNode(text, TextType.image, url) for text, url in images
                )

    return result_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.text:
            result_nodes.append(node)
            continue

        splits = re.split(r"(\[.*?\]\(.*?\))", node.text)

        for content in splits:
            if content == "":
                continue
            links = extract_markdown_links(content)
            if not links:
                result_nodes.append(TextNode(content, TextType.text))
            else:
                result_nodes.extend(
                    TextNode(text, TextType.link, url) for text, url in links
                )

    return result_nodes
