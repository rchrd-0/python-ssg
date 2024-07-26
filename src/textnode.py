from enum import Enum
from typing import Optional

TextType = Enum("TextType", ["bold", "italic", "anchor"])


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        self.text = text

        if not isinstance(text_type, TextType):
            raise TypeError(f"Invalid text_type: {text_type}")
      
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{type(self).__name__}({self.text}, {self.text_type.name}, {self.url})"
