from enum import Enum


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    md_split = markdown.split("\n\n")
    result = [split.strip() for split in md_split if split != ""]
    # result = []
    # for split in md_split:
    #     if split != "":
    #         result.append(split.strip())

    return result


def block_to_block_type(markdown: str) -> str:
    split_lines = markdown.split("\n")
    if (
        markdown.startswith("# ")
        or markdown.startswith("## ")
        or markdown.startswith("### ")
        or markdown.startswith("### ")
        or markdown.startswith("#### ")
        or markdown.startswith("##### ")
        or markdown.startswith("###### ")
    ):
        return BlockType.heading.value

    if len(split_lines) > 1 and markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.code.value

    if all(line.startswith(">") for line in split_lines):
        return BlockType.quote.value

    if all(line.startswith("* ") or line.startswith("- ") for line in split_lines):
        return BlockType.unordered_list.value

    if all(
        line.startswith(f"{index}. ") for index, line in enumerate(split_lines, start=1)
    ):
        return BlockType.ordered_list.value

    return BlockType.paragraph.value
