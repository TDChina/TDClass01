## 基本信息

- **时长** 1:47:37
- [**课程链接**](https://ke.qq.com/webcourse/index.html#course_id=252658&term_id=100297899&taid=1549667150322418&vid=n1423s3gmql)（仅报名用户可见）


## 课程大纲

- 需求分析
- 软件开发流程
- 软件架构设计
- 熟悉DCC软件二次开发模块
- 软件构建技巧
- Gui开发基础
- 软件打包


## 课程案例

- 在Maya中批量移动贴图文件


## 课程作业

- 在Maya中批量移动贴图文件
- 在Nuke中批量移动read节点原素材位置

#### 作业涉及的技术

- 如何在Maya/Nuke中列举出所有的“贴图”/“Read”节点？
    - `pm.ls(type="file")`
    - `nuke.selectedNodes("Read")`
- 如何获取节点属性信息？
    - `maya_node.Attribute.get()`
    - `nuke_node["file"].getValue()`
- 如何移动文件并修改文件名称？
    - `shitil.move(src, dst)`
- 如何修改节点属性？
    - `maya_node.Attribute.set(value)`
    - `nuke_node["file"].setValue(value)`


## 相关资料

- [课程思维导图](https://processon.com/mindmap/5a38dadee4b07c8d893bb5b3)
- [软件开发流程图](https://processon.com/diagraming/5a3b915ee4b0daa64fde2741)
- [编程能力的构成思维导图](https://processon.com/mindmap/5a3b8a28e4b0daa64fde11f8)
- [对软件架构设计的一些总结和理解](http://blog.csdn.net/cooldragon/article/details/48241965)