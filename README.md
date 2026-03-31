# Week 3: Metro City Help Center

## Summary
This assignment focuses on stacks and queues in a help center system. I implemented stack operations for tracking actions, queue operations for serving citizens, and functions for checking balanced brackets and processing requests.

## Complexity

- ActionStack.pop → O(1)  
  Removing from end of list is constant time  

- RequestQueue.dequeue → O(1)  
  deque allows fast removal from front  

- is_note_balanced → O(n)  
  We check each character once  

- process_request_line → O(n)  
  Each citizen is processed once  

## Edge Cases

- Empty stack → pop and peek return None  
- Empty queue → dequeue and peek return None  
- Empty string → True  
- No brackets → True  
- Empty citizen list → []  

## Assistance

- AI used: Yes  
- Help: logic, debugging, explanation  
- Sources: class notes, slides  