import os
from bs4 import BeautifulSoup
from flask import Flask, send_file

def combine_documents(input_dir, output_file):
    combined_content = []
    
    for root, dirs, files in os.walk(input_dir):
        for file in sorted(files):
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    soup = BeautifulSoup(content, 'html.parser')
                    main_content = soup.find('main')
                    if main_content:
                        h1 = soup.new_tag('h1')
                        h1.string = os.path.relpath(file_path, input_dir)
                        combined_content.append(str(h1))
                        combined_content.append(str(main_content))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("""
        <html>
        <head>
            <title>Combined Kubernetes Documentation</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
                h1 { border-top: 1px solid #ccc; padding-top: 20px; }
                pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
            </style>
        </head>
        <body>
            <h1>Combined Kubernetes Documentation</h1>
        """)
        f.write('\n'.join(combined_content))
        f.write("</body></html>")

# 문서 결합
input_directory = 'crawled_docs'
output_file = 'combined_docs.html'
combine_documents(input_directory, output_file)
print(f"문서가 성공적으로 결합되어 {output_file}에 저장되었습니다.")

# Flask 웹 서버 설정
app = Flask(__name__)

@app.route('/')
def serve_combined_doc():
    return send_file('combined_docs.html')

if __name__ == '__main__':
    print("웹 서버가 시작되었습니다. http://localhost:5000 에서 결합된 문서를 확인할 수 있습니다.")
    app.run(debug=True)