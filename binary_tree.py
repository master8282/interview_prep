#!/usr/bin/env python3

class Tree:
    # Made and playing with binary tree struct for interview peparation
    
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None
        self.level = dict()
                
    def add(self, i, node):
    # Adding new element "i" in existing bin tree struct "node"
        if not node.data:
            node.data = i
            return node
        
        elif node.data > i: 
            if node.left:
                self.add(i, node.left)
            else:
                node.left = Tree(i)    
        elif node.data < i: 
            if node.right:
                self.add(i, node.right)
            else:
                node.right = Tree(i)
        return node
        
    def new(self, k):
    # Makeing new bin tree struct from the list "k"
        if k:
            node = Tree(k[0])
            k = k[1:]
            
        for i in k:
            node = self.add(i, node)
        return node
    
    def level_print(self):
    # Just printing out dict struct that was made by "unpack" method
        for key in self.level:
            print(self.level[key])
    
    def unpack(self, t, c = 0):
    # Making dict struct where key is level num and val list of leaves
        if t:
            if c not in self.level:
                self.level[c] = list()
            self.level[c].append(t.data)
    
            if t.left:
                self.unpack(t.left, c + 1)
            if t.right:
                self.unpack(t.right, c + 1)
                
    def check(self, i, node, status = False):
    # Checking if value is in tree struct    
        if node:
            if node.data == i:
                return True
            elif node.data > i:
                status = self.check(i, node.left)
            elif node.data < i:
                status = self.check(i, node.right)
        return status
        

k = [6,4,67,99,81,5,17,28,32]
node = Tree().new(k)
node2 = Tree().add(81, node)
p = Tree()
p.unpack(node2)
p.level_print()
print(Tree().check(32, node2))
