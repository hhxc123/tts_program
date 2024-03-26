import torch
from torch.utils.data import DataLoader
from sentence_transformer_test import get_and_save_embedding
import re
import os
import json
import argparse
from string import punctuation
import random
import yaml
import numpy as np
from g2p_en import G2p

from utils.model import get_model, get_vocoder
from utils.tools import get_configs_of, to_device, synth_samples
from dataset import TextDataset
from text import text_to_sequence

text_path = r'D:\Users\Aa\Desktop\DailyTalk-main\output\result\DailyTalk\900000_guo\123\123.txt'
text_path1 = r'D:\Users\Aa\Desktop\DailyTalk-main\output\result\DailyTalk\900000_guo\123\您的输入历史.txt'

def read_lexicon(lex_path):
    lexicon = {}
    with open(lex_path) as f:
        for line in f:
            temp = re.split(r"\s+", line.strip("\n"))
            word = temp[0]
            phones = temp[1:]
            if word.lower() not in lexicon:
                lexicon[word.lower()] = phones
    return lexicon


def preprocess_english(text, preprocess_config):
    text = text.rstrip(punctuation)
    lexicon = read_lexicon(preprocess_config["path"]["lexicon_path"])

    g2p = G2p()
    phones = []
    words = re.split(r"([,;.\-\?\!\s+])", text)
    for w in words:
        if w.lower() in lexicon:
            phones += lexicon[w.lower()]
        else:
            phones += list(filter(lambda p: p != " ", g2p(w)))
    phones = "{" + "}{".join(phones) + " sp sp sp sp sp sp}"
    phones = re.sub(r"\{[^\w\s]?\}", "{sp}", phones)
    phones = phones.replace("}{", " ")

    print("Raw Text Sequence: {}".format(text))
    print("Phoneme Sequence: {}".format(phones))
    sequence = np.array(
        text_to_sequence(
            phones, preprocess_config["preprocessing"]["text"]["text_cleaners"]
        )
    )

    return text, phones

def gen_text(input0):
    print(input0)
    with open(text_path,'w') as f:
        f.write("")
    with open(text_path1,'w') as f:
        f.write("")
    # my_sentence = input("输入句子")
    myinput = input0
    myinput1 = myinput.split('\n')
    for index, item in enumerate(myinput1):
        my_sentence = str(item)

        config_dir = os.path.join("./config", 'DailyTalk')
        preprocess_config = yaml.load(open(
            os.path.join(config_dir, "preprocess.yaml"), "r"), Loader=yaml.FullLoader)

        text, phones = preprocess_english(my_sentence, preprocess_config)

        speaker = index % 2
        print("讲话者:", speaker)
        myans = str(index)+'_' + str(speaker) + '_d123|' + str(speaker) + '|' + phones + '|' + my_sentence[:-1] + '|none\n'
        myans1 = my_sentence
        with open(text_path1, 'a+') as f:
            f.write(myans1)
        print(myans,end="")
        with open(text_path, 'a+') as f:
            f.write(myans)
        print("成功添加到txt文件")
        save_path = 'D:\\Users\\Aa\\Desktop\\DailyTalk-main\\output\\result\\DailyTalk\\900000_guo\\123\\text_emb\\' + str(speaker) + '-text_emb-' + str(index) + '_' + str(speaker) + '_d123' + '.npy'
        # get_and_save_embedding(save_path)
        # print("编码文件保存成功")


if __name__ == "__main__":
    input0 = 'Hello? who are you?\nHello, my name is mingxuan jia. I come from shandong province.\nDo you like play badminton?Could you play with me?\nOk! Let us go to play this sport!'
    gen_text(input0)
