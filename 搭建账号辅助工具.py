import random
import os
import zipfile

jiaoben_path = os.getcwd()

js_str = """export default {
  async fetch(request, env) {
    let url = new URL(request.url);
    if (url.pathname.startsWith('/')) {
      url.hostname = ''
      let new_request = new Request(url, request);
      return fetch(new_request);
    }
    return env.ASSETS.fetch(request);
  },
};"""


def choose_path():
    choose = input("1、将文件保存到脚本旁边\n2、将文件保存到自定义路径\n请输入编号：").strip()

    if not choose.isdigit():
        print("不合法的输入，请输入编号！")

    if choose == '1':
        flie_path = jiaoben_path
        return flie_path

    elif choose == '2':
        inp_path = input("请输入保存路径；").strip().replace('"', '')
        return inp_path

    else:
        print("没有此选项！")


def js_file():  # 创建js文件函数
    ym = input("请输入原始域名：")

    # 创建js文件
    js_str1 = js_str[0:145]
    js_str2 = js_str[145:]
    js_workers = js_str1 + ym + js_str2
    f = open("_worker.js", 'w', encoding='utf-8')
    f.write(js_workers)
    f.close()

    # 将js文件压缩成zip
    server_path = choose_path() # 询问保存在哪里
    server_worker_path = os.path.join(server_path, "_worker.zip")   # 定义路径
    js_file_path = os.path.join(jiaoben_path, '_worker.js')
    worker = zipfile.ZipFile(server_worker_path, 'w')    # 创建ZIP文件
    worker.write(js_file_path, '_worker.js', zipfile.ZIP_DEFLATED)   # 将指定文件写入zip文件中
    worker.close()
    os.remove('_worker.js') # 压缩后删除js文件
    os.system("clear")
    print("创建成功！")
    print()


def func_uuid():    # 随机生成UUID
    num_uuid = int(input("请输入生成数量：").strip())
    print()
    os.system("clear")
    for i in range(num_uuid):
        uuid_format = "0123456789abcdef0123456789abcdef0123456789abcdef"
        uuid_str = "".join(random.sample(uuid_format, 28))
        uuid = f"{uuid_str[0:8]}-{uuid_str[8:12]}-{uuid_str[12:16]}-{uuid_str[16:28]}"
        print(uuid)
    print()


func_dic = {
    '0': ['退出'],
    '1':  ['创建js文件'],
    '2': ['生成UUID'],
}   # 所有功能信息

while True:
    # 第一批功能
    print('----------欢迎使用搭建账号辅助工具！----------')
    for k in func_dic:
        print('\t', "[%s]" % k, func_dic[k][0])
    print("----------------------------------------")
    choose = input("请输入命令编号：").strip()

    if not choose.isdigit():
        print("请输入命令编号！")

    if choose == "0":
        break
    elif choose == "1":
        js_file()
    elif choose == "2":
        func_uuid()
    else:
        print("没有此选项，如果你需要什功能的话请反馈给开发人员")