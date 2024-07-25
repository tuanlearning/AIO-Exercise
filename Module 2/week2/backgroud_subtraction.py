import numpy as np


def compute_difference(bg_img, input_img):
    # Tính toán giá trị khác biệt tuy ệt đối giữa hai hình ảnh
    difference_three_channel = np .abs(bg_img - input_img)

    # Chuy ển đổi sự khác biệt 3 kênh sang một kênh bằng cách tính trung bình.
    # Điều này giúp giảm dữ liệu khác biệt xuống một giá trị cường độ đơn lẻ.
    difference_single_channel = np .sum(difference_three_channel, axis=2) / 3.0

    # Chuy ển đổi trở lại sang uint8 để phù hợp với xử lý ảnh.
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel


def compute_binary_mask(difference_single_channel, threshold=15):
    # Áp dụng ngưỡng ( threshold ) để tạo mask nhị phân
    # Các điểm ảnh có sự chênh lệch màu sắc lớn hơn hoặc bằng 15 được đặt là 255
    difference_binary = np . where(
        difference_single_channel >= threshold, 255, 0)

    # Ghép nối mask nhị phân thành 3 kênh để phù hợp với định dạng RGB.
    binary_binary = np . stack((difference_binary,) * 3, axis=-1)

    return binary_binary


def replace_background(bg_image1, bg_image2, ob_image):
    # Tính toán sự khác biệt giữa hình ảnh đối tượng và hình nền thứ nhất
    difference_single_channel = compute_difference(bg_image1, ob_image)

    # Tính toán mask nhị phân dựa trên sự khác biêt
    binary_mask = compute_binary_mask(difference_single_channel)

    # Thay thế hình nền:
    # ở vị trí mà mask là trắng (255) : thay thế bằng hình nền thứ hai.
    # ở vị trí mà mask là đen (0): giữ hình ảnh đối tượng.
    output = np . where(binary_mask == 255, ob_image, bg_image2)

    return output
