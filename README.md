ROS 2 RectangleArea Servisi Odevi

Bu depo, ozel bir ROS 2 servis arayuzu (RectangleArea.srv) ile dikdortgen alani hesaplayan sunucu (server) ve istemci (client) dugumlerini icerir. Negatif kenar uzunluklari success: false yaniti ile reddedilmektedir.
Derleme Komutlari

cd ~/ros2_ws
colcon build
source install/setup.bash
Calistirma Komutlari

    Terminal (Sunucu):
    ros2 run alan_py server

    Terminal (Istemci):
    ros2 run alan_py client 5.0 4.2
    ros2 run alan_py client -3.0 4.0

Dogrulama Ciktilari

$ ros2 run alan_py client 5.0 4.2
[INFO] [rectangle_area_client]: Sonuc (Basarili): width=5.0, height=4.2 -> Alan = 21.0

$ ros2 run alan_py client -3.0 4.0
[ERROR] [rectangle_area_client]: Istek Reddedildi (success=False): Negatif deger girilemez! (width=-3.0, height=4.0)

$ ros2 service call /calculate_rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.0, height: 3.5}"
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.0, height=3.5)

response:
alan_interfaces.srv.RectangleArea_Response(area=21.0, success=True)

