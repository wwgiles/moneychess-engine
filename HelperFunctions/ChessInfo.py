import chess

# Piece point values (example - adjust as needed)
PIECE_POINTS = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    # King cannot be bought, but we'll include it for completeness
    chess.KING: 0,
}

# Mapping for string representation of pieces (e.g., 'P' for pawn)
PIECE_STR_MAP = {
    'P': chess.PAWN, 'N': chess.KNIGHT, 'B': chess.BISHOP, 'R': chess.ROOK, 'Q': chess.QUEEN, 'K': chess.KING,
    'p': chess.PAWN, 'n': chess.KNIGHT, 'b': chess.BISHOP, 'r': chess.ROOK, 'q': chess.QUEEN, 'k': chess.KING,
}

# Max rows for initial placement
MAX_DEPLOYMENT_ROWS = 3