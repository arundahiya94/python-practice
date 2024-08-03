class Binary_Search_Tree:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Binary_Search_Tree(value)
            else:
                self.left.insert(value)

        if value > self.value:
            if self.right == None:
                self.right = Binary_Search_Tree(value)
            else:
                self.right.insert(value)


    def search(self, value):
        current = self
        found = False
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                found = True
                break             

        return found
            



var = Binary_Search_Tree(90)
var.insert(50)
var.insert(110)
var.insert(40)
var.insert(30)
var.insert(45)
var.insert(105)
var.insert(115)

print(var.search(105))
print(var.search(115))
