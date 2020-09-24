class Stack:

    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):

        return not len(self.stack)

    def get_top(self):
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)


def parenthesis_match(s):
    parenthesis_match_dict = {']': '[', ')': '(', '}':'{'}
    stack = Stack()
    for ch in s:
        if ch in ['(', '[', '{']:
            stack.push(ch)
        elif ch in [')', ']', '}']:
            if stack.is_empty():
                return False
            if stack.get_top() != parenthesis_match_dict[ch]:
                return False

            else:   
                stack.pop()
    if stack.is_empty():
        return True
    else:
        return False

s1 = '(){([asdfsd])[]}[]'
s2 = '()]'
s3 = '(])['
print(parenthesis_match(s2))

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.pop())
# print(stack.pop())