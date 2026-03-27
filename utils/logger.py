def log(msg):
    with open("reports/log.txt", "a") as f:
        f.write(msg + "\n")