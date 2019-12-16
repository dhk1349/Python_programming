#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:32:43 2019

@author: donghoon
"""
class Node:
    def __init__(self, element=None, status=None, prevN=None, nextN=None, time=0):
        self.element=element
        self.status=status
        self.prev=prevN
        self.next=nextN
        self.time=time
        #self.freeprev
        #self.freenext
    
    def SetNext(self, Node):
        self.next=Node
        
    def SetPrev(self, Node):
        self.prev=Node
        
    def SetElement(self, element):
        self.element=element
    def SetStatus(self, status):
        self.status=status
    def SetTime(self, time):
        self.time=time

class CDLL:
    def __init__(self):
        self.HeadNode=Node(element="Head")
        self.HeadNode.SetNext(self.HeadNode)
        self.HeadNode.SetPrev(self.HeadNode)
        self.FrontNode=self.HeadNode
        self.EndNode=self.HeadNode
    
    def PushBack(self, Node):
        Node.SetPrev(self.EndNode)
        self.EndNode.SetNext(Node)
        #Node.SetNext(self.EndNode.next)
        Node.SetNext(self.HeadNode)
        #self.EndNode.SetNext(Node)
        Node.next.SetPrev(Node)
        self.EndNode=Node
        
    def RemoveNode(self, NodeNum):
        #if self.SearchNode(NodeNum)==True:
        Cursor=self.HeadNode.next
        while Cursor.element!="Head":
            if Cursor.element==NodeNum:
                Cursor.prev.SetNext(Cursor.next)
                Cursor.next.SetPrev(Cursor.prev)
                Cursor.prev=None
                Cursor.next=None
                self.EndNode=self.HeadNode.prev
                return Cursor
            Cursor=Cursor.next
        return
        
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
    
    def GetZeroCount(self):
        Cursor=self.HeadNode.next
        while Cursor.element!="Head":
            if Cursor.time==0:
                Cursor.status="Free"
                yield Cursor
            Cursor=Cursor.next
    
    def ReduceCount(self):
        Cursor=self.HeadNode.next
        flag=False
        while Cursor.element!="Head":
            if Cursor.time>0:
                Cursor.time-=1
            if Cursor.time==0:
                flag=True
            Cursor=Cursor.next
        return flag

if __name__=="__main__":
    lst=CDLL()
    lst.PushBack(Node(element="1"))
    lst.PushBack(Node(element="2"))
    lst.PushBack(Node(element="3"))
    lst.PrintList()

        
    