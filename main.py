from compiler import Compiler
from emitter import Emitter
from parser import Parser
import json


def main():
    print("AST Compiler")

    with open('data.json', 'r') as input_file:
        data = input_file.read()

    parser = Parser(data)
    emitter = Emitter('terraform')
    compiler = Compiler(parser, json.loads(data), emitter)

    compiler.program()
    emitter.write_files()
    print("Compiling completed.")


main()
