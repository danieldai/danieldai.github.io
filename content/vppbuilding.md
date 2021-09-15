Title: 编译VPP
Date: 2021-09-15 22:20
Slug: vppbuilding
Category: Post
Tags: VPP, 矢量报文处理
Status: published


# 如何下载和构建VPP

下面介绍了如何下载和构建VPP。

## 设置代理

根据您操作的环境，可能需要设置代理。运行这些代理命令来指定代理服务器名称和相应的端口号：

```bash
$ export http_proxy=http://<proxy-server-name>.com:<port-number>
$ export https_proxy=https://<proxy-server-name>.com:<port-number>
```

## 获取VPP源代码
要获取用于创建构建的VPP源代码，请运行以下命令：

```bash
$ git clone https://gerrit.fd.io/r/vpp
$ cd vpp
```

## 构建VPP依赖关系
运行以下make命令来安装VPP的依赖项。

如果下载时发生挂起，那么您可能需要先按第一步设置代理才能正常下载。

```bash
$ make install-dep
```

## 构建VPP（发布版本）

使用下面的make命令构建VPP的发布版本。

```bash
$ make build-release
```

## 运行VPP
构建VPP二进制文件后，您现在已经构建了几个镜像。使用以下命令运行VPP

```bash
$ sudo bash
# make run
```

英文源：https://fd.io/vppproject/vppbuilding/