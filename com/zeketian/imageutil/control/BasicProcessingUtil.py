import cv2
import numpy as np
from aip import AipOcr
from PIL import Image, ImageDraw, ImageFont
import os, math


def crop_image(src_img, x_start, x_end, y_start, y_end):
    """
    图片裁剪
    :param src_img: 原始图片
    :param x_start: x 起始坐标
    :param x_end:  x 结束坐标
    :param y_start:  y 开始坐标
    :param y_end: y 结束坐标
    :return:
    """
    tmp_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    tmp_img = tmp_img[y_start:y_end, x_start:x_end]  # 长，宽
    return cv2.cvtColor(tmp_img, cv2.COLOR_RGB2BGR)


def adjust_lightness(src_img, lightness_value):
    """
    :param src_img: 待调整亮度的图片
    :param lightness_value: 亮度值
    :return:
    """
    height, width, channel = src_img.shape  # 获取shape的数值，height和width、通道

    # 新建全零图片数组src2,将height和width，类型设置为原图片的通道类型(色素全为零，输出为全黑图片)
    src2 = np.zeros([height, width, channel], src_img.dtype)
    # new_img = cv2.addWeighted(src_img, a, src2, 1 - a, lightnessValue)  # 处理后的图片
    new_img = cv2.addWeighted(src_img, 1, src2, 1, lightness_value)  # 处理后的图片

    return new_img


def add_watermark(src_img, water_text, position, color):
    """
    添加水印
    :param src_img: 原始图片
    :param water_text: 水印文字
    :param position: 水印位置
    :param color: 水印文字颜色
    :return:
    """
    # 根据选择的位置，确定水印的起始位置
    height, width, channel = src_img.shape
    x_padding, y_padding = width * 0.05, height * 0.05  # 与边缘的间距

    scale = min((width / 1000), (height / 1000))  # 按照图片的长宽大小对字体进行一个放大，scale 即为放大倍数
    font_size = 20 + int(scale) * 5  # 根据 scale 增加字体的大小，从而使得字体大小适应图片的大小
    font_path = "{0}/ui/font.ttf".format(os.getcwd())
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")  # 获取自定义的字体
    (text_width, text_height) = font.getsize(water_text)

    x_start, y_start = 0, 0  # 水印文字的左下角坐标
    if position == "左上角":
        x_start = x_padding
        y_start = y_padding
    elif position == "右上角":
        x_start = width - text_width - x_padding
        y_start = y_padding
    elif position == "中间":
        x_start = (width - text_width) / 2
        y_start = (height - text_height) / 2
    elif position == "左下角":
        x_start = x_padding
        y_start = height - y_padding - text_height
    elif position == "右下角":
        x_start = width - text_width - x_padding
        y_start = height - y_padding - text_height

    img_pil = Image.fromarray(cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB))  # 将 OpenCV 的 BGR 色彩转换成 PIL 需要的 RGB 色彩
    draw = ImageDraw.Draw(img_pil)
    draw.text((x_start, y_start), water_text, color, font=font)
    return cv2.cvtColor(np.asarray(img_pil), cv2.COLOR_RGB2BGR)  # 将 PIL 的 RGB 色彩转换成 OpenCV 的 BGR 色彩


def gaussian_blur(src_img, x_start, x_end, y_start, y_end, ksize, sigmaX):
    """
    高斯模糊
    """
    blur = src_img[y_start:y_end, x_start:x_end]
    blur = cv2.GaussianBlur(blur, ksize, sigmaX)
    src_img[y_start:y_end, x_start:x_end] = blur
    return src_img


def compress_img(src_img, size):
    """
    调整图片到指定大小
    """
    return cv2.resize(src_img, size, interpolation=cv2.INTER_AREA)


def img_stitching(images):
    """
    图片拼接
    """
    stitcher = cv2.Stitcher_create()
    status, stitch_img = stitcher.stitch(images)
    if status != cv2.Stitcher_OK:
        print(f"合拼图片失败，status = {status}")
    return stitch_img


def img_encoding(image, dir_path):
    """
    图片加密
    :return:
    """
    height, width, channel = image.shape

    # 随机创建密钥文件
    img_key = np.random.randint(0, 256, size=[height, width, channel], dtype=np.uint8)
    # 保存密钥
    np.save(dir_path + "/" + "img_key2", img_key)

    #  返回加密后的图片
    return cv2.bitwise_xor(image, img_key)


def img_decoding(image, key_file_path):
    """
    图片解密
    """
    img_key = np.load(key_file_path)
    return cv2.bitwise_xor(image, img_key)


def img_ocr(image):
    """
    OCR 文字识别
    """
    APP_ID = '你的 App ID'
    API_KEY = '你的 Api Key'
    SECRET_KEY = '你的 Secret Key'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    text = client.basicGeneral(image)
    words_result = text["words_result"]
    result_str = ""  # 存储最终的结果
    for w in words_result:
        result_str = result_str + w["words"] + "\n"

    return result_str


# 滤镜效果
def black_white_filter(src_img):
    """
    黑白滤镜
    """
    return cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)  # 直接将图片转换为灰度图片即可


def sketch_filter(src_img):
    """
    素描滤镜
    """
    # 图像灰度处理
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

    # 高斯滤波降噪
    gaussian = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Canny算子
    canny = cv2.Canny(gaussian, 50, 150)

    # 阈值化处理
    ret, result = cv2.threshold(canny, 100, 255, cv2.THRESH_BINARY_INV)
    return result


def embossment_filter(src_img):
    """
    浮雕滤镜
    """
    # 获取图像行和列
    height, width = src_img.shape[:2]
    # 图像灰度处理
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

    result = np.zeros(gray_img.shape, np.uint8)

    for w in range(0, width - 1):
        new_value = np.int32(gray_img[:, w]) - np.int32(gray_img[:, w + 1]) + 120
        new_value[new_value > 255] = 255
        new_value[new_value < 0] = 0
        result[:, w] = new_value

    return result


def reminiscence_filter(src_img):
    """
    怀旧滤镜
    """
    # 图像怀旧特效
    B = 0.272 * src_img[:, :, 2] + 0.534 * src_img[:, :, 1] + 0.131 * src_img[:, :, 0]
    G = 0.349 * src_img[:, :, 2] + 0.686 * src_img[:, :, 1] + 0.168 * src_img[:, :, 0]
    R = 0.393 * src_img[:, :, 2] + 0.769 * src_img[:, :, 1] + 0.189 * src_img[:, :, 0]

    # 像素值大于 255 的，则直接赋值为 255
    B[B > 255] = 255
    G[G > 255] = 255
    R[R > 255] = 255

    filter_result = np.dstack((B, G, R))  # 加了滤镜效果后的图片
    return np.uint8(filter_result)  # 将像素值从 numpy.float64 类型转换成 np.uint8 类型，从而可以正常显示

    # for i in range(rows):
    #     for j in range(cols):
    #         B = 0.272 * src_img[i, j][2] + 0.534 * src_img[i, j][1] + 0.131 * src_img[i, j][0]
    #         G = 0.349 * src_img[i, j][2] + 0.686 * src_img[i, j][1] + 0.168 * src_img[i, j][0]
    #         R = 0.393 * src_img[i, j][2] + 0.769 * src_img[i, j][1] + 0.189 * src_img[i, j][0]
    #         if B > 255:
    #             B = 255
    #         if G > 255:
    #             G = 255
    #         if R > 255:
    #             R = 255
    #         dst[i, j] = np.uint8((B, G, R))
    # return dst


def add_filter(src_img, filter_type):
    """
    为图片添加滤镜效果
    :param src_img: 原始图片
    :param filter_type:  滤镜类型
    """
    if filter_type == "黑白":
        return black_white_filter(src_img)
    elif filter_type == "素描":
        return sketch_filter(src_img)
    elif filter_type == "浮雕":
        return embossment_filter(src_img)
    elif filter_type == "怀旧":
        return reminiscence_filter(src_img)
