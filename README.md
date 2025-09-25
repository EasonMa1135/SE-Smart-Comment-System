
# 本地运行说明

## 所需环境

1. Node.js
2. npm (cnpm)
3. python3.x
4. conda
5. MySQL80

## 文件结构

1. backend 为后端程序文件夹
2. database 为数据库建表脚本文件夹
3. frontend 为前端文件夹

## 技术栈

1. 数据库使用 MySQL
2. 后端使用 Flask 的后端框架 + SqlAlchemy 的 ORM 工具
3. 前端使用 Vue 的前端框架 + vuex 状态管理 + vuetify 的 UI 组件库 + vite 构建工具 + axios 网络请求库 + echarts 可视化图表库

## 运行步骤

1. 数据库建立
   * 在 MySQL Workbench 8.0 CE 中根据需要使用密码登录用户，需要在后续修改 ./backend/config.py 中用户名密码的相关配置
   * 执行 ./database/create.sql 脚本
2. 后端启动
   * `cd backend` 进入后端文件夹
   * 根据需要修改 config.py 中连接数据库的用户名和密码
   * 执行命令 `conda create --name bs_flask python=3.10.13` 此处 python 版本可根据需要替换
   * 重启终端后执行命令 `conda activate bs_flask` 开启虚拟环境
   * 执行命令 `pip3 install -r requirements.txt` 下载所需库
   * 执行命令 `python app.py` 运行后端程序
3. 前端启动
   * `cd frontend` 进入前端
   * `npm install` 安装所需库
   * `npm run dev` 可运行在本地，在宿主机的 <http://localhost:8888> 访问本网站
   * 或使用 `npm run build` 并 `npm run preview` 可查看构建生产版本，根据终端输出的提示确定端口，以访问本网站
