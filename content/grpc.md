Title: gRPC
Date: 2021-09-23 22:20
Slug: grpc
Category: Go
Tags: gRPC, Python
Status: published


gRPC 是Google发起的一个开源远程过程调用系统。该系统基于HTTP/2 协议传输，使用Protocol Buffers 作为接口描述语言。 

其他功能： 

- 认证 
- 双向流 
- 流控制 
- 超时 
 
 最常见的应用场景是： 

- 微服务框架下，多种语言服务之间的高效交互。 
- 将手机服务、浏览器连接至后台 
- 产生高效的客户端库


## 在 Python 中使用 gRPC


### 环境要求

- Python 3.5 以上版本
- pip 9.0.1 以上版本

如果 pip 的版本太低，使用如下命令升级：

```bash
python -m pip install --upgrade pip
```

如果由于权限原因不能升级操作系统的pip, 可以使用virtualenv来运行这个示例。

```bash
python -m pip install virtualenv
virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

### gRPC

安装 gRPC

```bash
python -m pip install grpcio
```

或者全局安装：

```bash
sudo python -m pip install grpcio
```

### gRPC 工具

Python的gRPC工具包括protocol buffer编译器`protoc`, 以及从`.proto`服务定义文件生成服务器和客户端代码的特殊插件。对于快速入门示例的第一部分，我们已经从`helloworld.proto`生成了服务器和客户端的stub，但是你需要工具来完成我们的快速入门，以及以后的教程和你自己的项目。


使用下面的命令安装gRPC 工具：
```bash
python -m pip install grpcio-tools
```

### 下载示例

您需要把示例代码下载到本地来完成这个快速入门。从我们的GitHub存储库下载示例代码（以下命令克隆整个存储库，但您只需要这个快速入门和其他教程的示例）：

```bash
# Clone the repository to get the example code:
$ git clone -b v1.40.0 https://github.com/grpc/grpc
# Navigate to the "hello, world" Python example:
$ cd grpc/examples/python/helloworld
```

### 运行示例gRPC程序
在 `examples/python/helloworld` 文件夹:

运行服务器:

```bash
python greeter_server.py
```

在另一个终端中运行客服端:

```bash
python greeter_client.py
```

恭喜！你刚刚使用gRPC运行了一个客户端-服务器应用程序。

### 更新gRPC服务

现在让我们看看如何更新应用程序，在服务器上使用一个新的的方法来，以便客户端调用。我们的gRPC服务是使用protocol buffer定义的；你可以在gRPC和基础教程或者简介中找到更多关于如何在`.proto`文件中定义服务的信息。现在你只需要知道服务器和客户端“stub”都有一个SayHello RPC方法，它从客户端获取一个HelloRequest参数，从服务器返回一个HelloReply，这个方法是这样定义的：


```protobuf
// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

让我们更新一下，这样`Greeter`服务有两种方法。编辑`examples/protos/helloworld.proto`文件。在里面增加一个`SayHelloAgain`方法，它具有相同的请求和响应类型：

```protobuf
// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
  // Sends another greeting
  rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

记得保存文件。

### 生成gRPC 代码

现在我们需要更新我们的应用程序使用的gRPC代码，以便使用新的服务定义。

在 `examples/python/helloworld`目录运行：

```bash
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
```

这会生成`helloworld_pb2.py`和`helloworld_pb2_grpc.py`两个文件，第一个文件包含请求和应答类，第二个文件包含客户端和服务器类。

### 更新并运行应用程序

我们想在已经有了新生成的服务器和客户端代码，但是我们依然需要自己手工写代码来实现和调用新的方法。

```python
class Greeter(helloworld_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

  def SayHelloAgain(self, request, context):
    return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)
```

### 更新客户端

在同一个目录，打开 `greeter_client.py`文件，像下面这样调用新的方法：

```python
def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
  response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)
```

### 运行

想开始那样在`examples/python/helloworld`目录中:

运行服务器:

```bash
python greeter_server.py
```

在另一个终端中运行客户端：

```bash
python greeter_client.py
```
官方网站：https://grpc.io/