# -*- coding: utf-8 -*- 
import os
import json
import random

import matplotlib.pyplot as plt
from handw_wc import gen_wc

def gen_words(word_name, mask_name, color_name, font_name):
    words = []

    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    words_path = os.path.join(d, 'conf', word_name)
    with open(words_path, 'r') as in_io_handler:
        words = json.load(in_io_handler)

    words_dict = {}
    for w in words:
        words_dict[w] = random.randint(20, 500)

    mask_path = os.path.join(d, 'mask', mask_name)
    color_path = os.path.join(d, 'mask', color_name)
    font_path = os.path.join(d, 'font', font_name)

    wc = gen_wc(words_dict, mask_path, font_path, color_path)

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()