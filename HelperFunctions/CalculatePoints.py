from function_app import app
import azure.functions as func


def calculate_points(pieces):
    #"""Calculates total points spent on a list of pieces."""
    total_points = 0
    for piece_type in pieces:
        total_points += PIECE_POINTS.get(piece_type, 0)
    return total_points