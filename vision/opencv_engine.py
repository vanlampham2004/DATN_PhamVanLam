import cv2
import os

class OpenCVEngine:

    def __init__(self, threshold=0.8):
        self.threshold = threshold

    def find(self, screen_path, template_path, debug_name="debug"):
        screen = cv2.imread(screen_path, 0)
        template = cv2.imread(template_path, 0)

        if screen is None:
            print("Screen not found")
            return None

        if template is None:
            print("Template not found:", template_path)
            return None

        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= self.threshold:
            h, w = template.shape

            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2

            print(f"Found {template_path} | confidence={max_val}")

            # highlight vùng detect
            screen_color = cv2.imread(screen_path)
            cv2.rectangle(
                screen_color,
                max_loc,
                (max_loc[0] + w, max_loc[1] + h),
                (0, 255, 0),
                2
            )

            os.makedirs("reports", exist_ok=True)
            debug_path = f"reports/{debug_name}.png"
            cv2.imwrite(debug_path, screen_color)

            return center_x, center_y

        print(f"Not found {template_path}")
        return None