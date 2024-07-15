# 欢迎访问 [DanielDai.com](http://www.danieldai.com)

**[DanielDai.com](http://www.danieldai.com)** 是使用 **[Pelican](http://getpelican.com/)** 生成的个人博客网站，**[Pelican](http://getpelican.com/)** 是使用 **[Python](http://python.org/)** 开发的静态网页网站生成工具。 

网站内容的源文件放在 `master` 分支，生成的静态网页文件放在 `github-pages` 分支。


## 怎么编辑这个博客 (给本人自己的笔记提示)

* 设置 venv 环境 并安装依赖

在Linux 或者 Windows WSL 下运行如下命令
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

安装 Pelican 插件

在当前目录的上级目录运行如下命令
```
git clone --recursive https://github.com/getpelican/pelican-plugins
```

按如下方式配置 `PLUGIN_PATHS`
```
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap']
```


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
