def build_ui_prompt(image_context, feature_name="UI", n=5):
    feature = feature_name.lower()
    ocr_text = image_context[:500]

    if "login" in feature:
        screen_rule = """
MÀN HÌNH HIỆN TẠI: LOGIN UI

BẮT BUỘC:
- Chỉ sinh test case cho giao diện đăng nhập.
- Ưu tiên: username/email/phone input, password input, login button, login title, login form layout.
- CẤM dùng các từ: register, sign up, đăng ký.
"""
    elif "register" in feature:
        screen_rule = """
MÀN HÌNH HIỆN TẠI: REGISTER UI

BẮT BUỘC:
- Chỉ sinh test case cho giao diện đăng ký.
- Ưu tiên: name input, email/phone input, password input, register button, register title, register form layout.
- CẤM dùng các từ: login, sign in, đăng nhập.
"""
    else:
        screen_rule = f"""
MÀN HÌNH HIỆN TẠI: {feature_name}

BẮT BUỘC:
- Chỉ sinh test case cho đúng màn hình hiện tại.
"""

    return f"""
Bạn là AI sinh TEST CASE kiểm thử giao diện Web từ ảnh chụp giao diện và OCR.

{screen_rule}

OCR TEXT:
{ocr_text}

PHẠM VI:
- Chỉ kiểm thử giao diện hiện tại.
- Không kiểm thử chức năng nghiệp vụ.
- Không kiểm thử đăng nhập/đăng ký thành công hoặc thất bại.
- Không kiểm thử validate dữ liệu.
- Không kiểm thử backend, database, API.
- Không sinh error message nếu OCR không có.
- Không copy nguyên OCR nhiễu vào Expected Result.

LOẠI TEST CASE ĐƯỢC PHÉP:
- Kiểm tra page/form hiển thị.
- Kiểm tra input hiển thị.
- Kiểm tra button hiển thị.
- Kiểm tra text readable.
- Kiểm tra layout alignment.
- Kiểm tra spacing và không bị chồng lấn.

FORMAT BẮT BUỘC:
TC001 | Description | Expected Result | Output | Highlight

QUY TẮC OUTPUT:
- Sinh đúng {n} test case.
- Không ít hơn {n}.
- Không nhiều hơn {n}.
- Bắt đầu ngay bằng TC001.
- Không viết câu mở đầu.
- Không header.
- Không markdown.
- Không JSON.
- Không giải thích.
- Không dùng dấu ":" sau TC ID.
- Không tạo dòng phân cách.
- Mỗi dòng đúng 5 cột.
- Dùng dấu | để phân tách cột.
- Highlight nếu không lỗi ghi "-".
- Nếu lỗi chỉ dùng: OCR_MISMATCH, ELEMENT_MISSING, UI_NOT_FOUND, LAYOUT_ISSUE.

VÍ DỤ ĐÚNG:
TC001 | Verify input field visible | Input field should be visible | Input field visible | -
TC002 | Verify button visible | Button should be visible | Button visible | -
TC003 | Verify text readability | Text should be readable | Text readable | -
TC004 | Verify form layout alignment | Form layout should align correctly | Form layout aligned | -
TC005 | Verify page spacing | Page spacing should be consistent | Spacing consistent | -

CHỈ TRẢ VỀ ĐÚNG {n} DÒNG TEST CASE.
""".strip()