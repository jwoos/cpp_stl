#!/usr/bin/env python2

def sum_lists(a, b):
    return [x + y for x, y in zip(coord, move)]

def get_possible_moves(maze, coord, last_move=None):
    max_row = len(maze) - 1
    max_col = len(maze[0]) - 1

    row, col = coord

    moves = []

    if row == 0 and last_move != (-1, 0):
        # no up
        moves.append((1, 0))
    elif row == max_row and last_move != (1, 0):
        # no down
        moves.append((-1, 0))
    else:
        if last_move != [-1, 0]:
            moves.append((1, 0))

        if last_move != (1, 0):
            moves.append((-1, 0))

    if col == 0 and last_move != (0, -1):
        # no left
        moves.append((0, 1))
    elif col == max_col and last_move != (0, 1):
        # no right
        moves.append((0, -1))
    else:
        if last_move != (0, -1):
            moves.append((0, 1))

        if last_move != (0, 1):
            moves.append((0, -1))

    return moves

def dfs(maze, coord, last_move=None, removed=False):
    moves = get_possible_moves(maze, coord)
    current = maze[coord[0]][coord[1]]

    if current == 0 and removed:
        return None
    elif not current:
        removed = True

    visited = 1

    for move in moves:
        r, c = move
        inside_visited = dfs(maze, sum_lists(coord, move), last_move=move, removed=removed)

        if inside_visited is not None:
            visited += inside_visited

    return visited

def answer(maze):
    coord = (0, 0)
    return dfs(maze, (0, 0))
