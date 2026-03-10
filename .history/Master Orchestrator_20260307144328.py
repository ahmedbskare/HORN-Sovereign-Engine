import os

class CompilerGenerator:
    def __init__(self, source_file):
        self.source_file = source_file
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.required_imports = [
            "import asyncio", "import hashlib", "import hmac", 
            "import time", "import thermal", "from SovereignRegistry import SovereignRegistry"
        ]

    def generate_modules(self):
        # 1. قراءة الملف الأصلي
        source_path = os.path.join(self.script_dir, self.source_file)
        if not os.path.exists(source_path):
            print(f"[!] خطأ: الملف {self.source_file} غير موجود في المجلد الحالي!")
            return

        with open(source_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        total = len(lines)
        # تقسيم احترافي حسب بنية المترجم
        distribution = {
            "lexer.py": int(total * 0.30),
            "parser.py": int(total * 0.40),
            "main.py": total - (int(total * 0.30) + int(total * 0.40))
        }

        # 2. إنشاء الملفات وضخ الأكواد
        start = 0
        print(f"[+] بدء إعادة بناء النظام من {total} سطر:")
        for filename, count in distribution.items():
            file_path = os.path.join(self.script_dir, filename)
            end = start + count
            chunk = lines[start:end]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                # حقن المكتبات في بداية كل ملف جديد
                f.write("\n".join(self.required_imports) + "\n\n")
                f.writelines(chunk)
            
            print(f"    [✔] تم إنشاء {filename} وضخ الكود بنجاح.")
            start = end
            
        print(f"\n[SYSTEM] تم إعادة بناء جميع الملفات بنجاح في: {self.script_dir}")

if __name__ == "__main__":
    # تأكد أن اسم الملف هو 'compiler.py'
    generator = CompilerGenerator("compiler.py")
    generator.generate_modules()