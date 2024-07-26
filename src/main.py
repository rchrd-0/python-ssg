from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    text_node_0 = TextNode("text", TextType.bold)
    print(text_node_0)

    # html_node_0 = HTMLNode("p", "paragraph value", props={
    #     "href": "https://rchrd.co",
    #     "target": "_blank"
    # })
    # print(html_node_0)


main()
