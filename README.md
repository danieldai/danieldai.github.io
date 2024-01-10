# 欢迎访问 [DanielDai.com](http://www.danieldai.com)

**[DanielDai.com](http://www.danieldai.com)** 是使用 **[Pelican](http://getpelican.com/)** 生成的个人博客网站，**[Pelican](http://getpelican.com/)** 是使用 **[Python](http://python.org/)** 开发的静态网页网站生成工具。 

网站内容的源文件放在 `master` 分支，生成的静态网页文件放在 `github-pages` 分支。


## 怎么编辑这个博客 (给本人自己的笔记提示)

* 设置 venv 环境

在使用 Python 3 作为默认python的电脑
```
mkvirtualenv danieldai
```

在使用 Python 2 作为默认python的电脑
```
mkvirtualenv -p /usr/bin/python3 danieldai
```

```
git clone git@github.com:danieldai/danieldai.github.io.git
cd danieldai.github.io.git
pip install -r requirements.txt
```

安装插件 https://github.com/getpelican/pelican-plugins

* 在 `content` 目录创建新内容或者编辑已有内容文件
* 把内容源文件编译为 HTML 文件

```
make html
```

* 启动本地预览服务器

```
make devserver
```

* 用浏览器方位 http://localhost:8000 预览内容
  
* 把内容发布到 Github Pages

```
make github
```
