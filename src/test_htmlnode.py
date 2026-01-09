import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag=None,
                        value=None,
                        children=None,
                        props={
                            "href": "https://www.google.com",
                            "target": "_blank",
                        }
        )
        propstext = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), propstext)
    


if __name__ == "__main__":
    unittest.main()