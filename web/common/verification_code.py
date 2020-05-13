import random, string
from PIL import Image, ImageFont, ImageDraw, ImageFilter

'''
生成验证码
'''
def generate_color():
    """随机颜色"""
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def generate_code(length=4):
    """
    随机验证码

    :param length: 验证码长度，默认4位
    :return: 指定长度的随机字符
    """

    # random.sample：从指定序列中随机获取指定长度的元素
    return "".join(random.sample(string.ascii_letters + string.digits, length))


def draw_lines(draw, lines=len(generate_code()), fill="black", img_width=150, img_height=50):
    """
    绘制干扰线

    :param draw: 绘图实例
    :param lines: 干扰线数量，默认同验证码长度
    :param fill: 干扰线颜色，默认黑色
    :param img_width: 图片宽度，默认150
    :param img_height: 图片高度，默认50
    :return:
    """

    for i in range(lines):
        # 起始点
        begin = (random.randint(0, img_width), random.randint(0, img_height))
        # 结束点
        end = (random.randint(0, img_width), random.randint(0, img_height))
        draw.line((begin, end), fill)


def generate_img(code_length=4, img_width=150, img_height=50, font_family="arial.ttf",
                 font_size=40, bgcolor="white", line_num=len(generate_code()), line_color="black"):
    """
    生成图形验证码

    :param code_length: 验证码长度，默认4位
    :param img_width: 图片宽度，默认150
    :param img_height: 图片高度，默认50
    :param font_family: 字体类型，默认arial.ttf
    :param font_size: 字体大小，默认40
    :param bgcolor: 背景色，默认白色
    :param line_num: 干扰线数量，默认同验证码长度
    :param line_color: 干扰线颜色，默认黑色
    :return: 验证码和图形验证码
    """

    code = generate_code(code_length)
    # 创建图片对象
    img = Image.new("RGB", (img_width, img_height), bgcolor)
    # 字体
    font = ImageFont.truetype(font_family, font_size)
    font_width, font_height = font.getsize(code)
    # 创建绘图实例
    draw = ImageDraw.Draw(img)
    # 绘制字符串
    draw.text(((img_width - font_width) / len(code), (img_height - font_height) / len(code)),
              code, font=font, fill=generate_color())
    # 绘制干扰线
    draw_lines(draw, line_num, line_color, img_width, img_height)
    # 滤镜：光滑
    img = img.filter(ImageFilter.SMOOTH_MORE)
    return code, img
