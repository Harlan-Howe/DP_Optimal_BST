import cv2
import numpy as np
import random


class TreeNode:
    """
    A simple binary tree node that you can use to generate binary trees.
    """
    def __init__(self, value: str = None, left: "TreeNode" = None, right: "TreeNode" = None):
        self.value = value
        self.left = left
        self.right = right


"""
The following two methods (a wrapper method and recursive drawing function) are just to display a tree made of 
TreeNodes.
You should not need to modify these methods, but you are welcome to look at them.
Note: they are stand-alone methods, not part of the TreeNode class.
"""


def display_tree(root: TreeNode = None, width: int = 800, height: int = 800, vspacing: int = 60):
    global font
    screen = np.zeros([height, width, 3], dtype=float)
    font = cv2.FONT_HERSHEY_PLAIN

    display_tree_at_location_on_screen_in_width(root=root, x=int(width/2), y=vspacing,
                                                vspacing=vspacing, screen=screen, width=width)

    cv2.imshow("tree", screen)
    cv2.waitKey(0)


def display_tree_at_location_on_screen_in_width(root: TreeNode = None, x: int = 400, y: int = 40, vspacing: int = 60,
                                                screen: np.ndarray = None, width: int = 800):
    if screen is None:
        print("Error - null screen")
        return
    if root is None:
        return
    word = root.value
    word_width = cv2.getTextSize(word, font, 1, 1)[0][0]

    col = (random.randint(0, 50) / 50 + 0.5, random.randint(0, 50) / 50 + 0.5, random.randint(0, 50) / 50 + 0.5)
    cv2.putText(img=screen, text=word, org=(int(x - word_width / 2), y),
                fontFace=font, fontScale=1,
                color=col, thickness=1)

    if root.left is not None:
        cv2.line(screen, (x, y), (x - int(width / 4), y + vspacing - 10), (255, 255, 255), 1)
        display_tree_at_location_on_screen_in_width(root=root.left, x=int(x - width / 4),
                                                    y=y + vspacing, screen=screen, width=int(width / 2))

    if root.right is not None:
        offset = random.randint(5, int(vspacing / 2))  # added so adjacent words don't collide so badly, thus the right
        # sides are downshifted a little.
        cv2.line(screen, (x, y), (x + int(width / 4), y + vspacing - 10 + offset), (255, 255, 255), 1)
        display_tree_at_location_on_screen_in_width(root=root.right, x=int(x + width / 4),
                                                    y=y + vspacing + offset, screen=screen, width=int(width / 2))
