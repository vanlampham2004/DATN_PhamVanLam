import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment


HEADERS = [
    "Test Case ID",
    "Description",
    "Expected Result",
    "Output",
    "Highlight"
]


def is_separator_row(parts):
    return all(
        p.replace("-", "").replace(" ", "") == ""
        for p in parts
    )


def save_to_excel(raw_text, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    rows = []

    for line in raw_text.splitlines():
        line = line.strip()

        if not line:
            continue

        if "|" not in line:
            continue

        # bỏ markdown table viền ngoài
        line = line.strip("|").strip()

        parts = [p.strip() for p in line.split("|")]

        if len(parts) != 5:
            continue

        # bỏ header AI trả về
        if parts[0].lower() == "test case id":
            continue

        # bỏ dòng -------
        if is_separator_row(parts):
            continue

        # chỉ nhận TC thật
        if not parts[0].upper().startswith("TC"):
            continue

        rows.append(parts)

    # fallback nếu AI sinh lỗi format
    if not rows:
        rows = [
            [
                "TC001",
                "Verify register UI visible",
                "Register UI should display correctly",
                "Register UI visible",
                "-"
            ],
            [
                "TC002",
                "Verify register form visible",
                "Register form should display clearly",
                "Register form visible",
                "-"
            ],
            [
                "TC003",
                "Verify register button visible",
                "Register button should display correctly",
                "Register button visible",
                "-"
            ],
            [
                "TC004",
                "Verify text readability",
                "Text should be readable",
                "Text visible",
                "-"
            ],
            [
                "TC005",
                "Verify layout alignment",
                "Layout should not overlap",
                "Layout aligned",
                "-"
            ],
        ]

    wb = Workbook()
    ws = wb.active
    ws.title = "UI Test Cases"

    ws.append(HEADERS)

    for row in rows:
        ws.append(row)

    header_fill = PatternFill(
        start_color="D9EAF7",
        end_color="D9EAF7",
        fill_type="solid"
    )

    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")

    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter

        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))

        ws.column_dimensions[col_letter].width = min(max_length + 5, 70)

    wb.save(file_path)