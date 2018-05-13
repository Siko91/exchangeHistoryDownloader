import xml.dom.minidom

def keyToObj(k):
    return {
        "type":str(k.getAttribute("type")),
        "apikey":str(k.getAttribute("apikey")),
        "secret":str(k.getAttribute("secret"))
    }

def parseKeys(path):
    DOMTree = xml.dom.minidom.parse(path)
    dom = DOMTree.documentElement
    keys = dom.getElementsByTagName("key")
    result = []
    for k in keys:
        result.append(keyToObj(k))

    return result