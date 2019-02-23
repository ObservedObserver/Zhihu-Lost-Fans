from request import getData
import time, json, os
if __name__ == '__main__':
  t = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
  data = getData()
  filepath = './data/[fans-data]' + t + '.json'
  with open(filepath, 'w+') as f:
    f.write(json.dumps(data))
  with open('./record.json', 'r') as f:
    records = json.loads(f.read())
    records.append(filepath)
    with open('./record.json', 'w') as w:
      w.write(json.dumps(records))
    compare = records[-2:]
    if len(compare) == 2:
      os.system('node check.js -last=' + compare[0] + ' -current=' + compare[1])
    else:
      print('Record saved. No last time record provided.\n')