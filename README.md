## CustAdmin

### 项目介绍
* 基于日常常用的CURD操作实现自定义admin示例Demo
* 开发环境: Django(1.11.4)+BootStrap
* 原理参考Django 自带的admin后台管理功能实现

### 目录结构
```
├── CustAdmin
│   ├── settings.py         # 配置文件
│   ├── urls.py             # 路由分发
│   ├── views.py            # 试图处理
├── README.md
├── app01
│   ├── admin.py            # admin后台
│   ├── arya.py             # arya组件使用
│   ├── models.py           # mondels模型
├── app02
│   ├── admin.py            # admin后台
│   ├── arya.py             # arya组件使用
│   ├── models.py           # models模型
├── arya
│   ├── apps.py             # 制作启动文件
│   ├── service     
│   │   └── v1.py           # arya组件核心逻辑
├── static                  # 静态文件
└── templates               # 模板文件
    ├── arya
    │   └── changelist.html
    ├── base.html
    ├── index.html
    └── login.html
```

### 使用说明
1. 确保本地已经安装python3.x + Django1.10.x以上版本环境
2. 拉取代码并运行程序
```
# git clone git@github.com:shuke163/CustAdmin.git
# cd CustAdmin/;python manage.py runserver
```
3. 浏览器访问
登陆: http://127.0.0.1:8000/login/
4. 测试账号
```
username: shuke password: 123
username: jack password: 123
username: tom  password: 123
```
5. 管理后台
管理: http://127.0.0.1:8000/admin/
登陆账号: username: admin password: admin!2345

### 原理
* 借鉴Django自带admin管理后台组件实现
* 理解Django程序在启动时加载的文件执行顺序，制作启动文件
* 利用python的单例模式和include原理实现URL的路由分发

### 组件引入
1. 在自己的project中导入arya组件包
2. 在project下的settings.py文件的配置项INSTALLED_APPS中注册arya组件(arya.apps.AryaConfig)
3. 在每个app应用下面创建arya.py文件，注册models模型，实现CURD操作

### 计划
* 完善CURD操作的前端展示UI
* 丰富arya组件的CURD功能,提高更灵活的定制化操作
* 结合RBAC组件使用