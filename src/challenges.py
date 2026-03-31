"""Weekly Coding #3 starter code: Metro City Help Center."""

from __future__ import annotations
from collections import deque


# ================================
# Stack Implementation
# ================================
class ActionStack:
    """Stack of recent help-center actions using a Python list."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def push(self, action: str) -> None:
        """Add an action to the top of the stack."""
        self.items.append(action)

    def pop(self) -> str | None:
        """Remove and return the top action, or None if empty."""
        if self.items:
            return self.items.pop()
        return None

    def peek(self) -> str | None:
        """Return the top action without removing it, or None if empty."""
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        return len(self.items) == 0


# ================================
# Queue Implementation
# ================================
class RequestQueue:
    """Queue of waiting citizens using collections.deque."""

    def __init__(self) -> None:
        self.items: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        """Add a citizen name to the back of the queue."""
        self.items.append(name)

    def dequeue(self) -> str | None:
        """Remove and return the front citizen, or None if empty."""
        if self.items:
            return self.items.popleft()
        return None

    def peek(self) -> str | None:
        """Return the front citizen without removing it, or None if empty."""
        if self.items:
            return self.items[0]
        return None

    def is_empty(self) -> bool:
        """Return True if the queue has no waiting citizens."""
        return len(self.items) == 0


# ================================
# Check Balanced Brackets
# ================================
def is_note_balanced(note: str) -> bool:
    """Return True if (), [], and {} are balanced correctly in a note."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in note:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# ================================
# Process Queue
# ================================
def process_request_line(citizens: list[str]) -> list[str]:
    """Return citizens in the order they are served."""
    queue = RequestQueue()
    
    for person in citizens:
        queue.enqueue(person)

    served = []
    while not queue.is_empty():
        served.append(queue.dequeue())

    return served


# ================================
# Undo Recent Actions (Stretch)
# ================================
def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    """Remove the most recent undo_count actions."""
    stack = ActionStack()

    for action in actions:
        stack.push(action)

    for _ in range(undo_count):
        if not stack.is_empty():
            stack.pop()

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    return result[::-1]  # reverse to maintain original order