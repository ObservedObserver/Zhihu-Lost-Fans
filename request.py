from urllib import request
import json, time
URL = 'https://www.zhihu.com/api/v4/members/chen-hao-49-32-68/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

def getAPI(offset, limit):
  return URL + '&offset=' + str(offset) + '&limit=' + str(limit)
def getTotalFans ():
  api = getAPI(0, 0)
  req = request.Request(api)
  req.add_header('user-agent', 'Chrome/69.0')
  res = request.urlopen(req)
  data = json.loads(res.read().decode('utf-8'))['paging']['totals']
  return data

def getData ():
  total = getTotalFans()
  ans = []
  for i in range(0, total, 20):
    print('get ' + str(i) + ' of total ' + str(total))
    time.sleep(5)
    api = getAPI(i, 20)
    req = request.Request(api)
    req.add_header('user-agent', 'Chrome/69.0')
    res = request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))['data']
    ans += data
  return ans

if __name__ == '__main__':
  data = json.loads(getData())
  names = map(lambda x: x['name'], data['data'])
  print(data['paging']['totals'])
  print(list(names))
  print(len(data['data']))