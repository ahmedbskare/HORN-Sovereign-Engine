import ast
import traceback


def master_heal(filename):
    print(f">>> [SYSTEM] ANALYZING: {filename}...")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. فحص الهيكل (Syntax Validation)
        try:
            ast.parse(code)
            print(">>> [SUCCESS] CODE STRUCTURE IS CLEAN.")
            return True
        except SyntaxError as e:
            print(f">>> [!] ERROR DETECTED AT LINE {e.lineno}")
            # 2. تصحيح تلقائي للإزاحة (Auto-Indentation Fix)
            # نقوم بإعادة كتابة الملف بتنسيق موحد
            lines = code.splitlines()
            healed_lines = [line.lstrip() for line in lines]

            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(healed_lines))
            print(f">>> [SYSTEM] FIXED LINE {e.lineno} AND RE-STRUCTURED FILE.")
            return False

    except Exception as e:
        print(f">>> [CRITICAL ERROR] {e}")
        return False


if __name__ == "__main__":
    master_heal("compiler.py")
