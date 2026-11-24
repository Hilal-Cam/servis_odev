# Dikdörtgen Alanı Hesaplama Servisi (alan_py)

Bu proje, ROS 2 ortamında özel bir servis arayüzü (`RectangleArea.srv`) kullanarak dikdörtgenin genişlik (`width`) ve yükseklik (`height`) değerlerine göre alanını hesaplayan sunucu ve istemci düğümlerini içerir.

## Özellikler
- `alan_interfaces` paketi altında özel `RectangleArea.srv` servis tanımı oluşturulmuştur.
- `/calculate_rectangle_area` servisi üzerinden istemcilerden gelen istekler dinlenir ve alan hesaplanır (`server`).
- Negatif kenar uzunlukları girildiğinde istek `success: false` yanıtı ile reddedilir.
- Komut satırından parametre alarak istek gönderen istemci düğümü (`client`) geliştirilmiştir.

## Kurulum ve Çalıştırma Adımları

### 1. Çalışma Alanını Derleme
```bash
cd ~/ros2_ws
colcon build --packages-select alan_interfaces alan_py
source install/setup.bash
```
### 2. Sunucu Düğümü Başlatma (1. Terminal)
```bash
ros2 run alan_py server
```
### 3. İstemci Düğümünü Çalıştırma (2. Terminal)
```bash
ros2 run alan_py client 5.0 4.2
ros2 run alan_py client -3.0 4.0
```
### 4. Terminal Üzerinden Doğrulama (ros2 service call)
```bash
ros2 service call /calculate_rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.0, height: 3.5}"
```
### Doğrulama Çıktıları
```bash
$ ros2 run alan_py client 5.0 4.2
[INFO] [rectangle_area_client]: Sonuç (Başarılı): width=5.0, height=4.2 -> Alan = 21.0

$ ros2 run alan_py client -3.0 4.0
[ERROR] [rectangle_area_client]: İstek Reddedildi (success=False): Negatif değer girilemez! (width=-3.0, height=4.0)

$ ros2 service call /calculate_rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.0, height: 3.5}"
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.0, height=3.5)

response:
alan_interfaces.srv.RectangleArea_Response(area=21.0, success=True)
```
### Ekran Görüntüsü
<img width="1781" height="789" alt="O3" src="https://github.com/user-attachments/assets/41a26474-f28e-4374-816a-132377c4bec5" />




