import os

class SystemMasterBuilder:
    def __init__(self, compiler_file):
        self.compiler_file = compiler_file
        self.files_to_build = {
            "thermal.py": "class ThermalEngine: pass",
            "SovereignRegistry.py": "class SovereignRegistry: pass",
            "lexer.py": "class Lexer: pass",
            "parser.py": "class Parser: pass",
            "main.py": "from modules import * \n# Master Orchestrator"
        }

    def reset_and_build(self):
        print("[#] جاري تنظيف البيئة وبدء البناء الهندسي...")
        
        # 1. تنظيف الملفات القديمة
        for f in self.files_to_build.keys():
            if os.path.exists(f):
                os.remove(f)
                print(f"[!] تم حذف {f} القديم.")

        # 2. بناء الملفات مع حقن الـ Security والـ Path Security
        for filename, content in self.files_to_build.items():
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("import sys, os\nsys.path.append(os.getcwd())\n") # حقن الأمان
                f.write("import asyncio, hashlib, hmac, time\n\n")
                f.write(content)
            print(f"[✔] تم بناء {filename} بنجاح.")

        print("\n[SYSTEM] البناء اكتمل. الترتيب التسلسلي مفعل.")

if __name__ == "__main__":
    builder = SystemMasterBuilder("compiler.py")
    builder.reset_and_build()