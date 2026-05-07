import requests
import time

BASE = "http://127.0.0.1:11434"
GEN = f"{BASE}/api/generate"
TAGS = f"{BASE}/api/tags"

# dùng model nhẹ hơn nếu muốn nhanh:
# MODEL = "mistral"
MODEL = "llama3"


def check_ollama():
    """
    Kiểm tra Ollama server có đang chạy không
    """
    try:
        r = requests.get(TAGS, timeout=5)
        r.raise_for_status()
        return True
    except Exception as e:
        print(f"[ERROR] Ollama server not available: {e}")
        return False


def call_ollama(prompt, timeout=90, retry=3):
    """
    Gọi Ollama sinh test case
    Có retry để tránh timeout
    """

    if not check_ollama():
        return ""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            # càng thấp càng ổn định
            "temperature": 0.1,

            # giảm để nhanh hơn
            "num_predict": 80,

            # tối ưu tốc độ
            "top_p": 0.9,

            # tránh lặp
            "repeat_penalty": 1.1
        }
    }

    last_error = None

    for attempt in range(1, retry + 1):

        try:
            print(f"[INFO] Calling Ollama... attempt {attempt}/{retry}")

            start = time.time()

            r = requests.post(
                GEN,
                json=payload,
                timeout=timeout
            )

            r.raise_for_status()

            data = r.json()

            result = data.get("response", "").strip()

            duration = round(time.time() - start, 2)

            print(f"[INFO] Ollama completed in {duration}s")

            if result:
                return result

            print("[WARN] Empty response from Ollama")

        except requests.exceptions.Timeout:
            last_error = "Timeout"

            print(
                f"[WARN] Ollama timeout after {timeout}s "
                f"(attempt {attempt}/{retry})"
            )

        except requests.exceptions.ConnectionError:
            last_error = "Connection Error"

            print("[ERROR] Cannot connect to Ollama server")

        except Exception as e:
            last_error = str(e)

            print(
                f"[ERROR] Ollama failed "
                f"(attempt {attempt}/{retry}): {e}"
            )

        time.sleep(2)

    print(f"[FAILED] Ollama completely failed: {last_error}")

    return ""