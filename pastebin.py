""" function to generate and return a new paste as benchmark results"""

import json
import os
import requests


github_repo = os.environ['GITHUB_REPOSITORY']
commit_SHA = os.environ['GITHUB_SHA']

outputs_file = open('matrix-outputs.json','r')
outputs = json.load(outputs_file)

paste_file = open('newpaste.txt','a+')
paste_file.write(
    'python benchmark stats for https://github.com/{}/tree/{}/benchmarker.py\n'.format(github_repo,commit_SHA)
    )
for a in outputs:
    paste_file.writelines('python {} executed in {}s\n'.format(a,outputs[a]))

PASTEBIN_OPTION='paste'
pastebin_api_key = os.environ['PASTEBIN_API_KEY']
paste_file.seek(0)
paste_code = paste_file.read()
PASTE_NAME = 'my benchmark stats'

request_data = {
    'api_option'    : PASTEBIN_OPTION,
    'api_dev_key'   : pastebin_api_key,
    'api_paste_code': paste_code,
    'api_paste_name': PASTE_NAME
}

req = requests.post('https://pastebin.com/api/api_post.php', data=request_data)

print(req.status_code)
paste_file.write('URL: {}'.format(req.content))
