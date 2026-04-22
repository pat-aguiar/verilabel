import httpx
import os

# Configuration
API_URL = "http://localhost:8000/api/v1/upload"
TEST_PDF_PATH = "test_lab_report.pdf" # sample PDF

def test_upload():
    if not os.path.exists(TEST_PDF_PATH):
        print(f"❌ Error: Place a sample PDF at {TEST_PDF_PATH} first.")
        return

    files = {'file': (TEST_PDF_PATH, open(TEST_PDF_PATH, 'rb'), 'application/pdf')}
    data = {'brand_name': 'Test Brand Co'}

    print(f"🚀 Sending {TEST_PDF_PATH} to {API_URL}...")
    
    with httpx.Client(timeout=30.0) as client:
        response = client.post(API_URL, data=data, params=data, files=files)
    
    if response.status_code == 200:
        print("✅ Success!")
        print(f"Result: {response.json()}")
    else:
        print(f"❌ Failed with status {response.status_code}")
        print(f"Detail: {response.text}")

if __name__ == "__main__":
    test_upload()