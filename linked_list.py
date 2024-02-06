from typing import Generic, TypeVar


T = TypeVar('T')


class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.prev: Node[T] = None
        self.next: Node[T] = None


class DoublyLinkedList(Generic[T]):

    length: int
    head: Node[T] | None
    tail: Node[T] | None

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, item: T) -> None:
        new_node = Node(item)
        self.length += 1

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at(self, item: T, index: int) -> None:
        if index == self.length:
            self.append(item)
            return
        elif index == 0:
            self.prepend(item)
            return
        
        current = self._get_node_at(index)
        self.length += 1
        new_node = Node(item)
        
        # Linking the new node
        new_node.next = current
        new_node.prev = current.prev
        
        # Rearranging the links of adjacent nodes
        current.prev.next = new_node
        current.prev = new_node
    
    def append(self, item: T) -> None:
        new_node = Node(item)
        self.length += 1
        if self.tail is None:
            self.tail = self.head = new_node
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove(self, item: T) -> T | None:
        current = self.head
        for i in range(self.length):
            if current.value == item:
                break
            current = current.next

        if current is None:
            return
        
        self.length -= 1
        if self.length == 0:
            value = self.head.value
            self.head = self.tail = None
            return value

        if current.prev is not None:
            current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev
        
        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev

        current.next = current.prev = None

        return current.value

    def get(self, index: int) -> T:
        return self._get_node_at(index).value

    def remove_at(self, index: int) -> T:
        node = self._get_node_at(index)
        self.length -= 1
        
        if node.prev:
            node.prev.next = node.next
            node.prev = None
        if node.next:
            node.next.prev = node.prev
            node.next = None
        
        return node.value

    def _get_node_at(self, index: int) -> Node[T]:
        if index < 0 or index >= self.length:
            raise Exception('Out of bounds')

        current = self.head
        for i in range(index):
            current = current.next

        return current

