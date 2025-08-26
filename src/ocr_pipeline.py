import cv2
import pytesseract
import os


# Point to your installed tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"❌ File not found: {image_path}")

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"❌ Could not read the image file: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

if __name__ == "__main__":
    sample_img = "docs/sample_medical_report.png"
    print(extract_text(sample_img))
