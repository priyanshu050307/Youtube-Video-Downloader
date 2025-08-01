from flask import Flask, request, render_template, jsonify
import yt_dlp
import os

app = Flask(__name__)

# Ensure the "downloads" folder exists otherwise it will create problem 
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Function to download video
def download_video(url):
    ydl_opts = {'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Function to download MP3
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_video', methods=['POST'])
def download_video_route():
    url = request.form['url']
    try:
        download_video(url)
        return jsonify({'status': 'success', 'message': 'Video downloaded successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/download_audio', methods=['POST'])
def download_audio_route():
    url = request.form['url']
    try:
        download_audio(url)
        return jsonify({'status': 'success', 'message': 'Audio downloaded successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
