sec_config
==========

让程序的config信息加密存储，每次启动程序时手动输入密码解密config


#python
#使用方法：

修改`python/sec_config.py`文件里generate_sec_config函数里得config变量为你自己的config信息．
这是一个dict对象，够存很多config信息了，数据连接字符串，各种开发平台得KEY之类的．
填好了config，运行如下命令
```bash
python sec_config.py generate_sec_config

```

会产生sec_config
复制sec_config覆盖掉`python/sec_config.py`文件里start_sec_config函数里得sec_config．然后就可以在
```python
config = start_sec_config()
```
代码后面使用原始的config了，不过程序会在启动时要求输入生成sec_config时输入得key．如果输入错误，程序将无法启动．


#意义：
拖慢入侵者的脚步．这使得代码被窥视，重要信息也不会轻易被拿走．当然，dump内存，修改代码等下一次输入key等一系列绕过行为是必然存着得．

#不便：
服务器上程序挂了得手动上去启动，这对程序得鲁棒性是个挑战．

