from pyTree.Tree import Tree
from board import Board
import copy

SELF_PIECE = 'X'
OPP_PIECE = 'O'

def populateTree(tree, piece):
    cur_board = tree.data
    indices = cur_board.get_none_indices()
    
    if indices == [] or cur_board.board_won(piece) or cur_board.board_won(piece_comp(piece)):
        return Board()

    for i in indices:
        child_board = copy.deepcopy(cur_board)
        child_board.insert_element(i[0], i[1], piece)
        child = Tree(child_board)
        tree.addChild(child)
        populateTree(child, piece_comp(piece))

def mini_max(board):
    tree_root = Tree(board)
    populateTree(tree_root, SELF_PIECE)
    children = tree_root.getChildren()
    temp_min = 10000
    next_move = None

    for child in children:
        if get_tree_depth(child) < temp_min:
            next_move = child
            temp_min = get_tree_depth(child)

    if(next_move is not None):
        return next_move.data

    return None

    


def piece_comp(piece):
    if piece == SELF_PIECE:
        return OPP_PIECE
    else:
        return SELF_PIECE


def get_tree_depth(root):
    
    if root.getChildren() == []:
        return 0

    children = root.getChildren()
    depth = []
    for i in children:
        depth.append(get_tree_depth(i) + 1)

    return min(depth)