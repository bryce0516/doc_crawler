import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import time

class DocumentCrawler:
    def __init__(self, base_url, max_depth=3):
        self.base_url = base_url
        self.visited_urls = set()
        self.max_depth = max_depth

    def crawl(self, url, depth=0):
        if depth > self.max_depth:
            return

        if url in self.visited_urls:
            return

        self.visited_urls.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract content
            content = soup.find('div', class_='content')
            if content:
                self.save_content(url, content.get_text())

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
        # Create a file name from the URL
        path = urlparse(url).path
        file_name = path.strip('/').replace('/', '_') + '.txt'
        
        # Ensure the directory exists
        os.makedirs('crawled_docs', exist_ok=True)
        
        # Save the content
        with open(os.path.join('crawled_docs', file_name), 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    base_url = input("크롤링할 웹사이트 주소를 입력하세요: ")
    crawler = DocumentCrawler(base_url)
    crawler.crawl(base_url)
    print("크롤링이 완료되었습니다. 결과는 'crawled_docs' 폴더에 저장되었습니다.")