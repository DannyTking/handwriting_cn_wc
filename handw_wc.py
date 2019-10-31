# -*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image
import json 
from wordcloud import WordCloud, ImageColorGenerator

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def gen_wc(words, mask_path, font_path, color_path):
    np_mask = np.array(Image.open(mask_path))
    np_color = np.array(Image.open(color_path))
    repeat = True if len(words) < 50 else False
    wc = WordCloud(background_color="white", max_words=100,
            width=256, height=256, repeat=repeat,
            mask=np_mask, font_path=font_path, random_state=43)

    wc.generate_from_frequencies(words)

    image_colors = ImageColorGenerator(np_color)
    wc.recolor(color_func=image_colors)

    trace_path = os.path.join(d, 'conf', 'trace.json')
    seq = 0
    with open(trace_path, 'r') as in_io_handler:
        trace_dict = json.load(in_io_handler)
        seq = trace_dict['seq'] + 1

    save_path = os.path.join(d, 'out', "handwriting_{0}.png".format(seq))
    wc.to_file(save_path)
    with open(trace_path, 'w+') as out_io_handler:
        json.dump({'seq':seq}, out_io_handler, indent=4, ensure_ascii=False)

    return wc

