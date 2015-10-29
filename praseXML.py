#encoding=utf-8
import xml.dom
from xml.dom import minidom
ELEMENT_NODE = xml.dom.Node.ELEMENT_NODE
TEXT_NODE = xml.dom.Node.TEXT_NODE

class Node:
    '''
    ' 节点对象
    '''
    def __init__(self, name):
        self.name = name    #节点名称
        self.value = None   #节点值
        self._attr={}       #节点属性
        self.childs = []    #节点子节点
        
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
    

def getNodesByName(root, name, nodes=[]):    
    '''
    ' 根据节点名称获取节点对象,
    ' root:一个节点对象
    ' name:查找的节点名称
    '''    
    if root.name == name:
        nodes.append(root)
    else:
        for item in root.childs:
            if item.name == name:
                nodes.append(item)
            else:
                getNodesByName(item, name, nodes)
    return nodes
            
        
class PraseXML:
    """
    " 解析Xml 文件
    """
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
            node = Node(elem.nodeName)    #实例化节点对象
            root.setChilds(node)
            for attr in elem._attrs:
                node.setAttr(attr, elem._attrs[attr].value)
            node.setValue(elem.firstChild.nodeValue)
            if elem.nodeType is ELEMENT_NODE:
                self.parseElement(node, elem)
            else:
                pass
                
class XmlToNode:
    '''
    ' 组合 XML 解析类与节点类
    '''
    def __init__(self, file):
        xmlObj = PraseXML(file)
        self.rootNode = Node(xmlObj.root.nodeName)
        xmlObj.parseElement(self.rootNode)
    
    def nodeObj(self):
        return self.rootNode
        
        
if __name__ == '__main__':
    node = XmlToNode('/home/yanheng/test/data.xml').nodeObj()
    s = getNodesByName(node, 'number')
    print s[1].value