import json
with open('./config/record.json', 'w+') as f:
  f.write('[]')
with open('./config/userinfo.json', 'w+') as f:
  user_url_token = input('Input your Zhihu URL token: ')
  f.write(json.dumps({
    'user_url_token': user_url_token
  }))
print('init project completed.')