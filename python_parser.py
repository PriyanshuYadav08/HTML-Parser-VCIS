from flask import Flask, render_template
import os
from dotenv import load_dotenv
import re

load_dotenv()

app = Flask(__name__)

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" (?P<status>\d{3}) (?P<byte>\d+|-) "(?P<referrer>[^"]*)" "(?P<user_info>[^"]*)"'
)

def parse_logs(file_path):
    with open(file_path, 'r') as file:
        logs = []
        for line in file:
            match = LOG_PATTERN.match(line)
            if match:
                logs.append(match.groupdict())
        return logs

@app.route('/')
def display_logs():
    logs1 = parse_logs('D:/HTML-Parser-VCIS/1.txt')
    logs2 = parse_logs('D:/HTML-Parser-VCIS/2.txt')
    return render_template('logs.html', logs1=logs1, logs2=logs2)

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("my_ip_add"), port=5000)