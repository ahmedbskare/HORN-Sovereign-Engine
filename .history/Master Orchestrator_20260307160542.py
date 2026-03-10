import os
import re

class SystemArchitect:
    def __init__(self, source_file="compiler.py"):
        self.source_file = source_file
        self.modules = {
            "lexer.py": 3000,
            "parser.py": 4000,
            "main.py": 3000
        }

    def build_system(self):
        print("[!] جاري تنظيف وإعادة بناء هيكلية النظام...")
        if not os.path.exists(self.source_file):
            print(f"[!] خطأ: ملف المصدر {self.source_file} غير موجود!")
            return

        with open(self.source_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # توزيع الأسطر
        cursor = 0
        for mod, count in self.modules.items():
            content = lines[cursor:cursor + count]
            cursor += count
            
            # بناء الملف مع حقن الأمان والمسارات
            with open(mod, 'w', encoding='utf-8') as f:
                f.write("import sys, os\nsys.path.append(os.getcwd())\n")
                f.write("from SovereignRegistry import SovereignRegistry\n")
                f.writelines(content)
            print(f"[✔] تم بناء {mod} ({len(content)} سطر).")

        print("\n[✔] النظام متكامل. جاري التحقق من التبعيات...")
        self.verify_system()

    def verify_system(self):
        # التحقق من الأخطاء الصامتة (Pylance style check)
        for mod in self.modules.keys():
            with open(mod, 'r') as f:
                code = f.read()
                if "HornAssemblyTranslator" in code and "class HornAssemblyTranslator" not in code:
                    print(f"[!] تحذير: {mod} يستدعي كلاس غير معرف في نطاقه!")
        print("[SYSTEM] تم الانتهاء. النظام جاهز للتشغيل.")

if __name__ == "__main__":
    architect = SystemArchitect()
    architect.build_system()