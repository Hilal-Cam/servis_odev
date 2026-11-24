import sys
import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class RectangleAreaClient(Node):
    def __init__(self):
        super().__init__('rectangle_area_client')
        self.cli = self.create_client(RectangleArea, 'calculate_rectangle_area')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')
        self.req = RectangleArea.Request()

    def send_request(self, width, height):
        self.req.width = width
        self.req.height = height
        return self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print('Kullanım: ros2 run alan_py client <width> <height>')
        return

    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
    except ValueError:
        print('Hata: Lütfen geçerli sayısal değerler girin.')
        return

    client = RectangleAreaClient()
    future = client.send_request(width, height)
    rclpy.spin_until_future_complete(client, future)

    response = future.result()
    if response.success:
        client.get_logger().info(
            f'Sonuç (Başarılı): width={width}, height={height} -> Alan = {response.area}'
        )
    else:
        client.get_logger().error(
            f'İstek Reddedildi (success=False): Negatif değer girilemez! (width={width}, height={height})'
        )

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
