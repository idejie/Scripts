import asyncio
from pyppeteer import launch
import time


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


async def request_check(req):
    '''请求过滤'''
    if req.resourceType in ['image', 'media', 'eventsource', 'websocket']:
        await req.abort()
    else:
        await req.continue_()


async def get_home(city):
    # 打开浏览器
    browser = await launch({'args': ['--no-sandbox']})
    # 打开新页面
    page = await browser.newPage()
    # 页面设置
    await page.setViewport({'width': 1200, 'height': 1600})
    await page.setRequestInterception(True)
    page.on('request', request_check)
    await page.setJavaScriptEnabled(enabled=False)
    # 登录主页
    await page.goto('https://www.to8to.com/', timeout=100000)
    # 查找相关城市，建立'城市-link'字典
    cities_elements = await page.xpath('//*[@class="xzcs_dt"]/a')
    city_url_dict = {}
    for item in cities_elements:
        # 获取文本
        city_text = await (await item.getProperty('textContent')).jsonValue()
        # 获取链接
        city_link = await (await item.getProperty('href')).jsonValue()
        city_url_dict[city_text] = city_link
    # 判断是否在列表内
    if city in city_url_dict:
        # 构造城市链接
        city_link = city_url_dict[city]
        if city_link[-1] == '/':
            city_com_link = city_link + 'company/'
        else:
            city_com_link = city_link + '/company/'
        # 打开城市
        await page.goto(city_com_link, timeout=100000)
        # 获取公司列表数
        pages_count_element = await page.xpath('//div[@class="pages"]/a[@class="last"]')
        if len(pages_count_element) > 0:
            pages_count = await (await pages_count_element[0].getProperty('textContent')).jsonValue()
            pages_count = int(pages_count)
        else:
            raise Exception('没有查到公司列表')
        # 循环列表数
        for page_num in range(1, pages_count + 1):
            print('page:', page_num)
            companies_link = city_com_link + 'list_' + str(page_num) + '.html'

            try:
                # 打开相关页面
                await page.goto(companies_link, timeout=1000000)
                # 获取城市列表
                companies_list = await page.xpath('//ul[@class="company-data-list"]/li')
                for company_data in companies_list:
                    company_name_element = await company_data.querySelectorAll('p.company-name')
                    company_tel_element = await company_data.querySelectorAll('p.company-phone')

                    # 获取公司名字
                    if len(company_name_element) > 0:
                        company_name = await (await company_name_element[0].getProperty('textContent')).jsonValue()
                    else:
                        company_name = ''
                    # 获取公司电话
                    if len(company_tel_element) > 0:
                        company_tel = await (await company_tel_element[0].getProperty('textContent')).jsonValue()
                    else:
                        company_tel = ''

                    # 进一步判断，尝试拦截
                    if company_tel == '':
                        try:
                            element = await company_data.querySelector('div.company__data__btn.js-list-contact__btn')
                            company_tel = await page.evaluate('(element) => element.getAttribute("data-phone")',
                                                              element)
                            if company_tel != '':
                                raise Exception("Not Support")
                        except:
                            print('公司并无电话')
                            pass
                    # 开始写入文件
                    with open(city + '.txt', 'a') as f:
                        f.write(company_name.strip() + '\t' + company_tel.strip() + '\n')
                        f.close()
            except:
                time.sleep(1)
                continue

            time.sleep(1)
        await browser.close()
    else:
        raise Exception('城市："%s"未收录，请重新检测，目前该网站支持的城市：\n %s' % (city, city_url_dict.keys()))
    # content = await page.evaluate('document.body.textContent', force_expr=True)
    # print(content)
    # await browser.close()


if __name__ == '__main__':
    with open('cities.txt', 'r') as f:
        cities = f.readlines()
    for city_name in cities:
        city_name = city_name.strip()
        print(city_name)
        with open(city_name + '.txt', 'w') as f:
            f.write('')
            f.close()

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(get_home(city_name))
        except Exception as e:
            print(e)
            if '未收录' in str(e):
                with open('not_support.txt', 'a') as f:
                    f.write(city_name + '\n')
                    f.close()
            else:
                with open('tanchuang.txt', 'a') as f:
                    f.write(city_name + '\n')
