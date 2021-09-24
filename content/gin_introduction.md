Title: Gin简介
Date: 2021-09-13 22:20
Slug: gin-introduction
Category: Post
Tags: Golang, Go

# 一、简单介绍

Gin 是一个用 Go (Golang) 编写的 Web 框架。 它具有类似 martini 的 API，但是具有更好的性能； 得益于httprouter，它速度提高了 40 倍。 如果ni需要性能和良好的生产力，你会喜欢上 Gin 的。

在本节中，我们将介绍什么是 Gin，它解决了什么问题，以及它如何帮助您的项目。

或者，如果您准备在项目中使用 Gin，请访问快速入门。

## Gin的特点

### 速度快
基于基数树(Radix tree)的路由，内存占用小。没有使用反射。API性能可以预测。

### 支持中间件
传入的 HTTP 请求可以由一系列中间件和最终处理动作。 例如：Logger、Authorization、GZIP， 最后向数据库发送一条信息。

### 不会崩溃
Gin 可以捕获 HTTP 请求期间发生的错误并恢复它。 这样，您的服务器将始终可用。 还可以向 Sentry 报告此错误！

### JSON验证
Gin 可以解析和验证请求的 JSON - 例如，检查所需值的是否存在。

### 路由分组
使用分组可以更好地组织路由。 把需要授权与不需要授权或者不同的 API 版本放在不同的分组。更好的是分组可以无限嵌套，而不会降低性能。

### 错误管理
Gin 提供了一种方便的方法来收集 HTTP 请求期间发生的所有错误。 最终，中间件可以将它们写入日志文件、数据库并通过网络发送它们。

### 内置渲染
Gin 为 JSON、XML 和 HTML 渲染提供了一个易于使用的 API。

### 可扩展
创建一个新的中间件非常简单，只需查看示例代码即可。


# 二、快速入门

## 环境要求

Go 1.13 以上版本

## 安装并验证

要安装 Gin 包，您需要先安装 Go 并设置您的 Go 工作区。

1. 下载并安装:

```bash
$ go get -u github.com/gin-gonic/gin
```
1. 在代码中import:

```go
import "github.com/gin-gonic/gin"
```

1. 如果要使用`http.StatusOK`之类的常量，还需要`import net/http`

```go
import "net/http"
```

1. 创建工程目录，然后`cd`到该目录。

```bash
mkdir -p $GOPATH/src/github.com/danieldai/gin_poc && cd "$_"
```

2. 把模板代码复制到这个文件中。


```bash
$ curl https://raw.githubusercontent.com/gin-gonic/examples/master/basic/main.go > main.go
```

3. 运行工程看看是否工作正常

```bash
$ go run main.go
```

## 开始使用

首先，创建一个文件名为`example.go`的文件:

```bash
$ touch example.go
```

然后，把下面的代码输入到`example.go`中:

```go
package main

import "github.com/gin-gonic/gin"

func main() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run() // 在 0.0.0.0:8080 上监听、服务
}
```

最后，使用如下命令来运行代码:

```bash
# 运行 example.go 并在浏览器里访问 localhost:8080/ping
$ go run example.go
```