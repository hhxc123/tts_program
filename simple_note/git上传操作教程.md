```
1.在本地文件夹中加载github的原项目 克隆远程仓库
git clone https://github.com/hhxc123/tts_program.git
（若提示SSL证书有问题则执行 git config --global http.sslVerify false）
2.加载到了tts_program
需要更改的操作都在这个tts_program文件夹中进行
3.cd tts_program//输入该远程仓库名
4.git init 初始化git
5.git add . //当前目录下的所有文件放到缓存区，也可放入要修改的文件夹
6.git commit -m "提供注释信息"
7.git push  //提交到远程仓库
```



```C++
Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video
$ git clone https://github.com/hhxc123/tts_program.git
Cloning into 'tts_program'...
fatal: unable to access 'https://github.com/hhxc123/tts_program.git/': SSL certi
ficate problem: unable to get local issuer certificate

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video
$ git config --global http.sslVerify false

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video
$ git clone https://github.com/hhxc123/tts_program.git
Cloning into 'tts_program'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), 7.51 MiB | 53.04 MiB/s, done.

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video
$ cd tts_program

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git init
Reinitialized existing Git repository in D:/Users/Aa/Desktop/video/tts_program/.
git/

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git add .

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git commit -m "提交视频"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Aa@LAPTOP-DDB9ESPB.(none)')

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git config --global user.email "1837688993@qq.com"

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git config --global user.name "hhxc123"

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git commit -m "提交视频"
[main a7230d6] 提交视频
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename my_tts_program_show.mp4 => video/my_tts_program_show.mp4 (100%)

Aa@LAPTOP-DDB9ESPB MINGW64 /d/Users/Aa/Desktop/video/tts_program (main)
$ git push
warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more i
nformation.
info: please complete authentication in your browser...
warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more i
nformation.
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (1/1), done.
Writing objects: 100% (2/2), 235 bytes | 235.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/hhxc123/tts_program.git
   9ddcbe2..a7230d6  main -> main
```

