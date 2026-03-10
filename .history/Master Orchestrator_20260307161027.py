import os

class SystemArchitect:
    def __init__(self):
        # الهيكلية الصارمة للمشروع
        self.modules = {
            "lexer.py": "class Lexer: pass",
            "parser.py": "class Parser: pass",
            "main.py": "import sys\n# Master Orchestrator"
        }

    def build_clean_structure(self):
        print("[!] جاري إعادة هيكلة المشروع...")
        
        # 1. حقن مسارات الأمان لمنع أخطاء الاستيراد
        header = "import sys, os\nsys.path.append(os.getcwd())\n\n"
        
        for filename, content in self.modules.items():
            # مسح الملفات القديمة لضمان نظافة البناء
            if os.path.exists(filename):
                os.remove(filename)
                
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(header)
                f.write(content)
            print(f"[✔] تم بناء {filename} بنجاح.")

        print("\n[✔] البناء الهندسي اكتمل. الآن يمكنك توزيع الأكواد.")

if __name__ == "__main__":
    architect = SystemArchitect()
    architect.build_clean_structure()