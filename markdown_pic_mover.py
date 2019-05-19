# just support for myself

import argparse
import re
import os
import requests
import datetime
import time

headers = {
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "dnt": "1"
}


def move_img(name_md):
    with open(dir_md + name_md + ".md", encoding="utf8", mode='r') as f:
        content = str(f.read())
        # print(content)
        time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        urls = re.findall(r'(https://.+(?:.jpg|.gif|.jpeg|.png){1}){1}', content)

        for i in range(len(urls)):
            url = urls[i]
            if "sina" in url:
                print(url)
    #             file_type = os.path.splitext(url)[-1]
    #             ir = requests.get(url, headers=headers)
    #             if ir.status_code == 200:
    #                 # time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    #                 file_name = 'pics/%s%s' % (name_md + str(i), file_type)
    #                 open(file_name, 'wb').write(ir.content)
    #                 print(name_md, i, url, "ok")
    #                 time.sleep(1)
    #                 content = content.replace(url, "https://blog.idejie.com/" + file_name)
    #             else:
    #                 print(url, "error")
    #
    # os.system(
    #     "cd pics&&git add . && git commit -m\"%s\"&& git push https://github.com/idejie/pics.git master" % (
    #         time_now))
    # with open(dir_md + name_md + ".md", encoding="utf8", mode='w') as f:
    #     f.write(content)


dir_md = '/Users/idejie/Documents/Blog/source/_posts/'
for name_md in os.listdir(dir_md):
    print("start ", name_md)
    if ".md" in name_md:
        move_img(name_md.replace(".md", ""))
    # os.system("cd pics&&git pull")
