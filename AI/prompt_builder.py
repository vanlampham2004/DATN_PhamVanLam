def build_ui_prompt(image_context, feature_name="Register UI", n=5, user_instruction=""):
    extra = user_instruction.strip()
    clean_text = image_context[:700]

    return f"""
Bạn là hệ thống sinh TEST CASE kiểm thử giao diện WEB từ OCR.

MÀN HÌNH ĐANG TEST: {feature_name}

OCR TEXT:
{clean_text}

QUY TẮC BẮT BUỘC:
- Chỉ sinh test case cho màn hình: {feature_name}.
- Nếu là Login UI: ưu tiên kiểm tra form đăng nhập, input tài khoản/email/số điện thoại, input mật khẩu, button đăng nhập, link đăng ký/quên mật khẩu nếu OCR có.
- Nếu là Register UI: ưu tiên kiểm tra form đăng ký, input họ tên, email/số điện thoại, mật khẩu, button đăng ký, link đăng nhập nếu OCR có.
- Không dùng testcase chung chung giống nhau cho mọi màn hình.
- Không test chức năng nghiệp vụ.
- Không sinh login/register thành công hoặc thất bại.
- Không sinh error message nếu OCR không có.
- Nếu OCR nhiễu thì vẫn bám theo tên màn hình {feature_name}.
- Không JSON, không markdown, không giải thích.

FORMAT BẮT BUỘC:
Test Case ID | Description | Expected Result | Output | Highlight

YÊU CẦU:
- Sinh đúng {n} test case.
- Mỗi dòng đúng 5 cột.
- Dùng dấu |
- Highlight nếu không lỗi ghi "-".

YÊU CẦU NGƯỜI DÙNG:
{extra}
""".strip()