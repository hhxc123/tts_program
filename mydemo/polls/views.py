from time import sleep
import sys,os
sys.path.append(r'D:\Users\Aa\Desktop\DailyTalk-main')
from django.http import HttpResponse
from django.shortcuts import render
from generate_test_text import gen_text
import subprocess

# Create your views here.

def toLogin_view(request):
    # 渲染一个html页面
    return render(request, 'login.html')


def login_view(request):
    # u = request.GET.get("user","")
    # p = request.GET.get("pwd","")
    u = request.POST.get("user", "")
    p = request.POST.get("pwd", "")
    print(u, p)
    if u=='0201123313' and p=="123456":
        #return HttpResponse("登录成功")
        print("登录成功")
        return render(request, 'login_success.html')
    else:
        return HttpResponse("登录失败")


def to_tts(request):
    text = request.POST.get("text", "nothing")
    if text == "nothing":
        return render(request, 'tts.html')
    else:
        gen_text(text)

    # 定义要执行的命令和参数
    command = [r'D:\Users\Aa\Desktop\DailyTalk-main\venv\Scripts\python.exe', r'D:\Users\Aa\Desktop\DailyTalk-main\synthesize.py']
    arguments = [
        '--source', r'D:\Users\Aa\Desktop\DailyTalk-main\output\result\DailyTalk\900000_guo\123\123.txt',
        '--restore_step', '900000_guo',
        '--mode', 'batch',
        '--dataset', 'DailyTalk'
    ]

    # 将命令和参数合并为一个列表
    full_command = command + arguments
    print("完整命令是：", full_command)
    # 使用 subprocess 执行命令
    try:
        process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()  # 这会阻塞直到进程完成
        if process.returncode != 0:
            print(f"合成失败，错误信息：{stderr.decode()}")
        else:
            print("合成成功！")
        os.startfile(r'D:\Users\Aa\Desktop\DailyTalk-main\output\result\DailyTalk\900000_guo\123')
    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，会抛出 CalledProcessError 异常
        print(f"合成失败，错误信息：{e}")

    return render(request, 'tts.html')
