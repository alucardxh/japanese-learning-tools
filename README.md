# japanese-learning-tools
+ 这是项目主要是用代码解决一些在日语学习中遇到的一些问题
## cabocha_parse.py 工具
### 功能介绍
+ 解决我在学习日语遇见的分词问题。比如下面这一句话，如果没有分词器我根本不知道应该从哪里断开是一个完整的文节，这样我就没法进行可以理解输入。这个工具主要就是解决这个问题的。 
  >   バービキュ食べ過ぎて　僕もう草は食べられません   
    バービキュ　食べ過ぎて　僕　もう　草は　食べられません
  + 这种分词器非常多，但是分词都过于细致，大部分都是以单词划分，这样不利于可理解输入，目前发现只有这一款同时支持文节和单词划分。
  + 更多NPL项目可以参考这个github开源项目 https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/README.md 涵盖基本所有的日语的NPL项目。
+ 其余功能主要是将影视剧中的字幕文件进行转换，这样在对影视剧进行精听训练时就是直接就是划分好的日文字幕。
+ 使用某款app也能解决该问题，但是当需要大量的可理解输入的时候，一句句查效率很低。

### 项目依赖
1. 主要依赖这个项目 https://github.com/kenkov/cabocha 使用cabocho这个分词工具
   1. 需要在window上或者mac上安装 cabocha。mac上直接使用 brew install cabocha指令即可
   2. 执行 git clone https://github.com/taku910/cabocha 进入安装目录执行pip install python/
   3. 执行 pip install git+https://github.com/kenkov/cabocha@0.1.4 
2. 该文件的主要对字幕提取部分的功能使用到了函数式编程api，所以需要安装函数式依赖包 pip install pyfunctional 