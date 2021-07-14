# 腾讯视频会员V力值自动签到 - Actions
## 魔改版-原作者点这里[Demontisa/Tencent-Video-VIP-Actions](https://github.com/Demontisa/Tencent-Video-VIP-Actions)

<p align="center">
    <a href="https://github.com/Demontisa"><img alt="Author" src="https://img.shields.io/badge/author-Demontisa-blueviolet"/></a>
    <img alt="PHP" src="https://img.shields.io/badge/code-Python-success"/>
</p>
通过调用官方接口，每天上午 06 点，以及晚上 23 点自动触发，借此可以达到快速升级的目的。

一个账号平均耗时为3-5分钟左右。程序在GitHub Actions里自动运行不需要人工干预，每天自动领V力值，向你的企业微信发送任务通知。

------

## 准备

* `Fork` 本项目
* 注册`企业微信`


## 配置Actions secrets

1. 电脑打开浏览器访问`v.qq.com`，打开控制台(`F12`)、切换到Network，找到 `https://access.video.qq.com/user/auth_refresh` 的接口，把`Request URL:`后的地址都复制一下，然后点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`AUTH_REFRESH_URL` , `Value`值为`Request URL:后的地址`
例：
```
Request URL: https://access.video.qq.com/user/auth_refresh?vappid=1234567&vsecret=********&type=qq&g_tk=&g_vstk=********&g_actk=********&callback=jQuery191048649********_1575435********4&_=1575435********
```
`Value`值只取`https://access.video.qq.com/user/auth_refresh?vappid=1234567&vsecret=********&type=qq&g_tk=&g_vstk=********&g_actk=********&callback=jQuery191048649********_1575435********4&_=1575435********`


2. 依旧找到`https://access.video.qq.com/user/auth_refresh`这个接口，复制`Request Header`中的`cookie`，然后点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`LOGIN_COOKIE` , `Value`值为`Request Header中的cookie`

例：
```
cookie: RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; vqq_vusession=O1iwDP*****6ntxrWA..; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****
```
`Value`值只取`RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; vqq_vusession=O1iwDP*****6ntxrWA..; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****`

3. 复制第二步中的`cookie`，然后将`cookie`中的`vqq_vusession=O1iwDP*****6ntxrWA..;`删除，然后点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`SIGNIN_COOKIE` , `Value`值为`删除掉vqq_vusession=O1iwDP*****6ntxrWA..;`后的值

例：

去除前
```
RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; vqq_vusession=O1iwDP*****6ntxrWA..; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****
```

去除后
```
RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****
```
4. 点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`KEY` , `Value`值为[这个教程](https://hostloc.com/forum.php?mod=viewthread&tid=808429&highlight=CF%2B%2B%2Bworker)中的`CFworker链接`

## 启动Actions
1. 点击 `Actions` 再点击 `I understand my workflows, go ahead and enable them`
2. 首次使用需手动点击一次 `Start`
