class Stack:
    def __init__(self):
        self.stack = []
        pass

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, elem):
        self.stack.append(elem)
        pass

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

class BalanceStr(Stack):
    def __init__(self, check_dic):
        super().__init__()
        self.dic = check_dic

    def balance_braked(self, braked):
        while len(self.stack) != 0:
            self.stack.pop()
        for c in braked:
            if c in '({[':
                self.push(c)
            elif self.stack and c == self.dic[self.stack[-1]]:
                self.pop()
            else:
                print('Unbalanced')
                return
        if self.isEmpty() == True:
            print('Balanced')
            return
        else:
            print('Unbalanced')
            return
