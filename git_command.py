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
$ git push origin master  # 把本地master分支最新修改推送至GitHub
$ git pull origin master  # 取回远程主机的master分支
$ git push -u origin master -f  # 强制把本地master分支推送至GitHub
$ git clone git@github.com:lizonghang/python-repository.git  # 克隆得到一个本地库
$ ls # 查看Git库中的文件,需要先进入Git仓库目录