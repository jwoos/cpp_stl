#!/usr/bin/env python3
import chess.pgn as pgn


f = open('data_set/lichess_db_standard_rated_2013-03.pgn')

game = pgn.read_game(f)
while game:
    game = pgn.read_game(f)
    print(game)
