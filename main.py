from request import getData
import time, json
if __name__ == '__main__':
  t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
  data = getData()
  with open('[fans-data]' + t + '.json', 'w+') as f:
    f.write(json.dumps(data))