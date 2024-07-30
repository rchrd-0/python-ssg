def markdown_to_blocks(markdown: str) -> list[str]:
    md_split = markdown.split("\n\n")
    result = [split.strip() for split in md_split if split != ""]
    # for split in md_split:
    #     if split != "":
    #         result.append(split.strip())

    return result
