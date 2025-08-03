import logging
import json
import azure.functions as func
import chess
from function_app import app
# send a JSON body with gameID, currentFen, moveUci

@app.function_name(name="MovePiece")
@app.route(route="MovePiece")
def move_piece(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for a move.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
             "Please pass a JSON body with move data.",
             status_code=400
        )

    game_id = req_body.get('gameId')
    current_fen = req_body.get('currentFen')
    move_uci = req_body.get('moveUci')

    # Load the board state using python-chess
    board = chess.Board(current_fen)

    # Create the move object from UCI
    try:
        move = chess.Move.from_uci(move_uci)
    except chess.InvalidMoveError:
        return func.HttpResponse(
            "Invalid move format. Use UCI format like 'e2e4'.",
            status_code=400
        )

    # Validate the move
    if move not in board.legal_moves:
        return func.HttpResponse(
            "Illegal move. Please enter a valid move.",
            status_code=400
        )

    # Apply the move (excluding castling)
    if not board.is_castling(move): # Check for castling moves
        board.push(move)
    else:
        return func.HttpResponse(
            "Castling is not allowed in this variant.",
            status_code=400
        )

    # Check for game over conditions
    game_over = board.is_game_over()
    checkmate = board.is_checkmate()
    stalemate = board.is_stalemate()

    # Update the game state in the database (e.g., Azure Cosmos DB)
    # You'll need to implement the database interaction here

    # Respond with the updated game state
    return func.HttpResponse(
        json.dumps({
            "message": "Move successful",
            "gameId": game_id,
            "newFen": board.fen(),
            "gameOver": game_over,
            "checkmate": checkmate,
            "stalemate": stalemate
        }),
        mimetype="application/json",
        status_code=200
    )
