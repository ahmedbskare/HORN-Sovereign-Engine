import os


def total_rebuild(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    new_lines = []
    indent = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            new_lines.append("\n")
            continue

        # ضبط مستوى الإزاحة
        if stripped.endswith(":"):
            new_lines.append("    " * indent + stripped + "\n")
            indent += 1
        else:
            new_lines.append("    " * indent + stripped + "\n")

        # تقليل الإزاحة إذا لزم الأمر (تبسيط)
        if indent > 0 and (line.startswith("def ") or line.startswith("class ")):
            indent = max(0, indent - 1)

    with open("compiler_rebuilt.py", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(">>> [SYSTEM] REBUILT FILE SAVED AS: compiler_rebuilt.py")


if __name__ == "__main__":
    total_rebuild("compiler.py")
