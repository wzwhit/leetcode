#  设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
    #  push(x) -- 将元素 x 推入栈中。
    #  pop() -- 删除栈顶的元素。
    #  top() -- 获取栈顶元素。
    #  getMin() -- 检索栈中的最小元素。
#  示例:
#  MinStack minStack = new MinStack();
#  minStack.push(-2);
#  minStack.push(0);
#  minStack.push(-3);
#  minStack.getMin();   --> 返回 -3.
#  minStack.pop();
#  minStack.top();      --> 返回 0.
#  minStack.getMin();   --> 返回 -2.


#  用minstack记录最小值，用空间换时间
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minstack == [] or x <= self.minstack[-1]:
            self.minstack.append(x)


    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.minstack[-1]:
                del self.minstack[-1]
            del self.stack[-1]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack) > 0:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
