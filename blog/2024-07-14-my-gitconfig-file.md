---
title: "我的Git配置文件"
tags: [git]
authors: [danieldai]
---

我的Git配置文件，里面定义了一些常用的alias，方便使用。

<!-- truncate -->

```ini
[user]
        name = Daniel Dai
        email = daniel@danieldai.com
[alias]
        s = status
        br = branch
        co = checkout
        cm = commit
        oldest-ancestor = !bash -c 'diff --old-line-format= --new-line-format= <(git rev-list --first-parent \"${1:-master}\") <(git rev-list --first-parent \"${2:-HEAD}\") | head -1' -
        ssv = "log --no-merges --pretty=format:\"\\\"%h\\\";%an;%ai;%ct;\\\"%s\\\"\""
        lg1 = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
        lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
        lg3 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD / %cD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
        lg1a = !"git lg1 --all"
        lg2a = !"git lg2 --all"
        lg3a = !"git lg3 --all"
        lg = !"git lg1"
        fap = fetch --all --prune
        fpush = push --force-with-lease
[core]
        editor = vim
	excludesfile = ~/.gitignore
	autocrlf = input
[push]
        default = simple
```

## 配置说明

### 用户信息
- **name**: 设置Git用户名
- **email**: 设置Git邮箱地址

### 常用别名 (Aliases)
- **s**: `git status` 的简写
- **br**: `git branch` 的简写  
- **co**: `git checkout` 的简写
- **cm**: `git commit` 的简写

### 高级别名
- **oldest-ancestor**: 查找两个分支的最近公共祖先
- **ssv**: 生成CSV格式的提交日志
- **lg1/lg2/lg3**: 不同风格的图形化日志显示
- **lg1a/lg2a/lg3a**: 显示所有分支的图形化日志
- **lg**: 默认使用lg1风格
- **fap**: 获取所有远程分支并清理已删除的分支
- **fpush**: 安全的强制推送

### 核心设置
- **editor**: 使用vim作为默认编辑器
- **excludesfile**: 全局忽略文件路径
- **autocrlf**: 处理换行符转换
- **push.default**: 推送模式设置为simple

这些配置大大提高了Git使用的效率，特别是图形化的日志显示和简化的命令别名。
