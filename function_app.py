import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

from CoreFunctions.CreateGame import create_game
from CoreFunctions.DeployGameState import deploy_game_state
from CoreFunctions.GameHistory import game_history
from CoreFunctions.GameState import game_state
from CoreFunctions.MakeMove import move_piece
from CoreFunctions.ValidMoves import valid_moves
from CoreFunctions.Health import health