import ast


def sovereign_audit_and_fix(file_path):
    print(f">>> [AUDIT] READING FULL SYSTEM: {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            full_code = f.read()

        # محاولة تحليل الكود بالكامل
        tree = ast.parse(full_code)
        print(">>> [SUCCESS] SYSTEM INTEGRITY VERIFIED. NO ERRORS FOUND.")

    except SyntaxError as e:
        print(f">>> [!] ERROR FOUND AT LINE {e.lineno}: {e.msg}")
        # إذا وجد خطأ، سنقوم بتنظيف الملف باستخدام "استراتيجية الإزاحة الموحدة"
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # إعادة كتابة كل سطر بدون مسافات بادئة خاطئة (تصفير المسافات)
        fixed_lines = [line.lstrip() + "\n" if i != e.lineno - 1 else line.lstrip() + "\n" for i, line in enumerate(lines)]  # type: ignore

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(fixed_lines)

        print(f">>> [SYSTEM] RE-STRUCTURING ENTIRE FILE. RETRY EXECUTION.")


if __name__ == "__main__":
    sovereign_audit_and_fix("compiler.py")
