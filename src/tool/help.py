def help(select):
    menu_dict = {
        "yt": "youtubeの動画をダウンロードする",
        "mv": "word-dict-{version}.debのファイルを移動させます",
        "help": "ヘルプメニューを出します",
        "word": "単語数を調べます",
        "cope": "単語数のtxtを上書きします"
    }
    
    for menu, ex in menu_dict.items():
        if not(select):
            print(f"{menu}: {ex}")
        elif menu == select:
            print(f"{menu}: {ex}")

if __name__ == "__main__":
    menu = input("ヘルプメニューを選択してください: ")
    help(select=menu)