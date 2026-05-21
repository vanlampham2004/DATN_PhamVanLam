def build_ui_prompt(
        image_context,
        feature_name="UI",
        n=5
):
    feature = feature_name.lower()
    ocr_text = image_context[:500]

    # LOGIN
    if "login" in feature:
        screen_rule = """
MÀN HÌNH HIỆN TẠI: LOGIN UI

BẮT BUỘC:
- Chỉ sinh test case cho giao diện đăng nhập.
- Ưu tiên:
  + login title
  + username/email/phone input
  + password input
  + login button
  + login form layout
- CẤM dùng:
  + register
  + sign up
  + đăng ký
"""

    # REGISTER
    elif "register" in feature:
        screen_rule = """
MÀN HÌNH HIỆN TẠI: REGISTER UI

BẮT BUỘC:
- Chỉ sinh test case cho giao diện đăng ký.
- Ưu tiên:
  + register title
  + name input
  + email/phone input
  + password input
  + register button
  + register form layout
- CẤM dùng:
  + login
  + sign in
  + đăng nhập
"""

    # STORE PAGE
    elif "store" in feature:
        screen_rule = """
MÀN HÌNH HIỆN TẠI: STORE PAGE UI

BẮT BUỘC:
- Chỉ sinh test case cho giao diện hệ thống cửa hàng.
- Ưu tiên:
  + store page title
  + province dropdown
  + store information
  + store information
  + dropdown filter
  + map section
  + footer section
  + store layout alignment
- CẤM dùng:
  + login
  + register
  + sign in
  + sign up
  + đăng nhập
  + đăng ký
"""

    # DEFAULT
    else:
        screen_rule = f"""
MÀN HÌNH HIỆN TẠI: {feature_name}

BẮT BUỘC:
- Chỉ sinh test case cho đúng giao diện hiện tại.
"""

    return f"""
Bạn là AI sinh TEST CASE kiểm thử giao diện Web từ ảnh chụp giao diện và OCR.

{screen_rule}

OCR TEXT:
{ocr_text}

PHẠM VI:
- Chỉ kiểm thử giao diện hiện tại.
- Không kiểm thử chức năng nghiệp vụ.
- Không kiểm thử backend, database hoặc API.
- Không kiểm thử validate dữ liệu.
- Không kiểm thử đăng nhập hoặc đăng ký thành công/thất bại.
- Không sinh test case chức năng.
- Không tạo error message nếu OCR không có.
- Không copy nguyên OCR nhiễu vào Expected Result.

LOẠI TEST CASE ĐƯỢC PHÉP:
- Kiểm tra page hiển thị.
- Kiểm tra form hiển thị.
- Kiểm tra input hiển thị.
- Kiểm tra button hiển thị.
- Kiểm tra text readability.
- Kiểm tra layout alignment.
- Kiểm tra spacing không bị chồng lấn.
- Kiểm tra map section hiển thị.
- Kiểm tra dropdown/filter hiển thị.
- Kiểm tra card/list layout hiển thị.
- Kiểm tra footer hiển thị.

FORMAT BẮT BUỘC:
TC001 | Description | Expected Result | Output | Highlight

QUY TẮC OUTPUT:
- Sinh đúng {n} test case.
- Không ít hơn {n}.
- Không nhiều hơn {n}.
- Bắt đầu ngay bằng TC001.
- Không viết câu mở đầu.
- Không viết Note.
- Không header.
- Không markdown.
- Không JSON.
- Không giải thích.
- Không dùng dấu ":" sau TC ID.
- Không tạo dòng phân cách.
- Mỗi dòng đúng 5 cột.
- Dùng dấu "|" để phân tách cột.
- Highlight nếu không lỗi ghi "-".
- Nếu có lỗi chỉ dùng:
  + OCR_MISMATCH
  + ELEMENT_MISSING
  + UI_NOT_FOUND
  + LAYOUT_ISSUE

VÍ DỤ ĐÚNG:
TC001 | Verify page visible | Page should display correctly | Page visible | -
TC002 | Verify input field visible | Input field should display correctly | Input field visible | -
TC003 | Verify button visible | Button should display correctly | Button visible | -
TC004 | Verify text readability | Text should be readable | Text readable | -
TC005 | Verify layout alignment | Layout should align correctly | Layout aligned | -

CHỈ TRẢ VỀ ĐÚNG {n} DÒNG TEST CASE.
""".strip()