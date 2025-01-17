import json
import os

j = None
with open('cards.json') as fp:
    j = json.load(fp)

def list_files(directory):
  files = os.listdir(directory)
  return [file for file in files if not os.path.isdir(os.path.join(directory, file))]

fin_set = set(list_files('./cardtext-fin'))
for k in j:
    v = j[k]
    if v['id'] == 0:
        continue
    if str(v['id']) + '.txt' in fin_set:
        continue
    s = ''
    s += v['cn_name'] + '\n'
    if "set_ext" in v:
        s += '（系列：' + v['set_ext'] + '）\n'
    types = v['text']['types']
    types = types.replace('☆', '阶级').replace('★', '等级')
    s += types + '\n'
    s += v['text']['desc'].replace('\r', '')
    with open('cardtext/' + str(v['id']) + '.txt', 'w') as fp:
        fp.write(s)
