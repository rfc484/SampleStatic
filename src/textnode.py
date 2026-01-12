from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"


class TextNode:
    def __init__(self, text: str, 
                 text_type: TextType,
                 url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def __eq__(self, value):
        if not isinstance(value, TextNode):
            return False
        return (self.text == value.text and 
                self.text_type == value.text_type and 
                self.url == value.url)
    
def text_node_to_html_node(text_node):
    from leafnode import LeafNode
    from parentnode import ParentNode

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")