import random

actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

utilities = [[0, 0, 0, 0],
             [0, 0, 0, -10],
             [0, 0, 0, +10]]

frequencies = [[1, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

current_state = (0, 0)
gamma = 1
lr = 0.1

previous_state = (0, 0)


def print_board(current_state):
    dummy_board = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
    dummy_board[current_state[0]][current_state[1]] = 1
    print(str(dummy_board))


def is_terminal(state):
    if state == (1, 3) or state == (2, 3):
        return False
    return True


def is_allowed(current_state, actions):
    valid_actions = []
    for action in actions:
        row = current_state[0] + action[0]
        col = current_state[1] + action[1]
        if row >= 0 and row < 3:
            if col >= 0 and col < 4:
                if row != 1 or col != 1:
                    valid_actions.append((action[0], action[1]))
    return valid_actions


def random_action(actions):
    return random.sample(actions, 1)


def update_state(actions, state):
    valid_actions = is_allowed(state, actions)
    chosen_action = random_action(valid_actions)
    row = state[0] + chosen_action[0][0]
    col = state[1] + chosen_action[0][1]
    return (row, col)


def update_utility(c_s, p_s):
    reward = 0
    utilities[p_s[0]][p_s[1]] = utilities[p_s[0]][p_s[1]] + \
                              lr * (frequencies[p_s[0]][p_s[1]] * (reward + gamma * utilities[c_s[0]][c_s[1]] - utilities[p_s[0]][p_s[1]]))
    frequencies[p_s[0]][p_s[1]] += 1

print(str(update_state(actions, current_state)))

episodes = 20

for _ in range(episodes):
    current_state = (0, 0)
    print('here')
    while is_terminal(current_state):
        previous_state = current_state
        current_state = update_state(actions, current_state)
        update_utility(current_state, previous_state)
        print(utilities)
