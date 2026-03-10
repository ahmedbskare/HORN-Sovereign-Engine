import sys
import ast


def fix_system_code(input_file, output_file):
    print(f">>> [SYSTEM] INITIALIZING SURGICAL FIX ON: {input_file}")

    try:
        with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        fixed_lines = []
        indent_level = 0

        for i, line in enumerate(lines):
            stripped = line.lstrip()

            # 1. إزالة أي رموز غريبة أو تالفة
            clean_line = stripped.encode("ascii", "ignore").decode("utf-8")

            # 2. إصلاح الإزاحة (Indentation)
            # إضافة مسافات بناءً على الكلمات المفتاحية مثل class و def
            if clean_line.startswith(("class ", "def ", "async def ")):
                fixed_lines.append("\n" + clean_line)
                indent_level = 1
            elif clean_line.strip() == "":
                fixed_lines.append("\n")
            else:
                fixed_lines.append("    " * indent_level + clean_line)

        # 3. كتابة الملف المصحح
        with open(output_file, "w", encoding="utf-8") as f:
            f.writelines(fixed_lines)

        print(f">>> [SUCCESS] CODE HEALED. SAVED TO: {output_file}")

        # 4. التحقق من الهيكل (Syntax Validation)
        with open(output_file, "r", encoding="utf-8") as f:
            ast.parse(f.read())
            print(">>> [SYSTEM] INTEGRITY CHECK PASSED: CODE IS SYNTACTICALLY CORRECT.")

    except SyntaxError as e:
        print(f">>> [CRITICAL] SYNTAX ERROR AT LINE {e.lineno}: {e.msg}")
    except Exception as e:
        print(f">>> [ERROR] {e}")


if __name__ == "__main__":
    fix_system_code("compiler.py", "compiler_fixed.py")
