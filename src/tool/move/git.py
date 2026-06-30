import os
import shutil
from pathlib import Path

def git_move(version):
    deb = "/home/asano12300/word/word-dict-" + version + ".deb"
    to_move = "/home/asano12300/gitproject/" + version
    move = "/home/asano12300/gitproject"
    mv_deb = "/home/asano12300/gitproject/word-dict-" + version + ".deb"
    
    if os.path.exists(deb):
        shutil.move(deb, move)
        
        os.chdir("/home/asano12300/gitproject")
        os.mkdir(version)
        shutil.move(mv_deb, version)
    else:
        print("ファイルが存在しません")        