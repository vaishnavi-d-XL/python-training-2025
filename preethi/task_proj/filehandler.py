with open('app_logger.log','r') as f:
    data=f.read()
    print(type(data))
    print(f.tell())
    print(f.seek(10))
if Path('app_logger.log').exists():
        print("exixts")
else:
      print("not exists")
