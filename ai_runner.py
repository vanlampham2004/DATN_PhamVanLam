from vision.ocr import extract_text
from generator.test_case_gen import generate_test_cases
from generator.selenium_gen import generate_selenium_code

IMAGE = "screenshots/current.png"

# Step 1: OCR
text = extract_text(IMAGE)

# Step 2: Generate test cases
test_cases = generate_test_cases(text)
print("=== TEST CASES ===")
print(test_cases)

# Step 3: Generate Selenium
code = generate_selenium_code(test_cases)
print("=== SELENIUM CODE ===")
print(code)