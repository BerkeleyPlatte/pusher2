from datetime import datetime
import subprocess
from imports import insert

today = datetime.today().strftime('%Y-%m-%d')

with open('text.txt', 'w') as update:
    update.write(f'{today}')

path = 'C:/Program Files/Git/bin/git'

subprocess.Popen([path, 'add', '.'])
subprocess.Popen([path, 'commit', '-m', 'minor changes'])
subprocess.Popen([path, 'push', 'origin', 'master'])