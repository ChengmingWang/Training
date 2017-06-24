#encoding=utf-8

# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 实例变量：定义在方法中的变量，只作用于当前实例的类。
# 继承：即一个派生类（derived class ）继承基类（base class ）的字段和方法。
# 继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 方法：类中定义的函数。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

# 使用class语句来创建一个新类,class之后为类的名称并以冒号结尾
# 类的帮助信息可以通过ClassName.__doc__查看。
class Employee:
    '所有员工的基类'#类文档字符串
    empCount = 0#empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
    def __init__(self,name,salary):#__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()#<__main__.Test instance at xxxx>
t.prt()#__main__.Test

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

# 可以使用点(.)来访问对象的属性。也可以使用以下函数的方式来访问属性：
# getattr(obj, name[, default]) : 访问对象的属性。
# hasattr(obj,name) : 检查是否存在一个属性。
# setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
# delattr(obj, name) : 删除属性。

# Python内置类属性
#     __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#     __doc__ :类的文档字符串
#     __name__: 类名
#     __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#     __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print Employee.__dict__
print Employee.__doc__#所有员工的基类
print Employee.__name__#Employee
print Employee.__module__ #__main__
print Employee.__bases__#()

# Python对象销毁(垃圾回收)
# Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
# 在 Python 内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说，
# 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
a = 40      # 创建对象  <40> 1
b = a       # 增加引用， <40> 的计数 2
c = [b]     # 增加引用.  <40> 的计数 3
del a       # 减少引用 <40> 的计数 2
b = 100     # 减少引用 <40> 的计数 1
c[0] = -1   # 减少引用 <40> 的计数 0
# 垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
# 循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的。Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
# 作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。
# 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"
pt1 = Point()#count1
pt2 = pt1 #count2
pt3 = pt1 #count3
print id(pt1), id(pt2), id(pt3)  # 打印对象的id
del pt1 #count2
del pt2#count1
del pt3#count0

# 类的继承
# 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
# 需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写在括号里，基本类是在类定义的时候，在元组之中指明的。
# 在python中继承中的一些特点：
#     1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
#     2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
#     3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

class Parent:  # 定义父类
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"
    def parentMethod(self):
        print '调用父类方法'
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print "父类属性 :", Parent.parentAttr
class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"
    def childMethod(self):
        print '调用子类方法 child method'
c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法
c.getAttr()  # 再次调用父类的方法

#方法和运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # def __del__(self):#析构方法, 删除一个对象
    #     print 'deleted'
    def __str__(self):#用于将值转化为适于人阅读的形式
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __repr__(self):#转化为供解释器读取的形式
        return "repr,"
    def __cmp__(self, other):#对象比较
        return cmp(self.a,other.b)
    def __add__(self, other):#运算符重载
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print repr(v1)+repr(v2)

# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量
    _foo=1#protected var
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount  # 报错，实例不能访问私有变量

# 单下划线、双下划线、头尾双下划线说明：
#     __foo__: 定义的是特列方法，类似 __init__() 之类的。
#     _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#     __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。