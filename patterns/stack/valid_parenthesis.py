''' 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
''' 

class Solution:
    def isValid(self, s: str) -> bool:
        stack_ = []
        brackets = {"}": "{", ")":"(", "]":"["}
        for i in s:
            # pushing to stack if it is an opening bracket
            if i in brackets.values():
                stack_.append(i)
            # if it is a closing bracket
            if i in brackets.keys():
                # check if the stack is empty 
                if len(stack_) == 0:
                    # if yes, return False
                    return False
                else:
                    # Pop the last opening bracket and see if it matches the closing bracket.
                    popped = stack_.pop()

                    if popped != brackets[i]:
                        return False
        return len(stack_) == 0