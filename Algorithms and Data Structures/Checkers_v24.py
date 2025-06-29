import asyncio
import platform
from random import randrange

class Checkers:
    def __init__(s):
        s.moves = []
        s.badMoves = []
        s.move_history = []

    def CompTurn(s):
        s.moves = s.movesAvailable()
        scored_moves = []
        
        # Assign scores to moves based on strategic priorities
        for move in s.moves:
            score = 0
            # Prioritize captures
            if s.PieceCanCapture(s.moveEndsAt(move)[0], s.moveEndsAt(move)[1]):
                score += 10
            # Prioritize king promotions
            if (((s.moveEndsAt(move)[1] == 7 and s.tiles[move[0]][move[1]].isWhite) or 
                 (s.moveEndsAt(move)[1] == 0 and s.tiles[move[0]][move[1]].isBlack)) and 
                s.tiles[move[0]][move[1]].isPawn):
                score += 5
            # Prioritize capturing kings safely
            if s.tiles[move[2]][move[3]].isKing and s.isMoveSafe(move):
                score += 8
            # Prioritize pawn-for-king trades when advantageous
            if s.tiles[move[0]][move[1]].isPawn and s.tiles[move[2]][move[3]].isKing and not s.isMoveSafe(move):
                score += 6
            # Prioritize trades when ahead in pieces
            if (s.tiles[move[0]][move[1]].isKing and s.tiles[move[2]][move[3]].isKing or 
                s.tiles[move[0]][move[1]].isPawn and s.tiles[move[2]][move[3]].isPawn) and 
               not s.isMoveSafe(move) and s.hasMorePieces():
                score += 4
            # Prioritize safe moves
            if s.isMoveSafe(move):
                score += 2
            # Penalize moving from back row
            if s.movesFromBack(move):
                score -= 5
            scored_moves.append((move, score))
        
        # Sort moves by score in descending order and select the highest-scored move
        scored_moves.sort(key=lambda x: x[1], reverse=True)
        #+-Enhanced to ensure consistent selection of best move
        if scored_moves:
            best_move = scored_moves[0][0]
            if s.selectedTileAt == []:
                s.Action(best_move[0], best_move[1])
            s.Action(best_move[2], best_move[3])
        else:
            # Fallback to random selection if no moves remain
            m = randrange(0, len(s.moves))
            if s.selectedTileAt == []:
                s.Action(s.moves[m][0], s.moves[m][1])
            s.Action(s.moves[m][2], s.moves[m][3])

    def hasMorePieces(s):
        return s.numColour(s.pTurn) > s.numColour(s.opposite(s.pTurn))

    def isMoveSafe(s, move):
        X1, Y1 = [s.moveEndsAt(move)[0] - 1, s.moveEndsAt(move)[0] + 1], [s.moveEndsAt(move)[1] - 1, s.moveEndsAt(move)[1] + 1]
        for i in range(2):
            for j in range(2):
                if s.SpecialPCCP(s.tiles[move[0]][move[1]].pieceColour, X1[i], Y1[j], 
                                 s.moveEndsAt(move)[0], s.moveEndsAt(move)[1], move[0], move[1]):
                    return False
        return True

    def SpecialPCCP(s, piece2Colour, x, y, X, Y, initX, initY):
        X1, X2, Y1, Y2 = [x - 1, x + 1], [x - 2, x + 2], [y - 1, y + 1], [y - 2, y + 2]
        if ((0 <= X < 8) and (0 <= Y < 8)) and ((0 <= x < 8) and (0 <= y < 8)):
            if piece2Colour == s.opposite(s.tiles[x][y].pieceColour):
                if s.CanDoWalk(x, y, X, Y, exception=False):
                    for i in range(2):
                        for j in range(2):
                            if X1[i] == X and Y1[j] == Y:
                                if (0 <= X2[i] < 8) and (0 <= Y2[j] < 8):
                                    if not s.tiles[X2[i]][Y2[j]].isPiece or (X2[i] == initX and Y2[j] == initY):
                                        return True
        return False

    def removeBadMoves(s):
        if s.moves != s.badMoves:
            for move in s.badMoves:
                s.moves.remove(move)

    def movesFromBack(self, move):
        if (self.comp == 0 and self.color == 'White') or \
           (self.comp == 7 and self.color == 'Black'):
            return True
        return False

    def moveEndsAt(s, move):
        if s.tiles[move[2]][move[3]].isPiece:
            return [move[0] + (move[2] - move[0]) * 2, move[1] + (move[3] - move[1]) * 2]
        return [move[2], move[3]]

    def movesAvailable(s):
        moves = []
        for j in range(8):
            for i in range(8):
                X1, Y1 = [i - 1, i + 1], [j - 1, j + 1]
                for a in range(2):
                    for b in range(2):
                        if 0 <= X1[a] < 8 and 0 <= Y1[b] < 8:
                            if s.moveIsValid(i, j, X1[a], Y1[b]):
                                moves.append([i, j, X1[a], Y1[b]])
        return moves

    def moveIsValid(s, x, y, X, Y):
        if 0 <= x < 8 and 0 <= y < 8 and 0 <= X < 8 and 0 <= Y < 8:
            if not s.tiles[x][y].isPiece or s.tiles[x][y].pieceColour != s.pTurn:
                return False
            if s.tiles[X][Y].isPiece and s.tiles[X][Y].pieceColour == s.opposite(s.pTurn):
                return s.PieceCanCapturePiece(x, y, X, Y)
            if s.PieceCanJumpTo(x, y, X, Y):
                return True
            if s.CanDoWalk(x, y, X, Y) and not s.PlayerCanCapture():
                return True
        return False

    def CanDoWalk(s, x, y, X, Y, exception=False):
        X1, Y1 = [x - 1, x + 1], [y - 1, y + 1]
        for i in range(2):
            for j in range(2):
                if X1[i] == X and Y1[j] == Y:
                    if (0 <= X < 8) and (0 <= Y < 8):
                        if (s.tiles[x][y].isWhite and j == 1) or \
                           (s.tiles[x][y].isBlack and j == 0) or \
                           s.tiles[x][y].isKing:
                            if not (exception or s.tiles[X][Y].isPiece) or \
                               (exception and s.tiles[X][Y].isPiece and \
                                (s.pTurn != s.tiles[X][Y].pieceColour)):
                                return True
        return False

    def PieceCanCapturePiece(s, x, y, X, Y):
        X1, X2, Y1, Y2 = [x - 1, x + 1], [x - 2, x + 2], [y - 1, y + 1], [y - 2, y + 2]
        if ((0 <= X < 8) and (0 <= Y < 8)) and ((0 <= x < 8) and (0 <= y < 8)):
            if s.tiles[x][y].isPiece and s.tiles[X][Y].isPiece and \
               s.tiles[x][y].pieceColour == s.opposite(s.tiles[X][Y].pieceColour):
                if s.CanDoWalk(x, y, X, Y, exception=True):
                    for i in range(2):
                        for j in range(2):
                            if X1[i] == X and Y1[j] == Y:
                                if (0 <= X2[i] < 8) and (0 <= Y2[j] < 8):
                                    if not s.tiles[X2[i]][Y2[j]].isPiece:
                                        return True
        return False

    def PieceCanCapture(s, x, y):
        X1, X2, Y1, Y2 = [x - 1, x + 1], [x - 2, x + 2], [y - 1, y + 1], [y - 2, y + 2]
        for i in range(2):
            for j in range(2):
                if s.PieceCanCapturePiece(x, y, X1[i], Y1[j]):
                    return True
        return False

    def PieceCanJumpTo(s, x, y, X, Y):
        X1, X2, Y1, Y2 = [x - 1, x + 1], [x - 2, x + 2], [y - 1, y + 1], [y - 2, y + 2]
        for i in range(2):
            for j in range(2):
                if X2[i] == X and Y2[j] == Y:
                    if s.PieceCanCapturePiece(x, y, X1[i], Y1[j]):
                        return True
        return False

    def PlayerCanCapture(s):
        for i in range(s.BoardDimension):
            for j in range(s.BoardDimension):
                if s.pTurn == s.tiles[i][j].pieceColour and s.PieceCanCapture(i, j):
                    return True
        return False

    def Action(s, X, Y):
        if s.selectedTileAt == []:
            if 0 <= X < 8 and 0 <= Y < 8 and s.tiles[X][Y].isPiece and s.tiles[X][Y].pieceColour == s.pTurn:
                s.selectedTileAt = [X, Y]
                s.tiles[X][Y] = Tile(s.win, X, Y, True, s.tiles[X][Y].pieceColour, s.tiles[X][Y].pieceRank, isSelected=True)
        elif s.selectedTileAt != []:
            if s.moveIsValid(s.selectedTileAt[0], s.selectedTileAt[1], X, Y):
                tiles_copy = [[Tile(s.win, i, j, s.tiles[i][j].isPiece, s.tiles[i][j].pieceColour, s.tiles[i][j].pieceRank) 
                               for i in range(s.BoardDimension)] for j in range(s.BoardDimension)]
                s.move_history.append({
                    'tiles': tiles_copy,
                    'pTurn': s.pTurn,
                    'selectedTileAt': s.selectedTileAt[:],
                    'pieceCaptured': s.pieceCaptured
                })
                s.tiles[X][Y] = Tile(s.win, X, Y, True, s.tiles[s.selectedTileAt[0]][s.selectedTileAt[1]].pieceColour, 
                                     s.tiles[s.selectedTileAt[0]][s.selectedTileAt[1]].pieceRank)
                s.tiles[s.selectedTileAt[0]][s.selectedTileAt[1]] = Tile(s.win, s.selectedTileAt[0], s.selectedTileAt[1], False)
                s.selectedTileAt = []
                s.pTurn = s.opposite(s.pTurn)
            else:
                s.selectedTileAt = []

async def main():
    game = Checkers()
    while True:
        game.CompTurn()
        await asyncio.sleep(1.0 / 60)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
