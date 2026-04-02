import cv2
from ultralytics import YOLO
from tkinter import filedialog
import tkinter as tk

# 1. Modeli yükle
try:
    model = YOLO('best.pt')
except Exception as e:
    print(f"Model yüklenemedi: {e}")
    exit()

# 2. Tkinter kurulumu
root = tk.Tk()
root.withdraw()

def calistir():
    pencere_adi = "Yaren Metal - Tanimlama"
    print("\n" + "="*40)
    print("SİSTEM HAZIR!")
    print("👉 [E] Tuşu: Fotoğraf Seç ve Tanı")
    print("👉 [F] Tuşu: Programdan Çık")
    print("="*40)

    # İlk seçimle sistemi başlatıyoruz
    while True:
        # Eğer ekranda açık pencere yoksa direkt seçim açalım
        # Değilse tuş bekleyelim
        tus = cv2.waitKey(1) & 0xFF

        # E tuşuna basıldığında veya ilk başta
        if tus == ord('e') or tus == ord('E'):
            dosya_yolu = filedialog.askopenfilename(
                title="Fotoğraf Seç",
                filetypes=[("Resim Dosyaları", "*.jpg *.jpeg *.png *.bmp *.webp")]
            )

            if dosya_yolu:
                results = model.predict(source=dosya_yolu, save=False, conf=0.7)
                for r in results:
                    im_array = r.plot()
                    cv2.imshow(pencere_adi, im_array)
                    print(f"✅ İşlem Tamam: {dosya_yolu}")
            else:
                print("⚠️ Seçim yapılmadı.")

        # F tuşuna basıldığında çıkış
        elif tus == ord('f') or tus == ord('F'):
            print("👋 Çıkış yapılıyor...")
            break

        # Pencere 'X' butonuyla kapatılırsa da döngüyü kır
        if cv2.getWindowProperty(pencere_adi, cv2.WND_PROP_VISIBLE) < 1 and \
           cv2.getWindowProperty(pencere_adi, cv2.WND_PROP_AUTOSIZE) >= 0:
             # Eğer kullanıcı pencereyi manuel kapatırsa seçime geri dönmek için 
             # pencereyi tekrar oluşturabiliriz ama biz burada çıkışı tercih edelim
             print("Pencere kapatıldı.")
             # Yeniden seçim için 'e' beklemeye devam eder.

    cv2.destroyAllWindows()
    root.destroy()

if __name__ == "__main__":
    # Önce bir tane boş pencere açalım ki tuşları algılayabilsin
    cv2.namedWindow("Yaren Metal - Tanimlama", cv2.WINDOW_NORMAL)
    calistir()