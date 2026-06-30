import yt_dlp

def down_video(video_url):
    ydl_opts = {
        # 'bestvideo+bestaudio' で最高画質の映像と最高音質の音声を別々に取得し、
        # 'best' でそれらが結合できない場合のフォールバックを指定
        'format': 'bestvideo+bestaudio/best',
        
        # 保存するファイル名（動画タイトル.拡張子）
        'outtmpl': '%(title)s.%(ext)s',  
        
        # ffmpegを使って、動画を最終的に mp4 形式に美しく結合する設定
        'merge_output_format': 'mp4',
        
        # 進行状況などのログを出力する設定（任意）
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        print("ffmpegと連携して最高画質でのダウンロードを開始します...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("\nダウンロードと動画の結合が完了しました！")
        
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
        print("※ffmpegが正しくインストールされているか確認してください。")

if __name__ == "__main__":
    url = input("YouTubeの動画URLを入力してください: ")
    download_video(url)