# MeUmy天下第一的ACM 模板

模板中难免可能存在错误，如果发现了错误欢迎提出

## 环境

Windows 11 操作系统， Powershell 生成

如果是在 Linux 操作系统，需要对 Makefile 脚本稍作修改 

## 生成 PDF

需求：`xelatex` 环境 + `python-pygments`：

```bash
pip install pygments # python包下载

make                 # 生成完整 PDF
make update          # 仅更新内容
```

## 清除文件

```bash
make clean           # 清理在 make 过程中产生的无关文件
```

## 修改内容

需要在对映 Latex 文件中修改，md 文件为了方便