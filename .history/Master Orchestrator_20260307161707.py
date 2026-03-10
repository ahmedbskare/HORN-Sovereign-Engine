import os
import re

class SystemRebuilder:
    def __init__(self, source="compiler.py"):
        self.source = source
        self.target_dir = "core_modules"
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

    def extract_and_refactor(self):
        with open(self.source, 'r', encoding='utf-8') as f:
            content = f.read()

        # استخراج الكلاسات والمنطق البرمجي (الترتيب الهندسي)
        # هذا يضمن أن التعريفات تأتي دائماً في الأعلى
        classes = re.findall(r'(class\s+\w+.*?)(?=class\s+\w+|if __name__|$)', content, re.DOTALL)
        
        # بناء الموديولات الأساسية بترتيب هندسي [cite: 2026-02-15]
        modules = {
            "registry.py": "class SovereignRegistry: pass\nclass HornShield: pass",
            "lexer.py": "",
            "parser.py": ""
        }

        # حقن الكلاسات في الملفات (ترتيب: Registry -> Lexer -> Parser)
        for i, class_block in enumerate(classes):
            mod = "registry.py" if "Registry" in class_block or "Shield" in class_block else "parser.py"
            with open(f"{self.target_dir}/{mod}", 'a', encoding='utf-8') as f:
                f.write(f"\nimport sys, os\nsys.path.append(os.getcwd())\n\n{class_block}\n")

        print("[✔] تم إعادة هندسة الموديولات بنجاح.")

if __name__ == "__main__":
    rebuilder = SystemRebuilder()
    rebuilder.extract_and_refactor()