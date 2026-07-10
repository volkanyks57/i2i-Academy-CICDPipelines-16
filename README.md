# i2i-Academy-CICDPipelines-16
  GitHub Actions ile otomatik unit test, Selenium UI test ve deployment simülasyonu içeren CI/CD pipeline

# Özet
  Bu projede GitHub Actions kullanılarak uçtan uca bir CI/CD pipeline yapılandırıldı. 
  Her code push işleminde otomatik olarak unit test ve Selenium headless UI test 
  çalıştırılır, ikisi de başarılı geçerse deployment simülasyonu tamamlanır.

# Tamamlanan Görevler
  - app.py içinde email format doğrulaması yapan basit bir fonksiyon yazıldı.
  - pytest ile fonksiyon için unit test yazıldı.
  - Selenium ile example.com üzerinde headless UI test yazıldı ve sayfa başlığı doğrulandı.
  - .github/workflows/ci-cd.yml dosyası oluşturularak her push'ta otomatik tetiklenen workflow yapılandırıldı.
  - Workflow Step A ile Python kuruldu ve bağımlılıklar yüklendi.
  - Step B ile pytest, Step C ile Selenium testi çalıştırıldı.
  - Step D ile başarılı deployment mesajı console'a yazdırıldı.

# Kullanılan Teknolojiler
  - Python 3.11
  - pytest
  - Selenium
  - GitHub Actions
  - Ubuntu Runner
