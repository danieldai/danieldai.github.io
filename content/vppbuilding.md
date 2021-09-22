Title: 编译VPP
Date: 2021-09-15 22:20
Slug: vppbuilding
Category: VPP
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

## 错误处理
执行 `make run` 时发生如下错误：
```text
/vpp/build-root/install-vpp_debug-native/vpp/bin/vpp: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found
```

我是在Ubuntu 18.04上进行的实验，查看对应库的GLIBC版本发现最大支持到 `GLIBC_2.29`
```bash
$ strings /lib/x86_64-linux-gnu/libm.so.6 |grep GLIBC_
GLIBC_2.2.5
GLIBC_2.4
GLIBC_2.15
GLIBC_2.18
GLIBC_2.23
GLIBC_2.24
GLIBC_2.25
GLIBC_2.26
GLIBC_2.27
GLIBC_PRIVATE
```

为了继续实验，需要把glibm升级到 2.29

### 安装glibc-2.29

```bash
wget http://ftp.gnu.org/gnu/glibc/glibc-2.29.tar.gz 
tar -zxvf glibc-2.29.tar.gz
cd glibc-2.29
mkdir build
cd build
sudo apt install gawk bison
../configure --prefix=/opt/glibc-2.29
make
make install
```

glibc 软连接

安装完成后, 建立软链指向glibc-2.29, 执行如下命令:
```bash
rm -rf /lib/x86_64-linux-gnu/libm.so.6   //先删除之前的软连接

ln -s /opt/glibc-2.29/lib/libm-2.29.so  /lib/x86_64-linux-gnu/libm.so.6
```

英文源：https://fd.io/vppproject/vppbuilding/