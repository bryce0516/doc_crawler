import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import time
import re

class DocumentCrawler:
    def __init__(self, base_url, max_depth=3):
        self.base_url = base_url
        self.visited_urls = set()
        self.max_depth = max_depth
        self.saved_files = set()
        self.load_existing_files()

    def load_existing_files(self):
        if os.path.exists('crawled_docs'):
            for root, dirs, files in os.walk('crawled_docs'):
                for file in files:
                    if file.endswith('.html'):
                        path_parts = os.path.relpath(os.path.join(root, file), 'crawled_docs').split(os.sep)
                        url_path = '/' + '/'.join(path_parts)
                        url_path = url_path.rsplit('.', 1)[0]  # Remove the file extension
                        self.visited_urls.add(urljoin(self.base_url, url_path))
            print(f"Loaded {len(self.visited_urls)} existing URLs")

    def crawl(self, url, depth=0):
        if depth > self.max_depth:
            return

        if url in self.visited_urls:
            print(f"Skipping already visited URL: {url}")
            return

        self.visited_urls.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and save the main content
            main_content = soup.find('main')
            if main_content:
                self.save_content(url, main_content)
            else:
                print(f"No main content found for {url}")

            # Find and crawl links
            for link in soup.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                if self.is_valid_url(next_url):
                    self.crawl(next_url, depth + 1)

            time.sleep(1)  # Be polite, wait 1 second between requests

        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc == urlparse(self.base_url).netloc and parsed_url.path.startswith('/docs/')

    def save_content(self, url, content):
        # Create a file name and path from the URL
        path = urlparse(url).path
        file_path = os.path.join('crawled_docs', path.strip('/'))
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Add .html extension if not present
        if not file_path.endswith('.html'):
            file_path += '.html'
        
        # Save the content
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"<html><head><title>{url}</title></head><body>")
                f.write(f"<h1>Source: <a href='{url}'>{url}</a></h1>")
                f.write(str(content))
                f.write("</body></html>")
            print(f"Saved: {file_path}")
            self.saved_files.add(file_path)
        except Exception as e:
            print(f"Error saving {file_path}: {str(e)}")

if __name__ == "__main__":
    base_url = input("크롤링할 웹사이트 주소를 입력하세요: ")
    crawler = DocumentCrawler(base_url)
    crawler.crawl(base_url)
    print("크롤링이 완료되었습니다. 결과는 'crawled_docs' 폴더에 저장되었습니다.")
    print(f"총 {len(crawler.saved_files)}개의 새 파일이 저장되었습니다.")