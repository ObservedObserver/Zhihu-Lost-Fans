from urllib import request
import json, time

def getURL (url_token):
  return 'https://www.zhihu.com/api/v4/members/' + url_token + '/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

def getAPI (url_token, offset, limit):
  return getURL(url_token) + '&offset=' + str(offset) + '&limit=' + str(limit)

def getTotalFans (url_token):
  api = getAPI(url_token, 0, 0)
  req = request.Request(api)
  req.add_header('user-agent', 'Chrome/69.0')
  res = request.urlopen(req)
  data = json.loads(res.read().decode('utf-8'))['paging']['totals']
  return data

def getData (url_token):
  total = getTotalFans(url_token)
  ans = []
  for i in range(0, total, 20):
    print('get ' + str(i) + ' of total ' + str(total))
    time.sleep(5)
    api = getAPI(url_token, i, 20)
    req = request.Request(api)
    req.add_header('user-agent', 'Chrome/69.0')
    res = request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))['data']
    ans += data
  return ans

if __name__ == '__main__':
  url_token = ''
  with open('./config/userinfo.json', 'r') as f:
    url_token = json.loads(f.read())['user_url_token']
  data = json.loads(getData(url_token))
  names = map(lambda x: x['name'], data['data'])
  print(data['paging']['totals'])
  print(list(names))
  print(len(data['data']))