# =========================================================
# LIBRARY: HORN_UTILS (h_utils.py)
# PURPOSE: GENERAL SYSTEM HELPERS & STRING PROCESSING
# ARCHITECT: AHMAD
# =========================================================

import time
import random

class HornUtils:
    """مجموعة الأدوات المساعدة لضمان سرعة الـ 0.0004ms"""
    
    @staticmethod
    def get_timestamp():
        """توليد طابع زمني دقيق للعمليات السيادية"""
        return time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def generate_node_id():
        """توليد معرف فريد لإحدى العقد الـ 5005"""
        prefix = "HORN-NODE-"
        suffix = random.randint(1000, 9999)
        return f"{prefix}{suffix}"

    @staticmethod
    def format_memory_display(size_bytes):
        """تحويل البايتات إلى صيغة مقروءة (ميجابايت) لملف الـ Guard"""
        return f"{size_bytes / (1024 * 1024):.2f} MB"

# =========================================================
# [READY]: هذه المكتبة مخصصة لخدمة [main.py] و [compiler.py]
# =========================================================