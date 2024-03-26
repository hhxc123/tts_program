# 中文例子
from sentence_transformers import SentenceTransformer
import numpy as np

def get_and_save_embedding(save_path):
    mypath = "D:\\Users\\Aa\\Desktop\\DailyTalk-main\\distiluse-base-multilingual-cased-v1"
    model = SentenceTransformer(mypath)

    # Our sentences we like to encode
    sentences = ['早上好', '今天天气非常不错']
    sentences1 = 'hello, my name is mingxuan jia.I come from shandong province.'

    # Sentences are encoded by calling model.encode()
    embeddings = model.encode([sentences1])[0]

    # Print the embeddings
    # print(sentences, embeddings, len(embeddings), sep='\n')
    np.save(save_path, embeddings)
