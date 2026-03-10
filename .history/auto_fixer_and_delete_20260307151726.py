import os
import sys

def auto_fix_and_self_destruct():
    target_files = ["lexer.py", "parser.py", "main.py"]
    
    # 1. عملية الإصلاح (إضافة المسارات والمكتبات المفقودة)
    for file in target_files:
        if os.path.exists(file):
            with open(file, 'r+', encoding='utf-8') as f:
                content = f.read()
                # إضافة سطر الإصلاح إذا لم يكن موجوداً
                fix = "import sys, os\nsys.path.append(os.getcwd())\n"
                if "sys.path.append" not in content:
                    f.seek(0, 0)
                    f.write(fix + content)
            print(f"[✔] تم إصلاح: {file}")

    # 2. عملية "التدمير الذاتي" (مسح السكربت نفسه بعد الأداء)
    print("\n[SYSTEM] عملية التنظيف اكتملت. جاري حذف ملف الإصلاح...")
    try:
        os.remove(__file__)
        print("[✔] تم حذف ملف المصحح بنجاح.")
    except Exception as e:
        print(f"[!] خطأ في الحذف: {e}")

if __name__ == "__main__":
    auto_fix_and_self_destruct()