from typing import TypeVar, Generic


T = TypeVar('T')


class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.prev: Node[T] = None


class Stack(Generic[T]):

    length: int
    head: Node[T] | None

    def __init__(self) -> None:
        self.length = 0
        self.head = None

    def push(self, value: T) -> None:
        node = Node(value)
        self.length += 1

        if self.head is None:
            self.head = node
            return
        
        node.prev = self.head
        self.head = node

    def pop(self) -> T | None:
        if self.head is None:
            return None
        
        self.length -= 1
        value = self.head.value
        self.head = self.head.prev

        return value

    def peek(self) -> T | None:
        return self.head.value if self.head else None

