---
title: "扩展"
sidebar_position: 6
---

# A2A 中的扩展

智能体到智能体（A2A）协议为智能体间通信提供了坚实的基础。然而，特定领域或高级用例通常需要超出通用方法的额外结构、自定义数据或新的交互模式。扩展是 A2A 在基础协议上分层新能力的强大机制。

扩展允许使用新数据、要求、RPC 方法和状态机来扩展 A2A 协议。智能体在其智能体卡片中声明对特定扩展的支持，然后客户端可以选择加入扩展提供的行为，作为向智能体发出的请求的一部分。扩展由 URI 标识并由其自己的规范定义。任何人都可以定义、发布和实现扩展。

扩展的灵活性允许在不分裂核心标准的情况下自定义 A2A，促进创新和特定领域的优化。

## 扩展的范围

扩展可能使用方式的确切集合有意设计得很广泛，以便能够将 A2A 扩展到已知用例之外。然而，一些可预见的应用包括：

- **仅数据扩展**：在智能体卡片中公开新的结构化信息，而不影响请求-响应流程。例如，扩展可以添加关于智能体 GDPR 合规性的结构化数据。
- **配置文件扩展**：在核心请求-响应消息上叠加额外的结构和状态更改要求。此类型实际上充当核心 A2A 协议的配置文件，缩小允许值的空间（例如，要求所有消息使用遵守特定模式的 `DataParts`）。这还可以包括通过使用元数据来增强任务状态机中的现有状态。例如，扩展可以在 `TaskStatus.state` 为 'working' 且 `TaskStatus.message.metadata["generating-image"]` 为 true 时定义 'generating-image' 子状态。
- **方法扩展（扩展技能）**：在协议定义的核心集合之外添加全新的 RPC 方法。扩展技能是指智能体通过实现定义新 RPC 方法的扩展而获得或公开的能力或功能。例如，`task-history` 扩展可能添加 `tasks/search` RPC 方法来检索先前任务的列表，有效地为智能体提供新的扩展技能。
- **状态机扩展**：向任务状态机添加新状态或转换。

## 示例扩展列表

| 扩展 | 描述 |
| :-------- | :------------ |
| [安全护照扩展](https://github.com/a2aproject/a2a-samples/tree/main/extensions/secure-passport) | 添加受信任的上下文层，以实现即时个性化并减少开销（v1）。 |
| [Hello World 或时间戳扩展](https://github.com/a2aproject/a2a-samples/tree/main/extensions/timestamp) | 一个简单的扩展，演示如何通过向 `Message` 和 `Artifact` 对象的 `metadata` 字段添加时间戳来增强基础 A2A 类型（v1）。 |
| [可追溯性扩展](https://github.com/a2aproject/a2a-samples/tree/main/samples/python/extensions/traceability) | 探索可追溯性扩展的 Python 实现和基本用法（v1）。 |
| [智能体网关协议（AGP）扩展](https://github.com/a2aproject/a2a-samples/tree/main/extensions/agp) | 核心协议层或路由扩展，引入自主小队（ASq）并根据声明的能力路由意图有效载荷，增强可扩展性（v1）。 |

## 限制

扩展不允许对协议进行某些更改，主要是为了防止破坏核心类型验证：

- **更改核心数据结构的定义**：例如，向协议定义的数据结构添加新字段或删除必需字段）。扩展应将自定义属性放在核心数据结构上存在的 `metadata` 映射中。
- **向枚举类型添加新值**：扩展应使用现有枚举值，并在 `metadata` 字段中注释额外的语义含义。

## 扩展声明

智能体通过在其 `AgentCapabilities` 对象中包含 `AgentExtension` 对象来在其智能体卡片中声明对扩展的支持。

```ts { .no-copy }
--8<-- "types/src/types.ts:AgentExtension"
```

以下是带有扩展的智能体卡片示例：

```json
{
  "name": "Magic 8-ball",
  "description": "An agent that can tell your future... maybe.",
  "version": "0.1.0",
  "url": "https://example.com/agents/eightball",
  "capabilities": {
    "streaming": true,
    "extensions": [
      {
        "uri": "https://example.com/ext/konami-code/v1",
        "description": "Provide cheat codes to unlock new fortunes",
        "required": false,
        "params": {
          "hints": [
            "When your sims need extra cash fast",
            "You might deny it, but we've seen the evidence of those cows."
          ]
        }
      }
    ]
  },
  "defaultInputModes": ["text/plain"],
  "defaultOutputModes": ["text/plain"],
  "skills": [
    {
      "id": "fortune",
      "name": "Fortune teller",
      "description": "Seek advice from the mystical magic 8-ball",
      "tags": ["mystical", "untrustworthy"]
    }
  ]
}
```

## 必需扩展

虽然扩展通常提供可选功能，但某些智能体可能有更严格的要求。当智能体卡片将扩展声明为 `required: true` 时，它向客户端发出信号，表明扩展的某些方面会影响请求的结构或处理方式，并且客户端必须遵守它。智能体不应将仅数据扩展标记为必需。如果客户端不请求激活必需扩展，或未能遵循其协议，智能体应使用适当的错误拒绝传入请求。

## 扩展规范

扩展的详细行为和结构由其**规范**定义。虽然没有强制规定确切的格式，但它至少应包含：

- 标识扩展的特定 URI。
- `AgentExtension` 对象的 `params` 字段中指定的对象的模式和含义。
- 客户端和智能体之间通信的任何其他数据结构的模式。
- 实现扩展所需的新请求-响应流程、附加端点或任何其他逻辑的详细信息。

## 扩展依赖

扩展可能依赖于其他扩展。这可以是必需的依赖项（扩展没有依赖项就无法运行）或可选的依赖项（如果存在另一个扩展，则启用附加功能）。扩展规范应记录这些依赖项。客户端有责任激活扩展及其扩展规范中列出的所有必需依赖项。

## 扩展激活

扩展默认为非活动状态，为不支持扩展的客户端提供基准体验。客户端和智能体执行协商以确定哪些扩展对特定请求处于活动状态。

1. **客户端请求**：客户端通过在对智能体的 HTTP 请求中包含 `A2A-Extensions` 标头来请求扩展激活。该值是客户端打算激活的扩展 URI 的逗号分隔列表。
2. **智能体处理**：智能体负责识别请求中支持的扩展并执行激活。智能体可以忽略任何不支持的请求扩展。
3. **响应**：一旦智能体识别了所有激活的扩展，响应应该包含 `A2A-Extensions` 标头，列出为该请求成功激活的所有扩展。

![A2A 扩展流程图](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Screenshot_2025-09-04_at_13.03.31.original.png)

**显示扩展激活的示例请求：**

```http
POST /agents/eightball HTTP/1.1
Host: example.com
Content-Type: application/json
A2A-Extensions: https://example.com/ext/konami-code/v1
Content-Length: 519
{
  "jsonrpc": "2.0",
  "method": "message/send",
  "id": "1",
  "params": {
    "message": {
      "kind": "message",
      "messageId": "1",
      "role": "user",
      "parts": [{"kind": "text", "text": "Oh magic 8-ball, will it rain today?"}]
    },
    "metadata": {
      "https://example.com/ext/konami-code/v1/code": "motherlode"
    }
  }
}
```

**回显激活扩展的相应响应：**

```http
HTTP/1.1 200 OK
Content-Type: application/json
A2A-Extensions: https://example.com/ext/konami-code/v1
Content-Length: 338
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "kind": "message",
    "messageId": "2",
    "role": "agent",
    "parts": [{"kind": "text", "text": "That's a bingo!"}]
  }
}
```

## 实施注意事项

虽然 A2A 协议定义了扩展的功能，但本节提供了有关其实施的指导——编写、版本控制和分发扩展实施的最佳实践。

- **版本控制**：扩展规范会演变。拥有清晰的版本控制策略至关重要，以确保客户端和智能体可以协商兼容的实现。
    - **建议**：使用扩展的 URI 作为主要版本标识符，理想情况下包括版本号（例如，`https://example.com/ext/my-extension/v1`）。
    - **破坏性更改**：在对扩展的逻辑、数据结构或必需参数引入破坏性更改时，必须使用新的 URI。
    - 处理不匹配：如果客户端请求智能体不支持的版本，智能体应该忽略该扩展的激活请求；它不得回退到不同的版本。
- **可发现性和发布**：
    - **规范托管**：扩展规范文档**应该**托管在扩展的 URI 上。
    - **永久标识符**：鼓励作者为其扩展 URI 使用永久标识符服务，例如 `w3id.org`，以防止链接断开。
    - **社区注册表（未来）**：A2A 社区可能会在未来建立一个中央注册表，用于发现和浏览可用的扩展。
- **打包和可重用性（A2A SDK 和库）**：
    为了促进采用，扩展逻辑应打包到可重用的库中，这些库可以集成到现有的 A2A 客户端和服务器应用程序中。
    - 扩展实现应作为其语言生态系统的标准包分发（例如，Python 的 PyPI 包、TypeScript/JavaScript 的 npm 包）。
    - 目标是为开发者提供流畅的集成体验。设计良好的扩展包应允许开发者使用最少的代码将其添加到服务器，例如：

        ```python
        --8<-- "https://raw.githubusercontent.com/a2aproject/a2a-samples/refs/heads/main/samples/python/agents/adk_expense_reimbursement/__main__.py"
        ```

        此示例展示了 A2A SDK 或库（例如 Python 中的 `a2a.server`）如何促进 A2A 智能体和扩展的实现。

- **安全性**：扩展修改了 A2A 协议的核心行为，因此引入了新的安全考虑：

    - **输入验证**：必须严格验证扩展引入的任何新数据字段、参数或方法。将来自外部方的所有与扩展相关的数据视为不受信任的输入。
    - **必需扩展的范围**：在智能体卡片中将扩展标记为 `required: true` 时要小心。这会为所有客户端创建硬依赖项，并且应仅用于对智能体的核心功能和安全性至关重要的扩展（例如，消息签名扩展）。
    - **身份验证和授权**：如果扩展添加新方法，实现必须确保这些方法受到与核心 A2A 方法相同的身份验证和授权检查。扩展不得提供绕过智能体主要安全控制的方法。

有关更多信息，请参阅 [A2A 扩展：赋能自定义智能体功能](https://developers.googleblog.com/en/a2a-extensions-empowering-custom-agent-functionality/)博客文章。
