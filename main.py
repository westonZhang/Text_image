from PIL import Image, ImageDraw, ImageFont  # pip install Pillow
from glob import glob
from os.path import basename, join

font_size = 7  # 字体大小
font_space = 1.2  # 字间距
text = "我喜欢你！"
font_file = 'Alibaba-PuHuiTi-Regular.ttf'  # 字体文件路径
inputs_folder = 'input_images'
outputs_folder = 'output_images'


def process(path):
    img_raw = Image.open(path)
    img_array = img_raw.load()
    img_new = Image.new('RGB', img_raw.size, (0, 0, 0))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype(font_file, size=font_size)

    def character_generator(text):
        while True:
            for i in range(len(text)):
                yield text[i]

    ch_gen = character_generator(text)

    for y in range(0, img_raw.size[1], int(font_size * font_space)):
        for x in range(0, img_raw.size[0], int(font_size * font_space)):
            draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

    img_new.convert('RGB').save(join(outputs_folder, basename(path)))


if __name__ == '__main__':
    for path in glob(join(inputs_folder, '*')):
        print('starting processing', path)
        process(path)
        print('finished processing', path)
