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