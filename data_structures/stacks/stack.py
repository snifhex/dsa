from abc import ABC, abstractmethod
from collections import deque
from queue import LifoQueue
from typing import NoReturn


class StackBase(ABC):
    length = 0
    bucket = None

    def push(self, element) -> NoReturn:
        self.bucket.append(element)
        self.set_length()
    
    def pop(self):
        poped_value = self.bucket.pop()
        self.set_length()
        return poped_value

    def lastitem(self):
        return self.bucket[-1]
    
    def is_empty(self) -> bool:
        return len(self.bucket) == 0

    def set_length(self) -> NoReturn:
        self.length = len(self.bucket)

    def __repr__(self):
        return str([elements for elements in self.bucket])

    @abstractmethod
    def __init__(self):
        pass
    

class ListStack(StackBase):
    def __init__(self):
        self.bucket = []
        self.set_length()


class DequeStack(StackBase):
    def __init__(self):
        self.bucket = deque()
        self.set_length()


class LifoQueueStack(StackBase):
    def __init__(self) -> NoReturn:
        self.bucket = LifoQueue()
        self.set_length()

    def push(self, element) -> NoReturn:
        self.bucket.put(element)
        self.set_length()
    
    def pop(self):
        poped_value = self.bucket.get()
        self.set_length()
        return poped_value

    def lastitem(self):
        return self.bucket.queue[-1]
    
    def set_length(self) -> NoReturn:
        self.length = len(self.bucket.queue)
    
    def __repr__(self):
        return str([elements for elements in self.bucket.queue])


def stack(**kwargs):
    backends = {'list':ListStack, 'deque': DequeStack, 'lqueue':LifoQueueStack} 
    backend=kwargs.get('backend', '')
    if backend:
        return backends[backend]()
    else:
        return DequeStack()



