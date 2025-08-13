import requests
import tempfile
import subprocess
import sys
import os

GITHUB_RAW_URL = "https://gist.githubusercontent.com/PurushothMathav/fcbb1f147c1670172f7466ea789e8b7d/raw/1507fe0fa730db350ac52643e1fae6e2e204b484/mx_downloader.py"

print("Downloading the latest Youder source from GitHub...")
response = requests.get(GITHUB_RAW_URL)
response.raise_for_status()

with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp_file:
    tmp_file.write(response.content)
    tmp_path = tmp_file.name

print(f"Running Youder from: {tmp_path}")
subprocess.run([sys.executable, tmp_path])

os.remove(tmp_path)