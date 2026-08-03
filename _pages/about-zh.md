---
permalink: /zh/
title: "Academic Pages：开箱即用的学术个人网站模板"
author_profile: true
lang: zh-CN
alternate_lang: en
alternate_url: /
---

这是一个由 [Academic Pages 模板](https://github.com/academicpages/academicpages.github.io)构建、托管在 GitHub Pages 上的网站主页。[GitHub Pages](https://pages.github.com) 是一项免费服务，它会根据 GitHub 仓库中的代码和数据自动构建并托管网站；每次向仓库提交更新，网站也会随之更新。这个模板最初基于 Michael Rose 创建的 [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/)，之后又针对学术工作者的需求进行了扩展，支持展示论文、报告、教学、作品集、博客，以及动态生成的个人简历。同样的功能也很适合任何希望展示专业经历的人。

你现在就可以 fork [这个模板](https://github.com/academicpages/academicpages.github.io)，修改配置和 Markdown 文件，添加自己的 PDF 等资料，免费建立一个没有广告的个人网站。

# 数据驱动的个人网站

与许多基于 Jekyll 的 GitHub Pages 模板一样，Academic Pages 将网站内容与页面样式分离。网站内容和元数据保存在结构化的 Markdown 文件中，主题文件则负责把这些内容转换为 HTML 页面。Markdown（`.md`）、YAML（`.yml`）、HTML 和 CSS 文件都保存在公开的 GitHub 仓库中。每次提交并推送更新后，[GitHub Pages](https://pages.github.com/) 都会自动构建静态页面，并免费托管到 GitHub 的服务器上。

这种方式只需传统动态内容管理系统（如 WordPress）很少一部分的计算资源，也更不容易受到入侵和 DDoS 攻击。你可以自由修改网站主题，而不必改动论文、报告等内容。即使不小心改坏了 Jekyll、HTML 或 CSS，保存内容的 Markdown 文件仍然安全，可以回退修改，甚至重新创建仓库——当然，请记得备份这些文件。你也可以编写脚本处理网站中的结构化数据，例如使用[这个脚本](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb)分析报告信息，并在地图上展示[所有报告地点](https://academicpages.github.io/talkmap.html)。

对于有进阶需求的用户，模板还支持以下常用工具：

- [MathJax](https://www.mathjax.org/)：显示数学公式
- [Mermaid](https://mermaid.js.org/)：绘制图表
- [Plotly](https://plotly.com/javascript/)：绘制交互式图形

# 开始使用

1. 如果还没有 GitHub 账号，请先注册并验证电子邮箱（必须完成验证）。
2. 打开[模板仓库](https://github.com/academicpages/academicpages.github.io)，点击右上角的 “Use this template” 按钮创建自己的仓库。
3. 进入仓库设置，将仓库重命名为“你的 GitHub 用户名.github.io”。这个名称同时也是网站地址。
4. 设置全站配置，并创建自己的内容和元数据。你也可以参考[这组修改记录](https://archive.is/3TPas)，了解示例网站从模板开始修改了哪些文件。
5. 将 PDF、ZIP 等资料上传到 `files/` 目录。比如 `files/example.pdf` 将可以通过 `https://你的用户名.github.io/files/example.pdf` 访问。
6. 在仓库设置的 GitHub Pages 部分查看部署状态。

## 全站配置

网站根目录中的 [`_config.yml`](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml) 是主要配置文件，用于设置侧边栏和其他全站功能。请将其中的默认内容替换为你自己的信息和 GitHub 仓库地址。顶部菜单保存在 [`_data/navigation.yml`](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml) 中。例如，如果不需要作品集或博客，可以删除对应菜单项；这不会影响其他页面。

## 创建内容和元数据

网站中的每一类内容都有对应的 Markdown 文件，分别保存在 `_publications`、`_talks`、`_posts`、`_teaching` 和 `_pages` 等目录中。例如，每场报告对应 `_talks` 目录中的一个 Markdown 文件。文件顶部的 YAML 区域保存结构化信息，主题会用这些数据生成不同页面。

同一份报告数据既可以生成[报告列表](https://academicpages.github.io/talks)，也可以生成[单场报告详情页](https://academicpages.github.io/talks/2012-03-01-talk-1)、个人简历中的报告部分，以及[报告地点地图](https://academicpages.github.io/talkmap.html)。地图需要运行仓库中的 [Python 脚本](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py)或 Jupyter Notebook，根据 `_talks` 目录的内容生成 HTML。

**Markdown 生成工具**

仓库提供了[一组 Jupyter Notebook](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator)，可以把包含报告或论文结构化信息的 CSV 文件转换为符合模板要求的 Markdown 文件。常见的工作方式是用电子表格维护论文和报告清单，然后运行这些 Notebook 批量生成网站内容。

# 如何编辑 GitHub 仓库

很多人使用 Git 客户端在本地编辑文件，再将修改推送到 GitHub。如果你还不熟悉 Git，也可以直接在 github.com 上编辑。打开某个文件（例如[这篇报告](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md)），点击内容预览右上角的铅笔图标即可修改；点击旁边的垃圾桶图标可以删除文件。在目录页面中还可以使用 “Create new file” 或 “Upload files” 新建、上传内容。

![编辑报告文件](/images/editing-talk.png)

# 更多信息

如需进一步了解 Academic Pages，请参阅[使用指南](https://academicpages.github.io/markdown/)、不断更新的 [Wiki](https://github.com/academicpages/academicpages.github.io/wiki)，或在 GitHub [讨论区](https://github.com/academicpages/academicpages.github.io/discussions)提问。[Minimal Mistakes 主题文档](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)也可能有所帮助。
