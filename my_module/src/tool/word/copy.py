import json
import os

def main():
    word = "/home/asano12300/word/data/dictionary.json"
    txt = "/home/asano12300/gitproject/word_data.txt"
    
    #JSONファイルの読み込み
    with open(word, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # TXTファイルへの書き出し
    with open(txt, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False, sort_keys=True)

    print("抽出完了しました")