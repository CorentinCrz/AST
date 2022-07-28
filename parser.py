import ast


class Parser:
    def __init__(self, data):
        self.tree = ast.parse(data)
        self.visitor = Visitor()

    def visit(self):
        self.visitor.visit(self.tree)


def _get_value(node, value):
    keys = list(map(lambda x: x.value, node.keys))
    if value in keys:
        return node.values[keys.index(value)]
    return None


class Visitor(ast.NodeVisitor):

    def visit_Dict(self, node):
        providers = _get_value(node, 'providers')
        if providers:
            # is it really necessary ?
            aws = _get_value(node, 'aws')

        self.generic_visit(node)
