---
title: "任务的生命周期"
sidebar_position: 5
---

# 任务的生命周期

在智能体到智能体（A2A）协议中，交互的范围可以从简单的无状态交换到复杂的长时间运行的进程。当智能体从客户端接收消息时，它可以以两种基本方式之一进行响应：

- **使用无状态 `Message` 响应**：此类型的响应通常用于立即的、自包含的交互，无需进一步的状态管理即可结束。
- **启动有状态 `Task`**：如果响应是 `Task`，智能体将通过定义的生命周期处理它，根据需要传达进度并要求输入，直到它达到中断状态（例如，`input-required`、`auth-required`）或终止状态（例如，`completed`、`canceled`、`rejected`、`failed`）。

## 对相关交互进行分组

`contextId` 是一个关键标识符，用于逻辑地将多个 `Task` 对象和独立的 `Message` 对象分组，为一系列交互提供连续性。

- 当客户端第一次发送消息时，智能体会响应一个新的 `contextId`。如果启动了任务，它还将具有 `taskId`。
- 客户端可以发送后续消息并包含相同的 `contextId`，以表示它们正在同一上下文中继续之前的交互。
- 客户端可选地将 `taskId` 附加到后续消息，以表示它继续该特定任务。

`contextId` 使多个、可能并发的任务能够朝着共同目标或共享上下文会话进行协作。在内部，A2A 智能体（尤其是使用 LLM 的智能体）使用 `contextId` 来管理其内部对话状态或其 LLM 上下文。

## 智能体响应：消息或任务

在使用 `Message` 或 `Task` 进行响应之间的选择取决于交互的性质和智能体的能力：

- **用于简单交互的消息**：`Message` 对象适用于不需要长时间运行处理或复杂状态管理的事务性交互。智能体可能会使用消息在提交到 `Task` 对象之前协商任务的接受或范围。
- **用于有状态交互的任务**：一旦智能体将传入消息的意图映射到需要在较长时间内进行大量可跟踪工作的受支持能力，智能体就会用 `Task` 对象进行响应。

从概念上讲，智能体以不同的复杂性级别运行：

- **仅消息智能体**：始终使用 `Message` 对象响应。它们通常不管理复杂状态或长时间运行的执行，并使用 `contextId` 将消息联系在一起。这些智能体可能直接包装 LLM 调用和简单工具。
- **生成任务的智能体**：始终使用 `Task` 对象响应，即使对于响应也是如此，然后将其建模为已完成的任务。一旦创建任务，智能体将仅返回 `Task` 对象以响应发送的消息，并且一旦任务完成，就无法再发送消息。这种方法避免了在 `Task` 与 `Message` 之间做出决定，但即使对于简单的交互也会创建已完成的任务对象。
- **混合智能体**：生成 `Message` 和 `Task` 对象。这些智能体使用消息来协商智能体能力和任务的工作范围，然后发送 `Task` 对象来跟踪执行并管理诸如 `input-required` 或错误处理之类的状态。一旦创建任务，智能体将仅返回 `Task` 对象以响应发送的消息，并且一旦任务完成，就无法再发送消息。混合智能体使用消息来协商任务的范围，然后生成任务来跟踪其执行。
    有关混合智能体的更多信息，请参阅 [A2A 协议：揭秘任务与消息](https://discuss.google.dev/t/a2a-protocol-demystifying-tasks-vs-messages/255879)。

## 任务细化

客户端经常需要根据任务结果发送新请求或细化先前任务的输出。这通过使用与原始任务相同的 `contextId` 开始另一个交互来建模。客户端通过在 `Message` 对象中使用 `referenceTaskIds` 提供对原始任务的引用来进一步提示智能体。然后，智能体使用新的 `Task` 或 `Message` 进行响应。

## 任务不可变性

一旦任务达到终止状态（已完成、已取消、已拒绝或失败），它就无法重新启动。与该任务相关的任何后续交互（例如细化）必须在同一 `contextId` 内启动新任务。这一原则提供了几个好处：

- **任务不可变性。** 客户端可靠地引用任务及其关联的状态、制品和消息，提供输入到输出的清晰映射。这对于编排和可追溯性很有价值。
- **明确的工作单元。** 每个新请求、细化或跟进都成为一个不同的任务。这简化了记录保存，允许对智能体的工作进行细粒度跟踪，并使每个制品都能跟踪到特定的工作单元。
- **更容易实施。** 这消除了智能体开发者关于是创建新任务还是重新启动现有任务的歧义。

## 并行跟进

A2A 通过使智能体能够为在同一 `contextId` 内发送的每条跟进消息创建不同的并行任务来支持并行工作。这允许客户端跟踪单个任务，并在先决条件任务完成后立即创建新的依赖任务。

例如：

- 任务 1：预订飞往赫尔辛基的航班。
- 任务 2：基于任务 1，预订酒店。
- 任务 3：基于任务 1，预订雪地摩托活动。
- 任务 4：基于任务 2，向酒店预订添加水疗预订。

## 引用先前的制品

服务智能体从引用的任务或从 `contextId` 推断相关制品。作为领域专家，服务智能体最适合解决歧义或识别缺失信息。如果存在歧义，智能体会通过返回 `input-required` 状态向客户端请求澄清。然后，客户端在其响应中指定制品，可选地在 `Part` 元数据中填充制品引用（`artifactId`、`taskId`）。

## 跟踪制品变更

跟进或细化任务通常会导致基于旧制品创建新制品。跟踪这些变更很重要，以确保在后续交互中仅使用制品的最新版本。这可以概念化为版本历史，其中每个新制品都链接到其前身。

但是，客户端处于管理此制品链接的最佳位置。客户端确定什么构成可接受的结果，并有能力接受或拒绝新版本。因此，服务智能体不应负责跟踪制品变更，此链接不是 A2A 协议规范的一部分。客户端应在其端维护此版本历史记录，并向用户呈现最新的可接受版本。

为了便于客户端跟踪，服务智能体在生成现有制品的细化版本时应使用一致的 `artifact-name`。

在启动跟进或细化任务时，客户端应明确引用他们打算细化的特定制品，理想情况下是从他们的角度来看的"最新"版本。如果未提供制品引用，服务智能体可以：

- 尝试根据当前 `contextId` 推断预期制品。
- 如果存在歧义或上下文不足，智能体应使用 `input-required` 任务状态进行响应，以请求客户端澄清。

## 跟进场景示例

以下示例说明了带有跟进的典型任务流程：

1. 客户端向智能体发送消息：

    ```json
    {
      "jsonrpc": "2.0",
      "id": "req-001",
      "method": "message.send",
      "params": {
        "message": {
          "role": "user",
          "parts": [
            {
              "text": "Generate an image of a sailboat on the ocean."
            }
          ],
          "messageId": "msg-user-001"
        }
      }
    }
    ```

2. 智能体使用帆船图像响应（已完成的任务）：

    ```json
    {
      "jsonrpc": "2.0",
      "id": "req-001",
      "result": {
        "id": "task-boat-gen-123",
        "contextId": "ctx-conversation-abc",
        "status": {
          "state": "completed"
        },
        "artifacts": [
          {
            "artifactId": "artifact-boat-v1-xyz",
            "name": "sailboat_image.png",
            "description": "A generated image of a sailboat on the ocean.",
            "parts": [
              {
                "file": {
                  "name": "sailboat_image.png",
                  "mediaType": "image/png",
                  "fileWithBytes": "base64_encoded_png_data_of_a_sailboat"
                }
              }
            ]
          }
        ]
      }
    }
    ```

3. 客户端要求将船涂成红色。此细化请求引用先前的 `taskId` 并使用相同的 `contextId`。

    ```json
    {
      "jsonrpc": "2.0",
      "id": "req-002",
      "method": "message.send",
      "params": {
        "message": {
          "role": "user",
          "messageId": "msg-user-002",
          "contextId": "ctx-conversation-abc",
          "referenceTaskIds": [
            "task-boat-gen-123"
          ],
          "parts": [
            {
              "text": "Please modify the sailboat to be red."
            }
          ]
        }
      }
    }
    ```

4. 智能体使用新的图像制品响应（新任务，相同上下文，相同制品名称）：智能体在同一 `contextId` 内创建新任务。新的帆船图像制品保留相同的名称，但具有新的 `artifactId`。

    ```json
    {
      "jsonrpc": "2.0",
      "id": "req-002",
      "result": {
        "id": "task-boat-color-456",
        "contextId": "ctx-conversation-abc",
        "status": {
          "state": "completed"
        },
        "artifacts": [
          {
            "artifactId": "artifact-boat-v2-red-pqr",
            "name": "sailboat_image.png",
            "description": "A generated image of a red sailboat on the ocean.",
            "parts": [
              {
                "file": {
                  "name": "sailboat_image.png",
                  "mediaType": "image/png",
                  "fileWithBytes": "base64_encoded_png_data_of_a_RED_sailboat"
                }
              }
            ]
          }
        ]
      }
    }
    ```
