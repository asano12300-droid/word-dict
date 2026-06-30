import json
import os

word = "/home/asano12300/.config/word-dict/dictionary.json"

def main(select):
    load_json(select)
    
def load_json(select):
    word = "/home/asano12300/.config/word-dict/dictionary.json"
    dict = "/home/asano12300/word/data/dictionary.json"
    
    if os.path.exists(word):
        if select == "1":
            with open(dict, 'r', encoding='utf-8') as f:
                now_dict = json.load(f)
                if select == "1":
                    ex_word = len(now_dict)
                    print(f"単語数: {ex_word}")
        elif select == "2" or select == "3":
            with open(word, 'r', encoding='utf-8') as f:
                now_dict = json.load(f)
                if select == "2":
                    now_word = len(now_dict)
                    print(f"単語数: {now_word}")
                elif select == "3":
                    search = input("検索した単語: ")
                    for word, ex in now_dict.items():
                        if word == search:
                            print(f"{word}の意味: {ex}")
        else:
            print("Error: 選択が無効です")
    else:
        print("インストールされていません")
            
