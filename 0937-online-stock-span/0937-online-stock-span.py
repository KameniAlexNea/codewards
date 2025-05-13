class Node:
    def __init__(self, val: int, score: int, next: "Node" = None):
        self.val = val # current value
        self.score = score # consecutive less than val
        self.next = next # next Node

class StockSpanner:

    def __init__(self):
        self.root = None

    def next(self, price: int) -> int:
        if self.root is None:
            self.root = Node(price, 1, None)
            return 1
        node = Node(price, 0)
        if node.val < self.root.val:
            node.score = 1
            node.next = self.root
            self.root = node
            return 1
        score = 1
        head = self.root
        while head is not None and head.val <= node.val:
            score += head.score
            head = head.next
        if head is None: # current value is greater than the pile
            self.root = Node(price, score, None)
            return score
        node.next = head
        node.score = score
        self.root = node
        return self.root.score
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)