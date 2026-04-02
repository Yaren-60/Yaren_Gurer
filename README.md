🎧 Akıllı Kulaklık Sınıflandırma ve Nesne Tespiti (YOLOv8) Tokat Gaziosmanpaşa Üniversitesi - Bilgisayar Programcılığı Geliştirici: Yaren Gürer

Proje Vizyonu Bu çalışma, giyilebilir teknoloji aksesuarlarını form faktörlerine göre analiz etmek amacıyla geliştirilmiştir. Görüntü ve videolar üzerinden Kulak İçi ve Kulak Üstü kulaklık modellerini gerçek zamanlı olarak tespit eden, YOLOv8 tabanlı bir derin öğrenme mimarisi sunar.

Veri Madenciliği ve Optimizasyon Sınıflandırma: Model; anatomik yapıları tamamen farklı olan Kulak İçi ve Kulak Üstü segmentlerini hedef alır.
Veri Seti Kapasitesi: Roboflow altyapısı ve özel toplama yöntemleriyle oluşturulan veri seti, yaklaşık 2000 adet yüksek çözünürlüklü görüntüden oluşmaktadır.

Hassas Etiketleme: Farklı ışık açıları, kullanıcı üzerindeki duruş varyasyonları ve karmaşık arka planlar altında dahi yüksek başarı sağlaması için tüm görseller manuel olarak "Bounding Box" yöntemiyle etiketlenmiştir.

Ön İşleme: Modelin genelleme kabiliyetini artırmak için veri artırma teknikleri uygulanmış; veri seti Train, Val ve Test olarak optimize edilmiştir.

Mimari Yapı ve Transfer Learning Hız ve doğruluk dengesi sebebiyle son teknoloji YOLOv8s mimarisi tercih edilmiştir. Modelin temel görsel algılama yetenekleri üzerine, tamamen bu projeye özgü kulaklık veri setiyle Transfer Learning uygulanarak sistem özelleştirilmiştir.

Eğitim Stratejisi ve Analitik Performans Süreç: Eğitim süreci 100 epoch üzerinden planlanmış ve erken durdurma parametreleri ile en optimize model elde edilmiştir.

Performans Kayıtları: Eğitim sürecindeki tüm kayıp metrikleri, mAP, Precision ve Recall grafikleri runs/detect/ dizini altında şeffaf bir şekilde tutulmaktadır.

Sonuç Analizi: Yapılan testler sonucunda model, kulaklık formlarını ayırt etmede %85’in üzerinde bir doğruluk oranına ulaşmıştır.

Fonksiyonel Sistem Modülleri (Arayüz Özellikleri) Proje, karmaşık kod yapılarını son kullanıcı için basitleştiren Tkinter tabanlı özgün bir grafik arayüz (GUI) ile birlikte sunulur:
🖼️ Fotoğraf Analiz Modu (foto_tani.py): Seçilen statik görsellerdeki kulaklıkları saniyeler içinde tespit eder ve sınıflandırır.

⌨️ Entegre Etiketleme Motoru: Yeni verileri sisteme hızla öğretmek için geliştirilmiş, klavye kısayolları destekli profesyonel etiketleme modülü.

📂 Proje Dosya Yapısı 📁 runs/: Modelin eğitim geçmişi, performans matrisleri ve görsel sonuçları.

📄 best.pt: Sistemin en yüksek doğruluğa ulaştığı, optimize edilmiş ağırlık dosyası.

📄 data.yaml: Sınıf isimlerini (In-ear, Over-ear) ve veri yollarını barındıran yapılandırma dosyası.

🐍 foto_tani.py: Arayüzü ve nesne tanıma motorunu başlatan ana kaynak kodu.

📝 readme.md: Projenin teknik detaylarını içeren bu dokümantasyon.
