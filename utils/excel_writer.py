import pandas as pd

def save_to_excel(data, path):
    lines = data.strip().split("\n")

    clean_rows = []

    for line in lines:
        # chỉ lấy dòng có dấu phẩy
        if "," in line:
            cols = [c.strip() for c in line.split(",")]

            # chỉ giữ dòng đủ 3 cột
            if len(cols) == 3:
                clean_rows.append(cols)

    # header
    header = ["Test Case ID", "Description", "Expected Result"]

    df = pd.DataFrame(clean_rows, columns=header)
    df.to_excel(path, index=False)

    print(" Excel saved:", path)