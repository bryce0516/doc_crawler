
# Document Crawler

This project is a Python script that crawls and extracts content from a specified website.

이 프로젝트는 지정된 웹사이트에서 콘텐츠를 크롤링하고 추출하는 Python 스크립트입니다.

## Prerequisites (필수 요건)

- Python 3.7 or higher (Python 3.7 이상)
- pip (Python package installer) (pip, Python 패키지 설치 관리자)

## Setting Up the Environment (환경 설정)

1. **Install Python (Python 설치)**:
   - Download and install Python from [python.org](https://www.python.org/downloads/)  
     [python.org](https://www.python.org/downloads/)에서 Python을 다운로드하고 설치하세요.
   - Ensure that Python and pip are added to your system's PATH  
     Python과 pip가 시스템의 PATH에 추가되어 있는지 확인하세요.

2. **Install virtualenv (virtualenv 설치)**:
   ```bash
   pip install virtualenv
   ```

3. **Clone the repository or download the 'doc_crawler.py' file (저장소 클론 또는 'doc_crawler.py' 파일 다운로드)**:
   ```bash
   git clone https://github.com/yourusername/doc-crawler.git
   cd doc-crawler
   ```

4. **Create a virtual environment (가상 환경 생성)**:
   ```bash
   python -m venv venv
   ```

5. **Activate the virtual environment (가상 환경 활성화)**:
   - **On Windows (Windows에서)**:
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS and Linux (macOS 및 Linux에서)**:
     ```bash
     source venv/bin/activate
     ```

6. **Install the required libraries (필수 라이브러리 설치)**:
   ```bash
   pip install requests beautifulsoup4
   ```

## Running the Crawler (크롤러 실행)

1. Ensure your virtual environment is activated  
   가상 환경이 활성화되었는지 확인하세요.

2. Run the script (스크립트 실행):
   ```bash
   python doc_crawler.py
   ```

3. When prompted, enter the URL of the website you want to crawl  
   프롬프트에 지정된 웹사이트의 URL을 입력하세요.

4. The extracted documents will be saved in the 'crawled_docs' directory  
   추출된 문서는 'crawled_docs' 디렉토리에 저장됩니다.

## Deactivating the Virtual Environment (가상 환경 비활성화)

When you're done, you can deactivate the virtual environment:  
작업이 끝나면 다음 명령어로 가상 환경을 비활성화할 수 있습니다:
```bash
deactivate
```

## Precautions (주의사항)

- This crawler can put significant load on websites. Use it responsibly.  
  이 크롤러는 웹사이트에 큰 부하를 줄 수 있습니다. 책임감 있게 사용하세요.
- The current version does not respect robots.txt. Consider legal and ethical implications before use.  
  현재 버전은 robots.txt를 따르지 않습니다. 사용 전에 법적 및 윤리적 측면을 고려하세요.
- The code may need modification for different website structures.  
  웹사이트 구조에 따라 코드가 수정될 수 있습니다.

## Troubleshooting (문제 해결)

If you encounter any issues:  
문제가 발생하면 다음을 확인하세요:

1. Ensure Python is correctly installed and added to PATH.  
   Python이 제대로 설치되고 PATH에 추가되었는지 확인하세요.
2. Verify that you've activated the virtual environment before running the script.  
   스크립트를 실행하기 전에 가상 환경이 활성화되었는지 확인하세요.
3. Check your internet connection.  
   인터넷 연결을 확인하세요.
4. If you get a "ModuleNotFoundError", ensure you've installed all required libraries.  
   "ModuleNotFoundError"가 발생하면 필수 라이브러리가 모두 설치되었는지 확인하세요.
