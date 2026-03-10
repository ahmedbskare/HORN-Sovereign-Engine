import os

def allocate_and_write(source_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()
    
    # تعريف التوزيع (النسب المطلوبة)
    # المجموع هنا يجب أن يساوي 10,000
    allocation = {
        "lexer.py": 3000,
        "parser.py": 4000,
        "main.py": 3000
    }
    
    current_line = 0
    for filename, count in allocation.items():
        print(f"[#] تخصيص {count} سطر لملف {filename}...")
        
        # استخراج الجزء الخاص بكل ملف
        chunk = all_lines[current_line : current_line + count]
        
        with open(filename, 'w', encoding='utf-8') as f:
            # حقن الترويسة الأمنية (التي تمنع أخطاء الـ Import)
            f.write("import sys, os\nsys.path.append(os.getcwd())\n\n")
            f.writelines(chunk)
            
        current_line += count
        print(f"[✔] تم بناء {filename} بنجاح.")

if __name__ == "__main__":
    allocate_and_write("compiler.py")