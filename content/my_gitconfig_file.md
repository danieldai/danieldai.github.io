Title: 我的Git配置文件
Date: 2024-07-14 22:20
Slug: my_gitconfig_file


我的Git配置文件，里面定义了一些常用的alias，方便使用。

```
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
        default = simpl
```