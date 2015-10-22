$ git init  # 创建一个仓库
$ git add <file>  # 将文件添加到仓库
$ git commit -m 修改信息  # 将文件提交到仓库
$ git status  # 查看仓库当前状态
$ git diff <file> # 对比工作区修改的内容
$ git diff HEAD -- <file>  # 查看工作区和版本库里面最新版本的区别
$ git log  # 查看提交日志
$ git reset --hard HEAD^  # 将当前版本回退到上一版本,当前版本HEAD,上一版本HEAD^^,上上版本HEAD^^,回退n个版本HEAD~n
$ git reset --hard 版本ID  # 返回到未来的某版本
$ git reflog  # 记录每一次命令(可查看commit id以找回版本)
$ git rm <file>  # 将文件从工作区中删除
$ git checkout  # 用版本库里的版本替换工作区的版本,一键还原
$ cat <file>  # 查看文件中的数据
$ git checkout -- <file>  # 丢弃工作区的修改 
$ git reset HEAD <file>  # 将暂存区中的修改回退到工作区
$ git push origin <branch>  # 把本地指定分支最新修改推送至GitHub
$ git pull origin master  # 取回远程主机的master分支
$ git push -u origin master -f  # 强制把本地master分支推送至GitHub
$ git clone git@github.com:lizonghang/python-repository.git  # 克隆得到一个本地库
$ ls # 查看Git库中的文件,需要先进入Git仓库目录
$ git checkout -b <branch>  # 创建并切换分支
$ git checkout -b <branch> origin/<branch>  # 创建远程origin的<branch>分支到本地
$ git branch <branch>  # 创建一个分支
$ git branch  # 查看所有分支
$ git checkout <branch>  # 切换到分支
$ git merge <branch>  # 合并指定分支到当前分支
$ git merge --no-ff -m <message> <branch>  # 禁用Fast forward合并分支,且原分支保留
$ git branch -d <branch>  # 删除分支
$ git stash  # 储藏当前工作现场,等待恢复现场后继续工作
$ git stash list  # 查看储藏的工作现场列表
$ git stash apply stash@<index> # 恢复工作现场,不删除stash内容
$ git stash drop stash@<index>  # 删除stash内容
$ git stash pop  # 恢复工作现场,同时删除stash内容
$ git branch --set-upstream <branch> origin/<branch>  # 指定本地<branch>分支与远程<branch>分支的链接
$ git tag # 查看所有标签
$ git tag <tag-name>  # 添加一个新标签,默认打在最新提交的commit上
$ git tag <tag-name> <commit-id>  # 给指定的提交添加标签
$ git show <tag-name>  # 查看标签信息
$ git tag -a <tag-name> -m <message> <commit-id>  # 创建带有说明的标签
$ git tag -d <tag-name>  # 删除标签
$ git push origin <tag-name>  # 推送标签<tag-name>至远程
$ git push origin --tags  # 一次性推送全部尚未推送到远程的本地标签
$ git push origin :refs/tags/<tag-name>  # 删除远程tag标签,需要先删除本地标签