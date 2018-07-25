# run with 'python -m tree.tests.test_basic' under 'Algorithm' dir
from tree.basic import make_a_basic_n_level_tree, print_tree

def test_make_a_basic_n_level_tree():
    for n in range(5):
        print_tree(make_a_basic_n_level_tree(n))


# TODO: 
#     fix this import
#     involve py.test for this dir
# http://python.jobbole.com/82604/

test_make_a_basic_n_level_tree()
