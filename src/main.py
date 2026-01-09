from textnode import TextNode, TextType

def main():
    node1 = TextNode("I am an air bender", TextType.ITALIC)
    node2 = TextNode("I am a water bender", TextType.LINK, url="http://waterbending.com")
    
    print(node1)
    print(node2)

main()