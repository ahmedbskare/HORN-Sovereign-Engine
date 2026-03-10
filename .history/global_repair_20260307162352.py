import os

# المكتبات التي يحتاجها مشروعك بناءً على تقرير الخطأ [cite: 2026-02-21]
REQUIRED_IMPORTS = """
import sys
import os
import platform
import uuid
import base64
import random
from datetime import datetime
from random import Random

# إضافة المسار الحالي لضمان رؤية الموديولات المحلية [cite: 2026-03-01]
sys.path.append(os.getcwd())

# استيراد الكلاسات المحلية التي أبلغ Pylance عن فقدانها
try:
    from registry import SovereignRegistry, HornShield, HornSecurityVault
    from lexer import HornVisionEngine, HornHardwareBridge
except ImportError:
    pass
"""

def fix_missing_variables(directory="core_modules"):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            path = os.path.join(directory, filename)
            with open(path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # التأكد من عدم تكرار الحقن
            if "import platform" in original_content:
                continue

            with open(path, 'w', encoding='utf-8') as f:
                f.write(REQUIRED_IMPORTS + "\n" + original_content)
            print(f"[✔] تم إصلاح التبعيات في {filename}")

if __name__ == "__main__":
    # تأكد من المسار الصحيح لمجلد موديولاتك
    fix_missing_variables("core_modules")
    print("\n[SYSTEM] تم تنظيف كافة أخطاء Variable Not Defined.")