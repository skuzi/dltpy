import unittest
from extractor import Extractor, Function


class TestExtractor(unittest.TestCase):

    expected = {
        "__init__": Function("__init__", "", ['self', 'x'], ['', 'int'], "None"),
        "add": Function("add", "This function adds some number to y", ['self', 'y'], ['', 'int'], "int"),
        "return_optional": Function("return_optional", "", ['self', 'y'], ['', 'List[List[int, int]]'], "Optional[int]"),
        "add_async": Function("add_async", "This is an async function", ['self', 'y'], ['', 'int'], "int"),
        "noargs": Function("noargs", "This function has no input arguments", [], [], "int"),
        "noreturn": Function("noreturn", "This function has no typed return", ['x'], ['int'], ""),
        "return_none": Function("return_none", "This function returns None", ['x'], ['int'], "None"),
        "untyped_args": Function("untyped_args", "This function has an untyped input argument", ['x', 'y'], ['int', ''], "int"),
        "type_in_comments": Function("type_in_comments", "", ['x', 'y'], ['', ''], ""),
        "with_inner": Function("with_inner", "This function has an inner function", ['self'], [''], "int"),
        "varargs": Function("varargs", "This function has args as well as varargs", ['self', 'msg', 'xs'], ['', 'str', 'int'], "int"),
        "untyped_varargs": Function("untyped_varargs", "This function has untype varargs", ['self', 'msg', 'xs'], ['', 'str', ''], "int"),
        "inner": Function("inner", "This is the inner function", [], [], "int"),
        "add_special": Function("add_special", "", ["self", "name"], ["", ""], "")
    }

    def setUp(self):
        with open("./resources/example.py") as file:
            program = file.read()
        self.fns = Extractor().extract(program)

    def test_function_parsing(self):
        for fn in self.expected.keys():
            actual = [x for x in self.fns if x.name == fn][0]
            expected = self.expected[fn]
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
