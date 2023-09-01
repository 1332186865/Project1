import numpy as np


class State:
    def __init__(self, state, direction_flag=None, parent=None):
        self.state = state
        self.direction = ['up', 'down', 'right', 'left']
        if direction_flag:
            self.direction.remove(direction_flag)
        self.parent = parent
        self.symbol = ' '

    def get_direction(self):
        return self.direction

    def show_info(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end='\t')
            print("\n")
        print('->\n')
        return

    def get_empty_pos(self):
        position = np.where(self.state == self.symbol)
        return position

    def generate_substates(self):
        if not self.direction:
            return []
        substates = []
        boarder = len(self.state) - 1
        row, col = self.get_empty_pos()
        if 'left' in self.direction and col > 0:
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = temp[row, col]
            news = State(s, direction_flag='right', parent=self)
            substates.append(news)
        if 'up' in self.direction and row > 0:
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = temp[row, col]
            news = State(s, direction_flag='down', parent=self)
            substates.append(news)
        if 'down' in self.direction and row < boarder:
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = temp[row, col]
            news = State(s, direction_flag='up', parent=self)
            substates.append(news)
        if self.direction.count('right') and col < boarder:
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = temp[row, col]
            news = State(s, direction_flag='left', parent=self)
            substates.append(news)
        return substates

    def solve(self):
        open_table = []
        close_table = []
        open_table.append(self)
        step = 1
        while len(open_table) > 0:
            n = open_table.pop(0)
            close_table.append(n)
            sub_states = n.generate_substates()
            move_path = []
            for s in sub_states:
                if (s.state == s.answer).all():
                    while s.parent and s.parent != originState:
                        move_path.append(s.parent)
                        s = s.parent
                        move_path.reverse()
                    return move_path, step + 1
                open_table.extend(sub_states)
                step += 1
        else:
            return None, None


if __name__ == '__main__':
    symbolOfEmpty = ' '
    State.symbol = symbolOfEmpty
    originState = State(np.array([[symbolOfEmpty, 2, 3], [1, 8, 4], [7, 6, 5]]))
    State.answer = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])
    s1 = State(state=originState.state)
    path, steps = s1.solve()
    if path:
        for node in path:
            node.show_info()
    print(State.answer)
    print("Total steps is %d" % steps)
