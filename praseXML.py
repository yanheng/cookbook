#encoding=utf-8
import xml.dom
from xml.dom import minidom
ELEMENT_NODE = xml.dom.Node.ELEMENT_NODE
TEXT_NODE = xml.dom.Node.TEXT_NODE

class MyNode:
    '''
    ' xml 文件节点
    '''
    def __init__(self, name):
        self.name = name
        self.value = None
        self._attr={}
        self.childs = []
        
    def setChilds(self, node):
        self.childs.append(node)
        
    def getChilds(self):
        return self.childs;
    
    def setAttr(self, name, value):
        if name not in self._attr:
            self._attr[name] = value
    
    def getAttr(self, name):
        return self._attr.get(name,"")
    
    def setValue(self, val):
        self.value = val
        
    def getValue(self):
        return self.value
    
    def display(self):
        print "node name %s" % self.name
        print "node value %s " % self.value
        print "node attr %s" % unicode(self._attr)
        
    def displayAll(self):
        self.display()
        for child in self.childs:
            child.display()
            
def getNodesByName(node, name):
    '''
    ' 根据节点名称获取节点对象,
    '''
    nodes=[]
    if node.name == name:
        nodes.append(node)
    else:
        while len(node.childs) > 0:
            for n in node.childs:
                nodes.append(n)
            
    return nodes
        
        
class PraseXML:
    def __init__(self, file):
        self.root = minidom.parse(file).documentElement
        
    def parseElement(self, root, elem=None):
        if elem is None:
            elements = self.root.childNodes
        else:
            elements = elem.childNodes
        for elem in elements:
            if elem.nodeType is TEXT_NODE:
                continue
            node = MyNode(elem.nodeName)
            root.setChilds(node)
            for attr in elem._attrs:
                node.setAttr(attr, elem._attrs[attr].value)
            node.setValue(elem.firstChild.nodeValue)
            if elem.nodeType is ELEMENT_NODE:
                self.parseElement(node, elem)
        
if __name__ == '__main__':
    obj = PraseXML('/home/yanheng/test/data.xml')
    rootnode = MyNode(obj.root.nodeName)
    obj.parseElement(rootnode)
    #rootnode.displayAll()
#     xx = getNodesByName(rootnode, 'list')
    print rootnode.childs[1].getAttr("id")