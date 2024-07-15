网站内容的源文件放在 `master` 分支，生成的静态网页文件放在 `github-pages` 分支。


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
