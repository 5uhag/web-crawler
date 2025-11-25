from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


app = Flask(__name__, template_folder='templates')

def scrape_links(target_url):
    unique_links = set()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(target_url, href)
            parsed = urlparse(full_url)
            if parsed.scheme in ['http', 'https']:
                unique_links.add(full_url)

        return list(unique_links), None

    except Exception as e:
        return [], str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape')
def handle_scrape():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "Please provide a url parameter"}), 400
    
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url

    links, error = scrape_links(target_url)
    
    if error:
        return jsonify({"error": error, "url": target_url}), 500
        
    return jsonify({
        "url": target_url,
        "total_links": len(links),
        "links": links
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
