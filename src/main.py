from textnode import TextNode, TextType, text_node_to_html
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import block_to_block_type


def main():
    heading_3 = "### heading 3"
    # print(block_to_block_type(heading_3))

    # quote_block = "> quote 1\n> quote 2"
    #
    # print(block_to_block_type(quote_block))

    unordered_block = "* hi\n- bye\n* hello"
    # print(block_to_block_type(unordered_block))

    ordered_block = "1. first\n2. second\n3. third\n4. fourth"
    ordered_block_false = "1. first\n3. second\n4. third\n4. fourth"
    print(block_to_block_type(ordered_block))
    print(block_to_block_type(ordered_block_false))


main()
