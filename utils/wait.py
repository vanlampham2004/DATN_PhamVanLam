import time

def wait_for(condition_func, timeout=10):
    start = time.time()

    while time.time() - start < timeout:
        if condition_func():
            return True
        time.sleep(1)

    return False
