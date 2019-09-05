class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = -1
        self.rear = -1

    def push(self, value) -> bool:
        if self.isFull:
            self.pop()
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def pop(self) -> bool:
        if self.isEmpty:
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1

    def isFull(self) -> bool:
        return True if (self.rear + 1) % self.size == self.head else False

    def isEmpty(self) -> bool:
        return True if self.rear == -1 and self.front == -1 else False

    def next(self, val: int) -> float:
        self.push(val)
        mv = 0
        n = 0
        for i in self.queue:
            if i:
                mv += i
                n += 1
        return mv / n if n > 0 else 0

m = MovingAverage(3)

print(m.next(1))
print(m.next(2))
print(m.next(3))
print(m.next(4))
print(m.next(5))
print(m.next(6))
