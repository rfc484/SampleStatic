from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if part and i%2  == 1:
                new_nodes.append(TextNode(part, text_type))
            if part and i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT)) 
    return new_nodes

def extract_markdown_images(text):
    # images
    img_re = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    images = re.findall(img_re, text)
    return images

def extract_markdown_links(text):
    # regular links
    link_re = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links = re.findall(link_re, text)
    return links

def split_nodes_image(old_nodes):
    return list(map(split_node_image,old_nodes))

def split_node_image(node):
    img_re = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    parts = re.split(img_re, node.text)
    new_nodes = []
    alt_text = None
    url = None
    for i in range(len(parts)):
        part = parts[i]
        if not part:
            continue
        if i % 3  == 0:
            new_nodes.append(TextNode(part, TextType.TEXT))
        elif i % 3 == 1 and len(parts) >= i + 2:
            alt_text = part
        elif i % 3 == 2:
            url = part
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url)) 
            alt_text = None
            url = None
        else:
            raise Exception("invalid image format")
    return new_nodes

def split_nodes_link(old_nodes):
    return list(map(split_node_link,old_nodes))


def split_node_link(node):
    link_re = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    parts = re.split(link_re, node.text)
    new_nodes = []
    alt_text = None
    url = None
    for i in range(len(parts)):
        part = parts[i]
        if not part:
            continue
        if i % 3  == 0:
            new_nodes.append(TextNode(part, TextType.TEXT))
        elif i % 3 == 1 and len(parts) >= i + 2:
            alt_text = part
        elif i % 3 == 2:
            url = part
            new_nodes.append(TextNode(alt_text, TextType.LINK, url)) 
            alt_text = None
            url = None
        else:
            raise Exception("invalid link format")
    return new_nodes 

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes)
    return nodes    

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))

main()