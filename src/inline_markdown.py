import re
from functools import reduce
from typing import Callable

from textnode import TextNode, TextType


# parse bold, italic and code text based on markdown delimiters
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


def create_delimiter_splitter(delimiter: str, text_type: TextType) -> Callable:
    def splitter(nodes: list[TextNode]) -> list[TextNode]:
        return split_nodes_delimiter(nodes, delimiter, text_type)

    return splitter


split_bold = create_delimiter_splitter("**", TextType.bold)
split_italic = create_delimiter_splitter("*", TextType.italic)
split_code = create_delimiter_splitter("`", TextType.code)


def apply_delimiter_splitters(
    nodes: list[TextNode], splitters: list[Callable]
) -> list[TextNode]:
    return reduce(lambda acc, splitter: splitter(acc), splitters, nodes)


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


# def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
#     result_nodes = []
#
#     for node in old_nodes:
#         if node.text_type != TextType.text:
#             result_nodes.append(node)
#             continue
#
#         splits = re.split(r"(!\[.*?\]\(.*?\))", node.text)
#
#         for content in splits:
#             if content == "":
#                 continue
#             images = extract_markdown_images(content)
#             if not images:
#                 result_nodes.append(TextNode(content, TextType.text))
#             else:
#                 result_nodes.extend(
#                     TextNode(text, TextType.image, url) for text, url in images
#                 )
#
#     return result_nodes


# def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
#     result_nodes = []
#
#     for node in old_nodes:
#         if node.text_type != TextType.text:
#             result_nodes.append(node)
#             continue
#
#         splits = re.split(r"(\[.*?\]\(.*?\))", node.text)
#
#         # for content in splits:
#         #     if content == "":
#         #         continue
#         #     links = extract_markdown_links(content)
#         #     if not links:
#         #         result_nodes.append(TextNode(content, TextType.text))
#         #     else:
#         #         result_nodes.extend(
#         #             TextNode(text, TextType.link, url) for text, url in links
#         #         )
#
#         for content in splits:
#             if content == "":
#                 continue
#             links = extract_markdown_links(content)
#             if not links:
#                 result_nodes.append(TextNode(content, TextType.text))
#             else:
#                 result_nodes.extend(
#                     TextNode(text, TextType.link, url) for text, url in links
#                 )
#
#     return result_nodes


def split_nodes_image_links(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.text:
            result_nodes.append(node)
            continue

        splits = re.split(r"(!?\[.*?\]\(.*?\))", node.text)

        for content in splits:
            if content == "":
                continue
            if content.startswith("!"):
                images = extract_markdown_images(content)
                result_nodes.extend(
                    TextNode(text, TextType.image, url) for text, url in images
                )
            elif content.startswith("["):
                links = extract_markdown_links(content)
                result_nodes.extend(
                    TextNode(text, TextType.link, url) for text, url in links
                )
            else:
                result_nodes.append(TextNode(content, TextType.text))

    return result_nodes


def text_to_textnodes(text: str) -> list["TextNode"]:
    base_node = TextNode(text, TextType.text)
    splitters = [
        split_bold,
        split_italic,
        split_code,
        split_nodes_image_links,
        # split_nodes_image,
        # split_nodes_link,
    ]
    split_nodes = apply_delimiter_splitters([base_node], splitters)
    return split_nodes
