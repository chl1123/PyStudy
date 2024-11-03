"""
里氏替换原则
定义：所有引用基类的地方必须能透明地使用其子类的对象
"""

"""
design mode before: 
只读文件的保存没有意义，因此在ReadOnlyDocument类中重写了save方法，抛出异常
问题：
1. 客户端调用ReadOnlyDocument类的save方法时，会抛出异常
      基类方法没有这个限制，因此客户端没有在保存前检查文档类型，客户端程序会在运行时出现错误
2. 违反开闭原则
      客户端代码依赖具体的Document类，如果引入新的Document子类，客户端代码需要修改才能适应新的子类
"""


class Document0(object):
    def __init__(self, data, filename):
        self._data = data
        self._filename = filename

    def open(self):
        print("open file: %s" % self._filename)

    def save(self):
        print("save file: %s" % self._filename)


class ReadOnlyDocument0(Document0):
    def save(self):
        raise Exception("Read-only document")


class Project0:
    def __init__(self):
        self.__documents = []

    def add_document(self, document):
        self.__documents.append(document)

    def open_all(self):
        for document in self.__documents:
            document.open()

    def save_all(self):
        for document in self.__documents:
            document.save()


"""
after design mode:
把只读文档类作为层次结构中的基类
"""


class Document(object):
    def __init__(self, data, filename):
        self._data = data
        self._filename = filename

    def open(self):
        print("open file: %s" % self._filename)


class WritableDocument(Document):
    def save(self):
        print("save file: %s" % self._filename)


class Project(object):
    def __init__(self):
        self.__all_docs = []
        self.__writable_docs = []

    def add_document(self, document):
        self.__all_docs.append(document)
        if isinstance(document, WritableDocument):
            self.__writable_docs.append(document)

    def open_all(self):
        for document in self.__all_docs:
            document.open()

    def save_all(self):
        for document in self.__writable_docs:
            document.save()


if __name__ == '__main__':
    # design mode before:
    # doc = ReadOnlyDocument0("hello world", "hello.txt")
    # doc.save()
    # project = Project0()
    #
    # project.add_document(doc)
    # project.open_all()
    # project.save_all()

    # design mode after:
    doc = WritableDocument("hello world", "hello.txt")
    doc.save()
    project = Project()
    project.add_document(doc)
    project.open_all()
    project.save_all()
