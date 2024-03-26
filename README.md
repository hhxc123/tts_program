# TTS项目使用操作手册

## 1.部署该项目

所需实验环境见requirements.txt，python环境3.7

## 2.启动django服务器

```
在终端中执行
python mydemo\manage.py runserver
```

## 3.输入账号密码

```
账号：0201123313
密码：123456
```

![image-20240326113652521](.\pictures\image-20240326113652521.png)

## 4.自动跳转到TTS界面

自行输入要合成语音的语句，系统将自动打开合成成功的文件夹，每条英文语句（按回车分割）都将合成一个wav保存的语音，同时您输入的语句可在“您的输入历史.txt”文件中查看到

![image-20240326113716941](.\pictures\image-20240326113716941.png)

![image-20240326113750868](.\pictures\image-20240326113750868.png)

## 5.演示视频

演示视频见video文件夹

## 6.相关笔记

配置django和git使用笔记保存到simple_note中

## 7.note

因GitHub限制大型文件的上传，请自行下载训练好的模型，下载网址：

```
https://drive.google.com/drive/folders/16-HcSkVhdziRVrG4WOtyb6wvDC5uQCKO?usp=drive_link
```

将所下载的模型放置于tts_program\output\ckpt\DailyTalk

同时若对训练过程感兴趣，欢迎下载训练日志，下载网址：

```
训练日志：https://drive.google.com/drive/folders/1enceunq5yNbXXrcNnRlzdLSbS0YdA-wC?usp=drive_link
验证日志：https://drive.google.com/drive/folders/10DxN84IlsShrio9w1iqVkILAdJKCPG8v?usp=drive_link
```

将训练日志和验证日志分别放到tts_program\output\log\DailyTalk下的train和val文件夹中