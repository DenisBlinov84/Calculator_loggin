from pathlib import Path
from datetime import datetime


def logg(head='INFO', body='Start program'):
    log_path = Path('data', 'logging.txt')
    log_time = datetime.now().strftime("%Y-%M-%d | %H:%M:%S | ")
    with open(log_path, 'a') as log:
        text = f'{(head + ":"):7}{log_time:30}{body}\n'
        log.write(text)
