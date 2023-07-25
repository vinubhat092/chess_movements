def get_valid_moves_queen(position):
    column, row = position[0], int(position[1])

    valid_moves = []

    # Horizontal moves (left and right)
    for col in "ABCDEFGH":
        if col != column:
            valid_moves.append(col + str(row))

    # Vertical moves (up and down)
    for r in range(1, 9):
        if r != row:
            valid_moves.append(column + str(r))

    # Diagonal moves (top-left to bottom-right)
    for i in range(1, 9):
        col = chr(ord(column) + i)
        r = row + i
        if col <= "H" and r <= 8:
            valid_moves.append(col + str(r))
        else:
            break

    for i in range(1, 9):
        col = chr(ord(column) - i)
        r = row - i
        if col >= "A" and r >= 1:
            valid_moves.append(col + str(r))
        else:
            break

    # Diagonal moves (top-right to bottom-left)
    for i in range(1, 9):
        col = chr(ord(column) + i)
        r = row - i
        if col <= "H" and r >= 1:
            valid_moves.append(col + str(r))
        else:
            break

    for i in range(1, 9):
        col = chr(ord(column) - i)
        r = row + i
        if col >= "A" and r <= 8:
            valid_moves.append(col + str(r))
        else:
            break

    return valid_moves

def get_valid_moves_bishop(position):
    column, row = position[0], int(position[1])

    valid_moves = []

    # Diagonal moves (top-left to bottom-right)
    for i in range(1, 9):
        col = chr(ord(column) + i)
        r = row + i
        if col <= "H" and r <= 8:
            valid_moves.append(col + str(r))
        else:
            break

    # Diagonal moves (top-right to bottom-left)
    for i in range(1, 9):
        col = chr(ord(column) + i)
        r = row - i
        if col <= "H" and r >= 1:
            valid_moves.append(col + str(r))
        else:
            break

    return valid_moves

def get_valid_moves_rook(position):
    column, row = position[0], int(position[1])

    valid_moves = []

    # Horizontal moves (left)
    for col in reversed("ABCDEFGH"[:ord(column) - ord("A")]):
        valid_moves.append(col + str(row))
        if col == "A":
            break

    # Horizontal moves (right)
    for col in "ABCDEFGH"[ord(column) - ord("A") + 1:]:
        valid_moves.append(col + str(row))

    # Vertical moves (up)
    for r in reversed(range(1, row)):
        valid_moves.append(column + str(r))

    # Vertical moves (down)
    for r in range(row + 1, 9):
        valid_moves.append(column + str(r))

    return valid_moves

def get_valid_moves_knight(position):
    print("dsd",position)
    column, row = position[0], int(position[1])
    print("dsdsd",column,row)

    valid_moves = []

    # Possible knight moves
    moves = [
        (1, 2), (2, 1),
        (1, -2), (2, -1),
        (-1, 2), (-2, 1),
        (-1, -2), (-2, -1)
    ]

    for move in moves:
        col = chr(ord(column) + move[0])
        r = row + move[1]
        if "A" <= col <= "H" and 1 <= r <= 8:
            valid_moves.append(col + str(r))

    return valid_moves