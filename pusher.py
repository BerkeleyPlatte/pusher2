from datetime import datetime
import subprocess
from imports import insert

today = datetime.today().strftime('%Y-%m-%d')

with open('text.txt', 'w') as update:
    update.write(f'{today}')

subprocess.Popen(['C:/Program Files/Git/bin/git', 'add', '.'])
subprocess.Popen(['C:/Program Files/Git/bin/git', 'commit', '-m', '"minor changes"'])