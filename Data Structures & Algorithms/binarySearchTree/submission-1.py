class TreeNode:
    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)

        if self.root == None:
            self.root = newNode
            return

        current = self.root

        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root

        while curr != None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1

    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right

        return curr.val if curr else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key < curr.key:
            curr = self.removeHelper(curr.left, key)
        elif key > curr.key:
            curr = self.removeHelper(curr.right, key)

        else:
            if curr.right == None:
                return curr.left
            elif curr.left == None:
                return curr.right

            else:
                minNode = self.findMin(curr.right)
                curr.val = minNode.val
                curr.key = minNode.key
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inOrderTraversal(self.root, result)
        return result

    def inOrderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inOrderTraversal(root.left, result)
            result.append(root.key)
            self.inOrderTraversal(root.right, result)

