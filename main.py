import requests
import os
import json
import logging
import re

# key = os.environ["KEY"]
#key = ''

# send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key

# https://access.video.qq.com/user/auth_refresh 获取 cookie
# login_cookie = os.environ["LOGIN_COOKIE"]
# signin_cookie = os.environ["SIGNIN_COOKIE"]
# auth_refresh_url = os.environ["AUTH_REFRESH_URL"]
login_cookie = 'tvfe_boss_uuid=c17e18df8ba386b4; pgv_pvid=3999877924; video_guid=5f0d190890486c96; video_platform=2; pgv_info=ssid=s2604017047; _qpsvr_localtk=0.6913157758126973; RK=jZK0Zv5OZe; ptcz=bfd5d050d1260b13c8b2f85c775f19c4a3ae8f7657f32e4b5d78bfe06a8e3be5; main_login=qq; vqq_access_token=8ADD26F6AECC724D425C9444282209D0; vqq_appid=101483052; vqq_openid=27F1D011825D09298C335340FCAFAA7E; vqq_vuserid=319682459; vqq_vusession=lgAwCdsV4ReuCucXIiCFsQ..; vqq_refresh_token=BC0B4AC4FAE7BOTURL72474015B3D962EAB2C3; login_time_init=2021-7-14 13:7:22; uid=404782061; vqq_next_refresh_time=6599; vqq_login_time_init=1626239239; login_time_last=2021-7-14 13:7:23'
signin_cookie = 'tvfe_boss_uuid=c17e18df8ba386b4; pgv_pvid=3999877924; video_guid=5f0d190890486c96; video_platform=2; pgv_info=ssid=s2604017047; _qpsvr_localtk=0.6913157758126973; RK=jZK0Zv5OZe; ptcz=bfd5d050d1260b13c8b2f85c775f19c4a3ae8f7657f32e4b5d78bfe06a8e3be5; main_login=qq; vqq_access_token=8ADD26F6AECC724D425C9444282209D0; vqq_appid=101483052; vqq_openid=27F1D011825D09298C335340FCAFAA7E; vqq_vuserid=319682459;  vqq_refresh_token=BC0B4AC4FAE7BOTURL72474015B3D962EAB2C3; login_time_init=2021-7-14 13:7:22; uid=404782061; vqq_next_refresh_time=6599; vqq_login_time_init=1626239239; login_time_last=2021-7-14 13:7:23'
# v_cookie = ''
auth_refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=&g_vstk=706413966&g_actk=1653342293&callback=jQuery191011312253965308239_1626239258458&_=1626239258459'


Referer = 'https://v.qq.com'
Agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers_login = {
  'User-Agent': Agent,
  'Cookie': login_cookie,
  'Referer': Referer
}

resultContent = ''
vip_info = ''
endTime = ''
level = ''
vNumber = ''
upgrade_score = ''
upgrade_times = ''

# 测试一个签到请求
login = requests.get(auth_refresh_url, headers=headers_login)
cookie = requests.utils.dict_from_cookiejar(login.cookies)
# 如果请求返回信息包含no login说明cookie已经失效

if not cookie:
    print("auth_refresh error")
    resultContent = '获取Cookie失败，Cookie失效'
urls = [
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=下载签到请求',
    # 下载签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6&_=1582366326994&callback=赠送签到请求',
    # 赠送签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=签到请求',
    # 签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=弹幕签到请求',
    # 弹幕签到请求
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1&_=1582997048625&callback=观看60分钟签到',
    # 观看60分钟签到
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=payvip&cmd=1&otype=json&getannual=1&callback=会员信息',
    # 获取总会员信息
    'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_vscore_user_mashup&type=2&otype=xjson',
]
count = 0
score = 0

for url in urls:
    count += 1
    if (count == 1):
        print("发送每日下载任务请求")
        refresh_cookie = cookie['vqq_vusession']
        headers_signin = {
          'User-Agent': Agent,
          'Cookie': signin_cookie + refresh_cookie + ';vqq_vusession=' + refresh_cookie + ';',
          'Referer': Referer
        }
        response = requests.get(url=url, headers=headers_signin)
        responseContent = response.content.decode("utf-8")
        print(responseContent)
        resultContent += '> `' + responseContent + '`\n\n'
    elif (count == 2):
        print("发送每日赠片任务请求")
        refresh_cookie = cookie['vqq_vusession']
        headers_signin = {
          'User-Agent': Agent,
          'Cookie': signin_cookie + refresh_cookie + ';vqq_vusession=' + refresh_cookie + ';',
          'Referer': Referer
        }
        response = requests.get(url=url, headers=headers_signin)
        responseContent = response.content.decode("utf-8")
        print(responseContent)
        resultContent += '> `' + responseContent + '`\n\n'
    elif (count == 3):
        print("发送每日签到任务请求")
        refresh_cookie = cookie['vqq_vusession']
        headers_signin = {
          'User-Agent': Agent,
          'Cookie': signin_cookie + refresh_cookie + ';vqq_vusession=' + refresh_cookie + ';',
          'Referer': Referer
        }
        response = requests.get(url=url, headers=headers_signin)
        responseContent = response.content.decode("utf-8")
        print(responseContent)
        resultContent += '> `' + responseContent + '`\n\n'
    elif (count == 4):
        print("发送每日弹幕任务请求")
        refresh_cookie = cookie['vqq_vusession']
        headers_signin = {
          'User-Agent': Agent,
          'Cookie': signin_cookie + refresh_cookie + ';vqq_vusession=' + refresh_cookie + ';',
          'Referer': Referer
        }
        response = requests.get(url=url, headers=headers_signin)
        responseContent = response.content.decode("utf-8")
        print(responseContent)
        resultContent += '> `' + responseContent + '`\n\n'
    elif (count == 5):
        print("发送每日观影60分钟任务请求")
        refresh_cookie = cookie['vqq_vusession']
        headers_signin = {
          'User-Agent': Agent,
          'Cookie': signin_cookie + refresh_cookie + ';vqq_vusession=' + refresh_cookie + ';',
          'Referer': Referer
        }
        response = requests.get(url=url, headers=headers_signin)
        responseContent = response.content.decode("utf-8")

        print(responseContent)
        resultContent += '> `' + responseContent + '`\n\n'
    elif (count == 6):
        print("获取会员信息")
        headers_signin = {
          'User-Agent': Agent,
          'Cookie': signin_cookie + refresh_cookie + ';vqq_vusession=' + refresh_cookie + ';',
          'Referer': 'https://film.qq.com/'
        }
        response = requests.get(url=url, headers=headers_signin)
    
        vip_info = re.findall(r'[^()]+', response.content.decode("utf-8"))[1]
        #print(vip_info)

        rest = json.loads(vip_info)

        if (rest['level'] == 1) :
          upgrade_score = 600 - rest['score']
          upgrade_times = upgrade_score / 10

        elif ( rest['level'] == 2) :
          upgrade_score = 1800 - rest['score']
          upgrade_times = upgrade_score / 10

        elif (rest['level'] == 3) :
          upgrade_score = 3800 - rest['score']
          upgrade_times = upgrade_score / 10

        elif (rest['level'] == 4) :
          upgrade_score = 8000 - rest['score']
          upgrade_times = upgrade_score / 10

        elif (rest['level'] == 5) :
          upgrade_score = 16800 - rest['score']
          upgrade_times = upgrade_score / 10

        elif (rest['level'] == 6) :
          upgrade_score = 36800 - rest['score']
          upgrade_times = upgrade_score / 10

        elif (rest['level'] == 7) :
          upgrade_score = 53600 - rest['score']
          upgrade_times = upgrade_score / 10

        elif (rest['level'] == 8) :
          upgrade_score = 0
          upgrade_times = 0

        level = str(rest['level'])
        endTime = str(rest['endTime'])
        vNumber = str(rest['score'])

        print('会员等级：' + str(level))
        print('会员到期时间：' + str(endTime))
        print('当前V力值：' + str(vNumber))
        print('升到下一级还需' + str(upgrade_score) + 'V力值')
        print('升到下一级还需' + str(upgrade_times) + '天')
        #vip_info = rest
        #print(responseContent)
    
'''
企业微信机器人推送
'''
def wechat():
    if key == '':
        return
    headers = {"Content-Type": "text/plain"}
    # data = {
    #     "msgtype": "markdown",
    #     "markdown": {
    #         "content": "<font color=\"warning\">腾讯视频签到通知</font>\n" + '> 当前会员等级为：' + str(level) + '\n > 会员到期时间：' + str(endTime) + '\n > 当前V力值：' + str(vNumber) + '\n > 升到下一等级还需：' + str(upgrade_score) + 'V力值' + '\n > 预计升到下一等级还需' + str(upgrade_times) + '天 \n' + '\n 运行日志：\n' + resultContent + '\n 会员信息查询日志: \n > ' + vip_info
    #     }
    # }
    params = {
      "form":"text",
      "content": "<font color=\"warning\">腾讯视频签到通知</font>\n" + '> 当前会员等级为：' + str(level) + '\n > 会员到期时间：' + str(endTime) + '\n > 当前V力值：' + str(vNumber) + '\n > 升到下一等级还需：' + str(upgrade_score) + 'V力值' + '\n > 预计升到下一等级还需' + str(upgrade_times) + '天 \n' + '\n 运行日志：\n' + resultContent + '\n 会员信息查询日志: \n > ' + vip_info
    }

    # r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key, headers=headers, json=data)
    r = requests.post(url='https://iqybot.shuai2051.workers.dev/', params=params)
    data = json.loads(r.text)
    logging.info(r.text)
    if data['errmsg'] == 'ok':
        logging.info('企业微信机器人推送成功')
    else:
        logging.info('企业微信机器人推送失败,请检查key是否正确')
        
'''
消息推送
'''
wechat()
