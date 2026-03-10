import os
import ast
import sys

# ===========================
# تحديد مجلد المشروع
# ===========================
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
PROJECT_FOLDER = os.path.join(DESKTOP, "Project_HORN")

CORE_FILE = os.path.join(PROJECT_FOLDER, "compiler.py")

# ===========================
# وظائف مساعدة
# ===========================
def read_code(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def analyze_compiler():
    code = read_code(CORE_FILE)
    tree = ast.parse(code)
    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    return classes, functions

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def check_file(file):
    try:
        ast.parse(open(file, "r", encoding="utf-8").read())
        print(f"[CHECK] {os.path.basename(file)} OK")
    except Exception as e:
        print(f"[CHECK] {os.path.basename(file)} ERROR: {e}")

# ===========================
# توليد الملفات
# ===========================
def generate_lexer():
    lexer_code = '''
class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.tokens = []

    def tokenize(self):
        while self.pos < len(self.source):
            char = self.source[self.pos]
            if char.isspace():
                self.pos += 1
                continue
            self.tokens.append(char)
            self.pos += 1
        return self.tokens
'''
    write_file(os.path.join(PROJECT_FOLDER, "lexer.py"), lexer_code)

def generate_parser():
    parser_code = '''
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        ast = []
        while self.pos < len(self.tokens):
            ast.append(self.tokens[self.pos])
            self.pos += 1
        return ast
'''
    write_file(os.path.join(PROJECT_FOLDER, "parser.py"), parser_code)

def generate_main():
    main_code = '''
from lexer import Lexer
from parser import Parser
from compiler import Compiler

def main():
    code = "test program"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    compiler = Compiler()
    compiler.compile(ast)
    print("Language Engine Build Success")

if __name__ == "__main__":
    main()
'''
    write_file(os.path.join(PROJECT_FOLDER, "main.py"), main_code)

# ===========================
# بناء المشروع
# ===========================
def build():
    if not os.path.exists(PROJECT_FOLDER):
        print(f"Project folder not found: {PROJECT_FOLDER}")
        sys.exit(1)

    if not os.path.exists(CORE_FILE):
        print(f"compiler.py not found in {PROJECT_FOLDER}")
        sys.exit(1)

    print("Analyzing compiler.py...")
    classes, functions = analyze_compiler()
    print("Classes found:", classes)
    print("Functions found:", functions)

    print("Generating lexer.py...")
    generate_lexer()
    print("Generating parser.py...")
    generate_parser()
    print("Generating main.py...")
    generate_main()

    print("\nChecking files...")
    check_file(CORE_FILE)
    check_file(os.path.join(PROJECT_FOLDER, "lexer.py"))
    check_file(os.path.join(PROJECT_FOLDER, "parser.py"))
    check_file(os.path.join(PROJECT_FOLDER, "main.py"))

    print("\nPROJECT GENERATED SUCCESSFULLY")

if __name__ == "__main__":
    build()