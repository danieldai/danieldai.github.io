# Welcome to [DanielDai.com](http://www.danieldai.com)!

**[DanielDai.com](http://www.danieldai.com)** is powered by **[Pelican](http://getpelican.com/)**, a static site generaotr written in **[Python](http://python.org/)**. 

As the contents of GitHub Pages for user must be on `master` branch, I put the source code of this blog on another branch named `source`. Whenever I do any changes to the contents of the blog, I check out the `source` branch, edit the markdown files, regenerate the content and output the content to `master` branch with `ghp-import`


## How to edit this blog (just notes for author)

* setup virtualenv and checkout code

on machine with python 3 as default
```
mkvirtualenv danieldai
```

on machine with python 2 as default
```
mkvirtualenv -p /usr/bin/python3 danieldai
```

```
git clone git@github.com:danieldai/danieldai.github.io.git
cd danieldai.github.io.git
git checkout source
pip install -r requirements.txt
```

* edit exiting or add new blogs in `content` directory
* compile content in to HTML

```
fab build
```

* start dev server

```
fab serve
```

* visit http://localhost:8888 to review it
* publish to `master` branch

```
fab pages:'<commit message for master branch>'
```

* publish to GitHub Pages

```
fab push
```

* push source branch

```
git add .
git commit -m "<commit message for source branch"
git push
```

## `master` and `source` are two parallel branchs

Unlike normal git repositories, `master` branch and `source` branches are 2 parallel branches that only share a common parent, but will never merge together in future.

```
o----o----o----o----o----o master branch
 \
  \---o--o--o--o--o--o--o--o--o--o--o--o--o--o--o source branch    
```    

each commit on `master` branch is the compiled result of on commit on `source` branch
   





