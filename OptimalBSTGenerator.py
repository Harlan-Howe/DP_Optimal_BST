import numpy as np
from typing import Tuple
from TreeNodeFile import TreeNode
import TreeNodeFile


class OptimalBSTGenerator:

    def __init__(self, freq_dict: dict):
        """
        takes a dictionary of string:float pairs, representing words and their frequency/probability.
        NOTE: assumes the words were added to the dictionary in alphabetical order, so that their keys are in order.
        :param freq_dict:
        """
        self.freq_dict = freq_dict
        self.frequencies = list(freq_dict.values())
        size = len(self.frequencies)
        self.costs = np.zeros([size+1, size+1], dtype=float)
        self.best_root_indices = np.zeros([size + 1, size + 1], dtype=int)

    def find_sum_of_frequencies(self, start: int, length: int) -> float:
        """
        calculates the sum of "length" consecutive frequencies, beginning at index "start"
        :param start: first index
        :param length: number of frequencies to add
        :return: sum of frequencies
        """
        freq_sum = 0
        # TODO: you write this. (It should go pretty quickly.)
        return freq_sum

    def find_min_tree_pair_cost(self, start: int, length: int) -> Tuple[float, int]:
        """
        considering a range of words start -> start+length, finds the index with the cheapest set of two subtrees, split
        before and after that index (not including the index) and returns the cost and the index.
        :param start: the index of the first word in the list
        :param length: the number of words under consideration.
        :return: the cost of the cheapest pair of trees (C.left + C.right) and the index of where this optimal
                 placing went.
        """
        best = 9E9
        best_i = -1
        # TODO: you write this.
        return best, best_i

    def find_tree_pair_cost(self, start: int, left_branch_length: int, length: int) -> float:
        """
        calculates the sum of the costs of two subtrees on either side of a prospective root.
        The first subtree is for words ranging from [index: start] through [index: start+left_branch_length-1]
        The second subtree is for words ranging from [index: start+left_branch_length+1] through [index: start+length]
        :param start: the index of the first word
        :param left_branch_length: the number of words in the first subtree
        :param length: the number of words under consideration
        :return: The sum of the costs of the two subtrees. (C.left + C.right)
        """
        # TODO: you write this.
        return 0.987654321  # garbage number, but it's distinct.

    def find_min_cost_for_subtree(self, start: int, length: int) -> Tuple[float, int]:
        """
        considering a range of words start -> start+length, finds the index with the cheapest set of two subtrees, split
        before and after that index (not including the index) and returns the cost of those trees plus the frequencies
        of this range and the index.
        :param start: the index of the first word in the list
        :param length: the number of words under consideration.
        :return: the cost of the cheapest subtrees (C.left + C.right + sum_of_frequencies) and the index of where this
        optimal placing went.
        """
        # TODO - you write this. Hint: it's a combination of two of the other methods.
        return -0.99, -9  # garbage numbers, but distinct.

    def build_cost_matrix(self):
        """
        fills in the self.costs matrix for the dictionary, using dynamic programming.
        :return: None
        """
        size = self.costs.shape[0] + 1
        # Column 0 is already initialized to zero, so you don't need to do anything here.
        pass

        # Column 1:
        for i in range(size):
            self.costs[i, 1] = self.frequencies[i]
            # Optional:
            self.best_root_indices[i, 1] = i

        # Columns 2+
        # TODO - you write this.

    def build_subtree_for_range(self, start: int, length: int) -> TreeNode:
        """
        generates a binary tree, based on the cost matrix, for the selected range of values in the dictionary.
        :param start: the index of the first word
        :param length: the number of words to include
        :return: the root TreeNode of the resulting subtree.
        """
        result = TreeNode()  # temporary line. Replace it with something better in the TO-DO section.
        # TODO - you write this.
        return result

    def build_tree(self) -> TreeNode:
        """
        Wrapper function to generate the optimal binary search tree for the entire dictionary, assuming you have already
        called build_cost_matrix.
        :return: the root TreeNode for this tree.
        """
        return self.build_subtree_for_range(0, len(self.freq_dict))


if __name__ == '__main__':
    generator = OptimalBSTGenerator({"begin": 0.05, "do": 0.40, "else": 0.08, "end": 0.04, "if": 0.10,
                                     "then": 0.10, "while": 0.23})
    generator.build_cost_matrix()
    print(f"generator.costs\n{generator.costs}")
    print(f"best_root_indices:\n{generator.best_root_indices}")

    # Uncomment when you are ready to build the tree and look at it.
    """
    root:TreeNode = generator.build_tree()
    TreeNodeFile.display_tree(root = root, width=800, height=400)
    """

    # Uncomment when you are ready to try the code above on a second frequency dictionary.
    """
    SIA_dict = {'A': 0.07292954264524104, 'AM': 0.018541409147095178, 'AND': 0.030902348578491966, 
    'ANYWHERE': 0.009888751545117428, 'ARE': 0.002472187886279357, 'BE': 0.004944375772558714, 
    'BOAT': 0.003708281829419036, 'BOX': 0.00865265760197775, 'CAR': 0.00865265760197775, 'COULD': 0.0173053152039555, 
    'DARK': 0.00865265760197775, 'DO': 0.04573547589616811, 'EAT': 0.029666254635352288, 'EGGS': 0.013597033374536464, 
    'FOX': 0.00865265760197775, 'GOAT': 0.004944375772558714, 'GOOD': 0.002472187886279357, 
    'GREEN': 0.013597033374536464, 'HAM': 0.013597033374536464, 'HERE': 0.013597033374536464, 
    'HOUSE': 0.009888751545117428, 'I': 0.103831891223733, 'IF': 0.0012360939431396785, 'IN': 0.049443757725587144, 
    'LET': 0.004944375772558714, 'LIKE': 0.05562422744128554, 'MAY': 0.004944375772558714, 'ME': 0.004944375772558714, 
    'MOUSE': 0.009888751545117428, 'NOT': 0.103831891223733, 'ON': 0.00865265760197775, 'OR': 0.009888751545117428, 
    'RAIN': 0.004944375772558714, 'SAM': 0.022249690976514216, 'SAY': 0.006180469715698393, 
    'SEE': 0.004944375772558714, 'SO': 0.006180469715698393, 'THAN': 0.0012360939431396785, 
    'THANK': 0.002472187886279357, 'THAT': 0.002472187886279357, 'THE': 0.013597033374536464, 
    'THEM': 0.0754017305315204, 'THERE': 0.011124845488257108, 'THEY': 0.002472187886279357, 
    'TRAIN': 0.011124845488257108, 'TREE': 0.007416563658838072, 'TRY': 0.004944375772558714, 
    'WILL': 0.02595797280593325, 'WITH': 0.023485784919653894, 'WOULD': 0.032138442521631644, 
    'YOU': 0.042027194066749075}
    
    generator2 = OptimalBSTGenerator(SIA_dict)
    generator2.build_cost_matrix()
    print(f"Cost of optimal = {generator2.costs[0, generator2.costs.shape[1] - 1]}")

    root2:TreeNode = generator2.build_tree()
    TreeNodeFile.display_tree(root=root2, width = 1600, height = 800)
    """