#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:32:43 2019

@author: donghoon
"""
class Node:
    def __init__(self, element=None, status=None, prevN=None, nextN=None):
        self.element=element
        self.status=status
        self.prev=prevN
        self.next=nextN
        
    
    def SetNext(self, Node):
        self.next=Node
        
    def SetPrev(self, Node):
        self.prev=Node

class CDLL:
    def __init__(self):
        self.HeadNode=Node(element="Head")
        self.HeadNode.SetNext(self.HeadNode)
        self.HeadNode.SetPrev(self.HeadNode)
        self.FrontNode=self.HeadNode
        self.EndNode=self.HeadNode
    
    def PushBack(self, Node):
        Node.SetPrev(self.EndNode)
        Node.SetNext(self.EndNode.next)
        self.EndNode.SetNext(Node)
        Node.next.SetPrev(Node)
        self.EndNode=Node
        
    def RemoveNode(self, NodeNum):
        #if self.SearchNode(NodeNum)==True:
        Cursor=self.HeadNode.next
        #while Cursor.element!="Head":
        #    if 
        
    def PrintList(self):
        Cursor=self.HeadNode.next
        while Cursor.element!="Head":
            print (Cursor.element)
            Cursor=Cursor.next
    
    def SearchNode(self, NodeNum):
        Cursor=self.HeadNode.next
        while Cursor.element!="Head":
            if Cursor.element==NodeNum:
                return Cursor
            Cursor=Cursor.next
        return False


if __name__=="__main__":
    lst=CDLL()
    lst.PushBack(Node(element="1"))
    lst.PushBack(Node(element="2"))
    lst.PushBack(Node(element="3"))
    lst.PrintList()

        
    