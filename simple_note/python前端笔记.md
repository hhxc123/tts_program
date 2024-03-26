## 1.环境

```python
cmd跳转D盘
D:
使用指定python创建虚拟环境
D:\python39\python.exe -m venv D:\Users\Aa\Desktop\frontendtest\venv
激活该虚拟环境
D:\Users\Aa\Desktop\frontendtest\venv\Scripts\activate
pycharm指定即可
```

下载django包

```python
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 2.创建项目

```
pycharm中的terminal
django-admin startproject mydemo

启动
python mydemo\manage.py runserver
```

## 3.创建一个app文件夹

```python
python mydemo\manage.py startapp polls
```

```C++
主路由的setting
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polls",# 添加一个polls APP
]
```

```C++
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],# html放到了子路由polls的templates路径下
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

## 4.html页面

```html
创建到polls\templates路径下
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录界面</title>
</head>
<body>
<form action="/polls/index/" method="get">
    <p><label>用户名：</label><input name="user"/></p>
    <p><label>密码：</label><input name="pwd"/></p>
    <input type="submit" value="提交">
</form>
</body>
</html>
```

```html
创建到polls\templates路径下
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录界面</title>
</head>
<body>
<form action="/polls/index/" method="post">
    {% csrf_token %}
    <p><label>用户名：</label><input name="user"/></p>
    <p><label>密码：</label><input name="pwd"/></p>
    <input type="submit" value="提交">
</form>
</body>
</html>
```



## 5.实现函数

```python
# 在views.py中
def login_view(request):
    u = request.GET.get("user","")
    p = request.GET.get("pwd","")
    if u and p:
        return HttpResponse("登录成功")
    else:
        return HttpResponse("登录失败")
```







```
python synthesize.py --restore_step 900000 --mode single --dataset DailyTalk --text 'hello, my name is mingxuan jia.I come from shandong province.' --speaker_id 0
```



```
python synthesize.py --source preprocessed_data/DailyTalk/val_phone.txt --restore_step 900000 --mode batch --dataset DailyTalk
```

```
python synthesize.py --source D:\Users\Aa\Desktop\DailyTalk-main\output\result\DailyTalk\900000_guo\123\123.txt --restore_step '900000_guo' --mode batch --dataset DailyTalk
```



```python
batchs: [(
    ['hello, my name is mingxuan jia.I come from shandong province.'],
    ['hello, my name is mingxuan jia.I come from shandong province.'], 
    array([0]), 
    array([[106,  73, 117, 123, 357, 118,  86, 119, 102, 118, 108, 146, 118,
        108, 120, 116, 144,  66, 119, 115, 113,  73, 357,  86, 116,  74,
        118, 104,  97, 118, 132,  67, 119,  90, 123, 120, 129, 130,  66,
        143,  73, 119, 131]]),
    array([43]), 
    43, 
    None, 
    array([4]))
]
```





```
1.text_emb
D:\Users\Aa\Desktop\DailyTalk-main\preprocessed_data\DailyTalk\text_emb
2.生成格式
0_1_d23|1  可行

0_0_d23|0|{HH AH0 L OW1 sp M AY1 N EY1 M IH0 Z M IH0 NG K W AA1 N JH IY1 AH0 sp AY1 K AH1 M F ER0 M SH AA2 N D OW1 NG P R AA1 V AH0 N S S S S}|hello, my name is mingxuan jia.I come from shandong province.|none
```





```
Hello, nice to meet you! what is your name? where are you from?
Hello, nice to meet you too! my name is spartacus. I come from shandong province.
ohh! I know shandong province! That is a good place.
haha, thank you. By the way, do you like play badminton? Could you play with me?
Certainly! I also like this sport very much! Let us play this sport together!
```

```
['python', 'D:\\Users\\Aa\\Desktop\\DailyTalk-main\\synthesize.py', '--source', 'D:\\Users\\Aa\\Desktop\\DailyTalk-main\\output\\result\\DailyTalk\\900000
_guo\\123\\123.txt', '--restore_step', '900000_guo', '--mode', 'batch', '--dataset', 'DailyTalk']
```

```
python D:\\Users\\Aa\\Desktop\\DailyTalk-main\\synthesize.py --source D:\\Users\\Aa\\Desktop\\DailyTalk-main\\output\\result\\DailyTalk\\900000_guo\\123\\123.txt --restore_step '900000_guo' --mode batch --dataset DailyTalk
```



```
D:\Users\Aa\Desktop\DailyTalk-main\venv\Scripts
```







