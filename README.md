# 设备管理系统

## 功能实现

用户登录注册：允许用户进行账号注册，并提供登录功能，以便用户登录系统进行操作。

设备列表显示：显示所有设备的列表，包括设备的基本信息，如名称、编号、型号等。

添加设备：允许用户添加新设备的信息。修改设备信息：允许用户修改已有设备的信息。

删除设备：允许用户删除已有设备的信息，从系统中移除设备记录。

设备查询：提供多种查询方式，如按设备名称、型号等进行查询，方便用户快速找到所需设备。

消息中心：用于接收设备借用的相关审批信息。

设备报废管理：允许管理员对设备进行报废操作，以及相关的处理流程。

设备借出管理：允许用户对设备进行借出操作，记录设备的借出时间、归还时间，以及借用者的信息，管理员可以对借出申请进行审批。

个人中心/修改资料：提供个人中心页面，允许用户查看和修改个人信息，如用户名、密码等。

## 开发技术

编程语言- 前端：HTML，CSS，JavaScript

后端：Python

数据库：MySQL

开发IDE：PyCharm、Visual Studio Code

Python 解释器：Python 3.8

Web 浏览器：Chrome

## 体系结构设计

### 系统架构

系统架构类型：本系统采用分层架构，共分为前端层、业务逻辑层和数据层三个主要层次。

架构模式：MVC（模型-视图-控制器）模式

技术栈：

​	前端：HTML, CSS, JavaScript

​	后端：Python, Django

​	数据库：MySQL

### 分层架构设计-前端层

​	功能：负责用户界面展示和用户交互。

​	技术：HTML, CSS, JavaScript

​	主要组件：登录注册页面、设备管理页面、设备查询页面等

### 分层架构设计-业务逻辑层

​	功能：处理业务逻辑，实现系统的核心功能。

​	技术：Python, Django

​	主要模块：

​		用户管理模块：处理用户注册、登录、权限控制。

​		设备管理模块：处理设备的添加、修改、删除。

​		设备查询模块：处理设备的查询功能。

​		设备借出模块：处理用户对设备的借用和管理员对申请的审批等功能。

​		设备报废模块：处理管理员对设备的报废。

​		消息中心模块：处理用户的借出申请以及管理员对申请的审批。

### 分层架构设计-数据层

​	功能：负责数据存储和管理。

​	技术：MySQL

​	主要表结构：

​		用户表：存储用户的基本信息和权限信息。

​		设备表：存储设备的详细信息。

​		借用记录表：记录设备的借用情况。

​		报废记录表：记录设备的报废情况。

### 模块间通信

前端与后端通过RESTful API进行通信，前端发送HTTP请求，后端返回JSON数据。

后端与数据库：使用Django ORM（对象关系映射）与MySQL数据库进行交互。

### 可扩展性与可维护性

模块化设计：每个功能模块独立开发，便于后续功能扩展和维护。

版本控制：使用Git进行版本控制，便于团队协作和代码管理。

代码规范：遵循Python编码规范和Django最佳实践，保证代码质量。
