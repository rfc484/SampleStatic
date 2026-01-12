from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.props:
            props_str = self.props_to_html()
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>" 
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    
