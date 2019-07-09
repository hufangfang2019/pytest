import pytest

def test_login():
    print("正在登录")

if __name__ == '__main__':
    # pytest.main("-s login.py")
    pytest.main(["-s","login.py"])
# .通过
# F不通过

# pytest 运行方式
# -命令行(用的多)
# pytest -s login.py
# -代码
# pytest.main("-s login.py")

# 如何快速打开终端并进入当前项目目录
# 控制台下方，有一个terminal

# 补充：如果快速进入测试python代码的程序（ipython)
# python Console