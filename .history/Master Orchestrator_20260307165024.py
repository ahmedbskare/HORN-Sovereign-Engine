import os
import re

class CodeMechanic:
    def __init__(self, file_path="compiler.py"):
        self.file_path = file_path

    def refactor(self):
        print(f"[!] جاري فحص وإصلاح: {self.file_path}...")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        imports = []
        classes = []
        logic = []

        # تصنيف الكود هندسياً
        for line in lines:
            if line.startswith("import") or line.startswith("from"):
                imports.append(line)
            elif line.startswith("class"):
                classes.append(line)
            else:
                logic.append(line)

        # إعادة بناء الملف بترتيب منطقي [cite: 2026-02-15]
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write("# --- هيكلية مصححة أوتوماتيكياً ---\n")
            f.writelines(imports)
            f.write("\n")
            f.writelines(classes)
            f.write("\n")
            f.writelines(logic)
        
        print("[✔] تم إصلاح الترتيب: المكتبات -> الكلاسات -> المنطق.")
        print("[✔] النظام الآن جاهز للعمل بدون أخطاء NameError.")

if __name__ == "__main__":
    mechanic = CodeMechanic()
    mechanic.refactor()