from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.props:
            props_str = self.props_to_html()
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>" 
        return f"<{self.tag}>{"".join(map(lambda x: x.to_html(), self.children))}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
    