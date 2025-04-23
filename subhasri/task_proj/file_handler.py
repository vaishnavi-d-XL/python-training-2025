from pathlib import Path

with open('app_logger.log','r') as f:
    data=f.read()
    print(type(data))
    print(data)
    print(f.tell())
    print(f.seek(5))

if Path('main.py').exists():
    print("file found")


        