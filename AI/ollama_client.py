import requests
import time

BASE = "http://127.0.0.1:11434"
GEN = f"{BASE}/api/generate"
TAGS = f"{BASE}/api/tags"

MODEL = "llama3"


def check_ollama():
    try:
        requests.get(TAGS, timeout=5).raise_for_status()
        return True
    except Exception as e:
        print(f"[ERROR] Ollama server not available: {e}")
        return False


def call_ollama(prompt, timeout=150, retry=2):
    if not check_ollama():
        return ""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 500,
            "top_p": 0.9,
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

            result = r.json().get("response", "").strip()

            print(f"[INFO] Ollama completed in {round(time.time() - start, 2)}s")

            if result:
                return result

            print("[WARN] Ollama returned empty response")

        except requests.exceptions.Timeout as e:
            last_error = e
            print(f"[WARN] Ollama timeout after {timeout}s (attempt {attempt}/{retry})")

        except Exception as e:
            last_error = e
            print(f"[ERROR] Ollama failed attempt {attempt}/{retry}: {e}")

        time.sleep(2)

    print(f"[FAILED] Ollama failed completely: {last_error}")
    return ""