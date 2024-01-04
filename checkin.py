import os
import requests

# 签到函数
def signin():
    # 创建会话
    session = requests.Session()

    # 发送登录请求
    login_url = 'https://sockboom.buzz/auth/login'
    login_data = {
        'email': os.environ.get('EMAIL'),
        'passwd': os.environ.get('PASSWD')
    }
    response = session.post(login_url, data=login_data)

    # 检查登录是否成功
    if response.status_code != 200:
        print('登录失败')
        return
    else:
        print('登陆成功')

    # 发送签到请求
    signin_url = 'https://sockboom.buzz/user/checkin'
    response = session.post(signin_url)

    # 检查签到是否成功
    if response.status_code != 200:
        print('签到失败')
        return

    # 打印签到结果
    print(eval(response.text)['msg'])

# 主函数
def main():
    # 执行签到
    print("\n--------------sockboom begin--------------")
    signin()
    print("--------------sockboom end--------------\n")

if __name__ == "__main__":
    main()
