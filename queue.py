from typing import TypeVar, Generic


T = TypeVar('T')


class Node(Generic[T]):
    
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Node[T] | None = None


class Queue(Generic[T]):
    
    length: int
    head: Node[T] | None
    tail: Node[T] | None

    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, value: T) -> None:
        node = Node(value)
        self.length += 1

        if not self.tail:
            self.tail = self.head = node
            return
        
        self.tail.next = node
        self.tail = node

    def deque(self) -> T | None:
        if not self.head:
            return None

        self.length -= 1
        if self.length == 0:
            self.tail = None

        value = self.head.value
        self.head = self.head.next
        
        return value

    def peek(self) -> T | None:
        return self.head.value if self.head else None

