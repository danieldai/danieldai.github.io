---
title: "使用Playwright捕获和记录浏览器的所有HTTP流量，特别是多标签场景"
tags: [playwright, testing, web-development]
authors: [danieldai]
---

在现代Web开发和测试中，捕获和分析HTTP流量是一个重要的技能。Playwright提供了强大的网络拦截和监控功能，可以帮助我们轻松捕获浏览器的HTTP请求和响应。本文将详细介绍如何使用Playwright捕获HTTP流量，特别是在多标签场景下如何使用context来管理和捕获流量。

<!-- truncate -->

## Playwright网络拦截基础

Playwright的网络拦截功能允许我们：
- 捕获所有HTTP/HTTPS请求和响应
- 修改请求（如添加headers、修改body）
- 修改响应（如模拟API响应）
- 记录流量用于分析或测试

### 基本设置

首先，我们需要安装Playwright：

```bash
npm install playwright
```

## 捕获单个页面的HTTP流量

让我们从一个简单的例子开始，捕获单个页面的HTTP流量：

```javascript
const { chromium } = require('playwright');

(async () => {
  // 启动浏览器
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // 启用网络事件监听
  await page.route('**/*', async (route) => {
    // 捕获请求
    const request = route.request();
    console.log(`Request: ${request.method()} ${request.url()}`);
    console.log(`Headers: ${JSON.stringify(request.headers(), null, 2)}`);
    
    if (request.postData()) {
      console.log(`Body: ${request.postData()}`);
    }

    // 继续请求
    await route.continue();

    // 捕获响应
    const response = await route.response();
    if (response) {
      console.log(`Response: ${response.status()} ${response.url()}`);
      console.log(`Response Headers: ${JSON.stringify(response.headers(), null, 2)}`);
      
      // 只获取文本响应的内容（二进制文件可能很大）
      const contentType = response.headers()['content-type'];
      if (contentType && contentType.includes('text')) {
        const body = await response.text();
        console.log(`Response Body: ${body.substring(0, 100)}...`); // 只显示前100个字符
      }
    }
  });

  // 访问页面
  await page.goto('https://example.com');

  // 关闭浏览器
  await browser.close();
})();
```

## 使用Context管理多标签场景

在实际测试中，我们经常需要处理多个标签页。Playwright的`BrowserContext`是一个隔离的浏览会话，它可以包含多个页面（标签页）。使用Context的好处是：

1. 可以在单个Context中管理多个页面
2. 网络拦截设置可以应用到整个Context（所有页面）
3. 可以为不同的测试场景创建多个隔离的Context

### 创建Context并捕获多标签流量

下面的例子展示了如何使用Context来捕获多个标签页的HTTP流量：

```javascript
const { chromium } = require('playwright');

(async () => {
  // 启动浏览器
  const browser = await chromium.launch();
  
  // 创建一个新的Context
  const context = await browser.newContext();

  // 存储所有捕获的请求和响应
  const trafficLog = [];

  // 在Context级别启用网络事件监听（将应用到所有页面）
  await context.route('**/*', async (route) => {
    const request = route.request();
    
    // 创建请求日志条目
    const logEntry = {
      id: Date.now() + Math.random(),
      timestamp: new Date().toISOString(),
      method: request.method(),
      url: request.url(),
      headers: request.headers(),
      postData: request.postData(),
      page: request.frame().page().url() // 记录请求来自哪个页面
    };

    // 继续请求
    await route.continue();

    // 捕获响应
    const response = await route.response();
    if (response) {
      logEntry.response = {
        status: response.status(),
        headers: response.headers()
      };
      
      // 获取响应内容（仅文本类型）
      const contentType = response.headers()['content-type'];
      if (contentType && contentType.includes('text')) {
        try {
          logEntry.response.body = await response.text();
        } catch (e) {
          logEntry.response.body = '[Failed to read body]';
        }
      }
    }

    // 将日志条目添加到trafficLog
    trafficLog.push(logEntry);
  });

  // 在Context中创建第一个页面
  const page1 = await context.newPage();
  await page1.goto('https://example.com');
  
  // 在Context中创建第二个页面
  const page2 = await context.newPage();
  await page2.goto('https://google.com');
  
  // 在第一个页面中打开一个新标签（仍属于同一个Context）
  const [page3] = await Promise.all([
    context.waitForEvent('page'), // 等待新页面事件
    page1.click('a[target="_blank"]') // 点击一个打开新标签的链接
  ]);
  await page3.waitForLoadState();

  // 输出捕获的流量日志
  console.log('=== 捕获的HTTP流量日志 ===');
  trafficLog.forEach((entry, index) => {
    console.log(`\n${index + 1}. ${entry.method} ${entry.url}`);
    console.log(`   来自页面: ${entry.page}`);
    console.log(`   状态码: ${entry.response?.status || 'N/A'}`);
  });

  // 关闭浏览器
  await browser.close();
})();
```

## 高级功能：过滤和自定义日志

### 过滤特定的请求

我们可以使用glob模式来过滤特定的请求：

```javascript
// 只捕获API请求
await context.route('**/api/**', async (route) => {
  // 处理API请求
  await route.continue();
});

// 捕获所有图片请求
await context.route('**/*.{png,jpg,jpeg,gif,webp}', async (route) => {
  // 处理图片请求
  await route.continue();
});
```

### 自定义日志格式

我们可以将捕获的流量保存为JSON格式，方便后续分析：

```javascript
const fs = require('fs');

// ... 捕获流量的代码 ...

// 将流量日志保存到文件
fs.writeFileSync('traffic-log.json', JSON.stringify(trafficLog, null, 2), 'utf8');
console.log('流量日志已保存到 traffic-log.json');
```

## 多Context场景

在某些情况下，我们可能需要创建多个Context来隔离不同的测试场景：

```javascript
// 创建第一个Context（用于用户A）
const contextA = await browser.newContext();
await contextA.route('**/*', handleRequestForUserA);

// 创建第二个Context（用于用户B）
const contextB = await browser.newContext();
await contextB.route('**/*', handleRequestForUserB);

// 在不同的Context中创建页面
const pageA = await contextA.newPage();
const pageB = await contextB.newPage();
```

## 实际应用场景

### 测试API集成

捕获HTTP流量可以帮助我们验证应用程序是否正确调用了API，以及API返回的数据是否符合预期。

### 性能分析

通过记录请求的响应时间和大小，我们可以分析应用程序的性能瓶颈。

### 安全测试

捕获HTTP流量可以帮助我们检查是否有敏感信息通过网络传输，以及是否正确使用了HTTPS。

### 调试问题

当应用程序出现问题时，捕获HTTP流量可以帮助我们快速定位问题所在，例如API调用失败、数据格式错误等。

## 最佳实践

1. **使用Context管理多标签**：在多标签场景下，始终使用Context来管理和捕获流量，这样可以确保所有相关页面的流量都被正确捕获。

2. **过滤请求**：只捕获我们需要的请求，避免日志过大。

3. **合理存储日志**：根据需要选择合适的日志存储方式，例如JSON文件、数据库等。

4. **注意异步操作**：网络请求是异步的，确保正确处理异步操作以避免丢失日志。

5. **清理资源**：使用完毕后，记得关闭页面、Context和浏览器，释放资源。

## 总结

Playwright提供了强大的网络拦截和监控功能，可以帮助我们轻松捕获和分析浏览器的HTTP流量。通过使用Context，我们可以有效地管理多标签场景下的流量捕获。掌握这些技巧可以帮助我们更好地进行Web开发、测试和调试工作。

希望本文对你有所帮助！如果你有任何问题或建议，欢迎在下方留言。