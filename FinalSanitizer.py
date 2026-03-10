import os
import glob

def auto_fix():
    # البحث عن ملف compiler.py في المجلد الحالي
    files = glob.glob("compiler.py")
    if not files:
        print(">>> [ERROR] compiler.py NOT FOUND IN CURRENT DIRECTORY!")
        return

    file_path = files[0]
    print(f">>> [SYSTEM] FOUND: {file_path}. STARTING CLEANING...")
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    fixed_lines = []
    # إزالة كل المسافات البادئة وجعل كل شيء مسطحاً
    for line in lines:
        fixed_lines.append(line.lstrip())

    with open("compiler_clean.py", "w", encoding='utf-8') as f:
        f.writelines(fixed_lines)
        
    print(">>> [SUCCESS] SYSTEM CLEANED. SAVED AS: compiler_clean.py")
    print(">>> [ACTION] NOW RUN: python -m black compiler_clean.py")

if __name__ == "__main__":
    auto_fix()