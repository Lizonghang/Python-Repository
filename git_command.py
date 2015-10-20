$ git init  # 创建一个仓库
$ git add 文件名.后缀  # 将文件添加到仓库
$ git commit -m 修改信息  # 将文件提交到仓库
$ git status  # 查看仓库当前状态
$ git diff 文件名.后缀 # 对比修改的内容
$ git log  # 查看提交日志
$ git reset --h ard HEAD^  # 将当前版本回退到上一版本
						  # 当前版本HEAD,上一版本HEAD^^,上上版本HEAD^^,回退n个版本HEAD~n
$ git reset --hard 版本ID  # 返回到未来的某版本
$ git reflog  # 记录每一次命令(可查看commit id以找回版本)
$ git rm 文件名.后缀  # 将文件从工作区中删除
$ git checkout  # 用版本库里的版本替换工作区的版本,一键还原
$ cat 文件名.后缀  # 查看文件中的数据