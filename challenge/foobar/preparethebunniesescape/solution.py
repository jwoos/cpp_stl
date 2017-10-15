#!/usr/bin/env python2

from collections import deque


def sum_lists(a, b):
    return [x + y for x, y in zip(a, b)]

def get_possible_moves(maze, coord):
    max_row = len(maze) - 1
    max_col = len(maze[0]) - 1

    row, col, wb = coord
    moves = []

    if row < max_row:
        # no up
        val = maze[row + 1][col]
        if not val:
            moves.append((row + 1, col, wb))
        elif val and wb:
            moves.append((row + 1, col, 0))

    if row > 0:
        # no down
        val = maze[row - 1][col]
        if not val:
            moves.append((row - 1, col, wb))
        elif val and wb:
            moves.append((row - 1, col, 0))

    if col < max_col:
        # no left
        val = maze[row][col + 1]
        if not val:
            moves.append((row, col + 1, wb))
        elif val and wb:
            moves.append((row, col + 1, 0))

    if col > 0:
        # no right
        val = maze[row][col - 1]
        if not val:
            moves.append((row, col - 1, wb))
        elif val and wb:
            moves.append((row, col - 1, 0))

    return moves

def answer(maze):
    q = deque([(0, 0, 1)])
    max_row = len(maze) - 1
    max_col = len(maze[0]) - 1

    matrix = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    matrix[0][0] = 1

    while q:
        x, y, wall_break = q.popleft()

        if (x, y) == (max_row, max_col):
            print(maze)
            print(matrix)
            return matrix[x][y]

        for m in get_possible_moves(maze, (x, y, wall_break)):
            m_x, m_y, wb = m

            if not matrix[m_x][m_y]:
                print(m_x, m_y, wb)
                matrix[m_x][m_y] = matrix[x][y] + 1
                q.append((m_x, m_y, wb))

    return None

# print(answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
# print(answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(answer([
    [0,1,1,1,1,1,1,1,0,1,1],
    [0,1,1,0,0,0,1,1,0,0,0],
    [0,0,0,0,1,0,1,1,0,1,1],
    [1,1,1,1,1,0,1,1,0,1,1],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,1,1,0,1,0,1,0,1,1,0],
    [0,1,1,0,0,0,1,0,1,1,0],
    [0,1,1,1,1,1,1,0,1,1,0],
    [0,0,0,0,0,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,0,0,0,1,1,0]
]))

[
    [1, 2, 0, 0, 0, 0, 0, 0, 29, 0, 0],
    [2, 3, 6, 7, 8, 9, 0, 0, 28, 29, 30],
    [3, 4, 5, 6, 7, 8, 0, 0, 27, 0, 0],
    [4, 5, 6, 7, 0, 9, 0, 0, 26, 0, 0],
    [5, 6, 7, 8, 0, 10, 0, 24, 25, 26, 27],
    [6, 0, 0, 9, 0, 11, 0, 23, 0, 0, 28],
    [7, 0, 0, 10, 11, 12, 0, 22, 0, 0, 29],
    [8, 0, 0, 0, 0, 0, 0, 21, 0, 0, 30],
    [9, 10, 11, 12, 13, 14, 0, 20, 0, 0, 31],
    [0, 0, 0, 0, 0, 15, 0, 19, 0, 0, 32],
    [0, 0, 0, 0, 0, 16, 17, 18, 0, 0, 33]
]

# print(answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
