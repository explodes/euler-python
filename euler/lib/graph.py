#!/usr/bin/env python
from collections import defaultdict, deque


class CyclicalGraphException(Exception):
    pass


NO_ROOT = object()
ROOT = object()


class Graph(defaultdict):
    def __init__(self, root=NO_ROOT):
        """
        Construct this graph
        :param root: Specify a root to use use as the default start point for functions
        """
        super(Graph, self).__init__(list)
        self.root = root
        if root is not NO_ROOT:
            self[root] = list()

    def add(self, start, *end):
        self[start].extend(end)

    def edges(self):
        """
        Generating yielding (node, node) tuples representing all edges
        """
        for node, neighbors in self.iteritems():
            for neighbor in neighbors:
                yield (node, neighbor)

    def traverse(self, root=ROOT):
        """
        Simple traversal generator, yielding all nodes in this graph.
        For trees, this will traverse breadth-first.
        :param root starting node, use sentinel ROOT to start with the root node
        """
        if root is ROOT:
            root = self.root

        if root not in self:
            raise KeyError("Start point not in graph")

        visited = set()
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            # add neighbors to the queue
            queue.extend(self[node])

            yield node

            visited.add(node)

    def print_tree(self, root=ROOT):
        """
        Print the nodes as a tree.
        Cyclical graphs will raise a CyclicalGraphException
        :param root starting node, use sentinel ROOT to start with the root node
        """
        if root is ROOT:
            root = self.root

        if root not in self:
            raise KeyError("Start point not in graph")

        visited = set()
        queue = deque()
        queue.append((0, root))
        while queue:
            depth, node = queue.popleft()
            if node in visited:
                raise CyclicalGraphException("Cycle detected")
            queue.extendleft(reversed([(depth + 1, child) for child in self[node]]))
            print '%s%s' % (' ' * (depth - 1), node)
            visited.add(node)


if __name__ == '__main__':
    import unittest


    class GraphTest(unittest.TestCase):

        def test_root(self):
            g = Graph(root="TOOB")
            self.assertIn("TOOB", g)

        def test_no_root(self):
            g = Graph()
            self.assertEqual(g.root, NO_ROOT)

        def test_gen_edges(self):
            g = Graph()
            g.add('a', 'b', 'c', 'd')
            g.add('b', 'c')
            g.add('c', 'd')
            self.assertItemsEqual(list(g.edges()), [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('c', 'd')])

        def test_traverse_invalid_start(self):
            g = Graph()
            g.add('a', 'b', 'c', 'd')
            g.add('b', 'c', 'e')
            g.add('c', 'd')
            self.assertRaises(KeyError, lambda: list(g.traverse('x')))

        def test_traverse(self):
            g = Graph()
            g.add('a', 'b', 'c', 'd')
            g.add('b', 'c', 'e')
            g.add('c', 'd')
            self.assertItemsEqual(list(g.traverse('a')), ['a', 'b', 'c', 'd', 'e'])

        def test_traverse_tree(self):
            g = Graph(root='a')
            g.add('a', 'b', 'c', 'd')
            g.add('b', 'c', 'e')
            g.add('c', 'd')
            self.assertItemsEqual(list(g.traverse()), ['a', 'b', 'c', 'd', 'e'])

        def test_traverse_cycle(self):
            g = Graph()
            g.add('a', 'b', 'c', 'd')
            g.add('b', 'c', 'e')
            g.add('c', 'd')
            g.add('e', 'a')
            self.assertItemsEqual(list(g.traverse('a')), ['a', 'b', 'c', 'd', 'e'])

        def test_traverse_breadth_first(self):
            g = Graph()
            g.add(1, 2, 3, 4)
            g.add(2, 5, 6)
            g.add(4, 7, 8)
            g.add(5, 9, 10)
            g.add(7, 11, 12)
            self.assertEqual(list(g.traverse(1)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

        def test_print_tree_cycle_error(self):
            g = Graph()
            g.add(1, 2, 3, 4)
            g.add(2, 5, 6)
            g.add(4, 5, 6)
            g.add(6, 7, 8)
            g.add(8, 1)
            self.assertRaises(CyclicalGraphException, g.print_tree, 1)

        def test_print_tree(self):
            g = Graph()
            g.add(1, 2, 3, 4)
            g.add(2, 5, 6)
            g.add(4, 7, 8)
            g.add(5, 9, 10)
            g.add(7, 11, 12)
            g.print_tree(1)
            pass

        def test_print_tree_root(self):
            g = Graph(1)
            g.add(1, 2, 3, 4)
            g.add(2, 5, 6)
            g.add(4, 7, 8)
            g.add(5, 9, 10)
            g.add(7, 11, 12)
            g.print_tree()
            pass


    unittest.main()
