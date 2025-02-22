from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        
        # Validate Instagram URL
        if 'instagram.com' not in url:
            return jsonify({'error': 'Invalid Instagram URL'})
        
        # API to fetch video (Replace with a working API)
        api_url = f"https://some-instagram-api.com/download?url={url}"
        response = requests.get(api_url)
        data = response.json()
        
        if 'video_url' in data:
            return jsonify({'video_url': data['video_url']})
        else:
            return jsonify({'error': 'Failed to fetch video.'})
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
