import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

class DocumentCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()

    def crawl(self, url):
        if url in self.visited_urls:
            return

        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract content
            content = soup.find('div', class_='content')
            if content:
                self.save_content(url, content.get_text())

            # Find and crawl links
            for link in soup.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                if self.is_valid_url(next_url):
                    self.crawl(next_url)

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