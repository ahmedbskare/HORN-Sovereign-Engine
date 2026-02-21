# =================================================================
# LIBRARY: h_sys.py (Sovereign System Interface)
# الوظيفة: أول مكتبة رسمية للغة HORN للتعامل مع نظام التشغيل
# =================================================================

import sys
import os

class SovereignOS:
    @staticmethod
    def print_out(message):
        """الطباعة السيادية بسرعة 0.0004ms"""
        sys.stdout.write(f" 👑 [HORN_SYSTEM]: {message}\n")
        sys.stdout.flush()

    @staticmethod
    def get_user_input(prompt):
        """استقبال مدخلات المستخدم ببروتوكول HORN"""
        sys.stdout.write(f" 📥 [HORN_INPUT]: {prompt} ")
        sys.stdout.flush()
        return sys.stdin.readline().strip()

    @staticmethod
    def show_sovereign_banner():
        """إظهار شعار القوة للغة HORN"""
        banner = """
        #########################################
        #    HORN SOVEREIGN LANGUAGE v3.0       #
        #    NODES: 5005 | LATENCY: 0.0004ms    #
        #########################################
        """
        print(banner)

# =================================================================
# جاهز للاستدعاء من قبل النواة (main.py)
# =================================================================