import pprint
python = {
    "1基础知识":{
        "标准库":{
            "标准库的组成":"函数+模块=标准库",
            "标准库与函数模块的关系":"函数在模块里，模块在标准库里",
            "标准库与模块的导入":"from xxx（标准库模块名字） import xxx（子模块名字）"
           },
        "python解释器":{
            "1":"解释器只有找到与开始中括号（[）匹配的结束中括号（]）才会认为语句结束",
            "2":"一般地，Python中一行结束就标志一条语句的结束",
            "3":"python中默认所有输入均为str字符串",
            "4":"由于数据类型间要用逗号（，）分开，所以在一个字符串内使用其他数据类型的时候要强制转换"
           },
        "Python变量动态赋值":{
            "变量的使用":"Python中第一次使用变量时，变量就立即存在，不需要预先声明。",
            "python操作符":"python提供了'<','>','<=','>=','==表示相等','!=表示不等于','=赋值操作符'"
           },
        "代码块的运行":{
            "in操作符作用":"in操作符会检查一个对象是否在另一个对象里",
            "in操作符返回":"in操作符会返回True/False",
            "python的缩进":{
                 "1":"python不用大括号（[]）区分代码块，因为大括号更多用来分隔数据",
                 "2":"python 使用缩进（Tab）划分代码组",
                 "3":"python会用冒号（:）来引入与某个python控制语句（如if, else,for等）关联的代码组",
                 "4":"冒号(:)会引入一个必须向右缩进的新的代码组，若无缩进，解释器会报错"
                },
            "if与else、elif语句":{
                 "else语句":"指示当对应的if语句返回一个False值时要执行的代码",
                 "elif":"python把else if拼成elif"
                }
           },
        "代码块可含嵌套代码组":"任意代码组都可包含任意嵌套代码组，但必须缩进",
        "for循环":{
            "1":"迭代处理对象序列",
            "2":"结合range函数指定for循环次数"
        },
        "让执行暂停指定秒数":"利用time模块中的sleep函数，time.sleep(5)暂停5秒",
        "生成随机数":{
            "1引入模块":"import random",
            "2生成随机数":"random.randint(1,60)在1-60间生成随机数"
        },
        "开始、结束和步进":{
            "start":"start值允许你控制的范围从哪里开始",
            "stop":"stop规定范围何时结束",
            "step":"如何生成范围（正值+递增，负值-递减）"
        }
        
     },
    "2列表数据":{
        "对象":{
            "对象含义":"python中一切都是对象，包括数字、字符串、函数、模块,所有对象都可以赋给变量",
            "对象特点":"对象可以有状态（属性或值）和行为（方法）"
        },
        "python内置数据结构":{
            "内置":"在代码中直接使用，使用前无需先导入",
            "4种数据结构":{
                "列表":{
                    "含义":"类似于其他编程语言数组的概念，是一个有序的可变对象集合",
                    "特点":{
                       "1":"列表是动态的，可根据需要随时扩展或收缩",
                       "2":"不必预先声明列表的大小",
                       "3":"不必预先声明所要存储对象的类型，可在一列表中混合不同类型对象",
                       "4":"列表是可变的，可在任何时间增加、删除、修改对象来修改列表",
                       "5":"与数组一样，从0开始索引"
                    },
                    "列表的使用":{
                        "列表结构":"总是用中括号[]保围，列表中的对象之间总是用（，）分隔",
                        "管理列表":{
                            "列表创建":"price =[]直接输入值建立列表，等号左边为列表名",
                            "列表的删除":{
                                 "remove方法":"删除指定数值xxx.remove(指定值)",
                                 "pop方法":{
                                    "有输入索引值":"删除并返回索引值所对应的一个对象",
                                     "无输入索引值":"无指定索引值，则删除并返回最后一个对象",
                                     "注意":"可把pop返回的对象赋给一个变量，使变量保留下来，否则会被回收",
                                     "代码":"xxx.pop(索引值)"
                                     },
                            "popleft":"xxx.popleft()删除第一个",
                            "del方法":"del指定[x]的某个位置进行删除 del xxx[索引值]"
                                 },
                            "extend":{
                                      "方法":"将两个列表合并到一个列表xxx.extend([])括号内会提供一个对象列表添加到现有列表末尾",
                                      "extend与append":"调用.extend([])不会像现有列表增加任何元素，而调用.append([])会在末尾增加一个空列表[]"
                                     },
                            "insert方法":"将一个对象插入一个现有列表中指定索引值前面 xxx.(插入对象的索引在这个位置之前，要插入的值)",
                            ".copy()":"复制一个数据结构third =second.copy()",
                            ".clear()":"xxx.clear()清空列表",
                            ".count()":"xxx.count()输入对象统计对象在某个元素在列表出现的次数",
                            ".index()":"xxx.idnex()输入对象查对象索引位置",
                            "字符串——>列表":"list('字符串')",
                            "列表->字符串":"''.join([列表])",
                            "更换列表":"xxx[列表索引值]='更换的内容'"
                        },
                        "列表索引":{
                            "含义":"允许从列表两端来访问列表",
                            "要点":{
                                "1":"正索引从左到右数；负索引从右向左数(负索引从-1开始)",
                                "2":"python对中括号的扩展不支持负索引值"
                            },
                            "列表的开始，结束与步长":"在[]里指定，相互间用‘：’分隔，遵循有头无尾原则，指定结束值取不到"
                        },
                        "python运行":"先运行括号内，在运行括号外"
                    }
                },
                "元组":{
                    "含义":"有序的不可变的对象集合",
                    "特点":{
                        "1":"一旦赋值完，任何情况下元组都不能改变",
                        "2":"元组也使用索引值（从0开始索引）",
                        "3":"一旦对元组输入修改代码，解释器会报错"
                    },
                    "元组的结构":"使用小括号（）",
                    "元组的2个方法":{
                        "x.count(值)":"输出该对象出现的次数",
                        "a.index(值)":"对象在元组a的索引值"
                    },
                    "注意只有一个对象的元组":"每个元组在小括号之间至少包含一个逗号（，），即使只有一个对象,否则被当做字符串"
                }, 
                "字典":{
                    "含义":"允许你存储一个键/值对",
                    "要点":{
                      "1":"字典中每一个唯一键有一个与之关联的值",
                      "2":"字典中可包含多个键值对，可根据需要扩展/收缩可有多个数据行，但只有两列",
                      "3":"与键关联的值可以是任意对象",
                      "4":"字典是无序且多变的",
                      "5":"使用时不能依赖解释器所用的内部顺序，因为字典不会保持这个顺序"  
                    },
                    "字典的使用":{
                        "字典的结构":"用{}保围，每个键和值分别用引号''保围,键和值不一定是字符串，键与值之间用冒号：分隔，键值对之间用，逗号分开",
                        "管理字典":{
                            "xxx ={ }":"大括号表示初始为空的字典，字典的键必须初始化，否则产生错误！",
                            "字典的增、修":"xxx['键']='值'",
                            "字典的删除":{
                              "1":"xxx.pop('键')",
                              "2":"del xxx['键']",
                              "随机删除":"xxx.popitem()"  
                            },
                            "字典的获取":{
                                "xxx.get('键')":"该键不存在不会报错",
                                "xxx['键']":"该键不存在会报错"
                            },
                            "'键' in xxx":"查看该键是否存在于xxx中，存在返回True,不存在返回False",
                            "xxx.fromkeys(x,0)":"把所有值设为同一个值",
                            "xxx.keys()":"查所有键",
                            "xxx.value()":"查所有值"
                        },
                        "字典的函数":{
                           ".setdefault('键',x)":"若该键不存在将给该键初始化一个x值" 
                        }
                    }
                },
                "集合":{
                    "含义":"无序的唯一对象集合",
                    "要点":{
                        "1":"其中的任何对象不会重复",
                        "2":"可根据需要扩展或收缩",
                        "3":"无序的"
                    },
                    "集合的使用":{
                        "集合的结构":"对象之间用逗号','隔开，包围在{}里",
                        "集合的顺序":"使用集合时，解释器不会维持插入顺序，与所有数据结构一样，可以使用sorted函数对输出进行排序",
                        "管理集合":{
                            "创建集合":{
                                "直接创建":"xxx={}",
                                "利用set()函数":"xxx =set('aeiou')",
                                },
                            "集合的并集":{
                                ".union()":"将一个集合与另一个集合合并，再把合并结果赋给新的变量",
                                "代码":"u = xxx.union({集合})原有xxx集合不会改变"
                                },
                            "集合的子父集":{
                                "子集":"xxx.issubset(yyy),xxx是yyy子集返回True,否则返回False",
                                "父集":"xxx.issuperset(yyy) xxx是yyy父集返回True,否则返回False"
                                },
                            "集合的差集":{
                              ".difference()函数":"d =zzz.difference({集合yyy})difference函数将两个集合对象比较，返回前面的集合（即集合zzz）",
                              "直接作差":"d = 集合zzz-集合yyy"  
                               },
                            "集合的交集":{
                                ".intersection()":" i = zzz.intersection(yyy)比较zzz与yyy两个集合，找出共同对象并赋值",
                                "利用&符号":"zzz & yyy"
                               },
                            ".pop()函数":"随机移除一个元素",
                            ".clear()函数":"清空",
                            ".add()":"加",
                            ".copy()":"复制",
                            "集合的移除":{
                                ".discard()":"删除不存在的元素时不报错",
                                ".remove()":"删除不存在元素时会报错"
                            }
                        }
                    }
                }
            }
        }
        
     },
    "3结构化数据":{
        "while循环":"while True:则开始循环，while False：输出空白",
        "使字典美观":{
            "1":"import pprint调用pprint模块",
            "2":"pprint.pprint(字典名)调用函数 "
        },
       "其他重要函数":{
           ".title()":"首字母转化为大写",
           "len()":"查看所有长度",
           "type()":"查看数据类型"
       },
        "访问复杂数据":"从第一层开始索引 变量['字典的键']['某个键的键名']",
        "定义空的数据结构":{
            "空列表":"list()函数——>[]",
            "空字典":"dict()函数——>{}",
            "空集合":"set()函数-->set()",
            "空元组":"tuple()函数-->()"
        }
    },
    "4代码重用":{
        "引入函数":{
            "def":"指定函数名并列出参数",
            "return":"向调用这个函数的代码传回一个值"
        },
        "类型信息":"python解释器不要求指定函数参数或返回值类型，允许一切对象",
        "def创建函数":"def后面是函数名，一个有无参数的参数表，一个冒号",
        "字符串的作用":{
            '1':'python中字符串可用单引号（\’不可跨多行，并且同一行用同一个引号字符结束），双引号（“”不可跨多行，并且同一行用同一个引号字符结束），三重引号（\"""""""）包围',
            '2':'三重引号（""" """）可跨多行作为函数解释文档'
        },
        "return":{
            "return返回一个值作用":{
                "1":"检查函数本身某部分代码的运行结果、内容",
                "2":"输出某个结果以开始下一段程序",
                "3":"可返回一个过程状态"
                
            },
            "return 返回多个值":"还是一个结果，返回一个元组",
            "要点":{
                "1":"不写return，默认返回none，return上面内容是一个过程",
                "2":"不必要在return传回调用代码对象两边加小括号"
            }
        },
        "使用注释改进文档":{
            "作用":"描述返回类型及所有参数的类型,使代码使用者无需读代码即可知道函数接受什么类型和返回什么类型",
            "注解特点":"可用可不用，因为python解释器不考虑来回传递的数据类型，但可提供有效信息",
            "参数注释":"以冒号为标记，例如:str、:int",
            "返回值标记":"以—>为标记，例如：->set、->tuple"
            
        },
        "函数的参数":{
            "形参与实参":{
                "形参":"形式参数，不是实际存在的，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参",
                "实参":"实参：实际参数，调用函数时传递给函数的参数，可以是常量、变量，表达式，函数，传给形参",
                "两者区别":"形参是虚拟的，不占用空间，形参变量只有在被调用时才分配内存单元，实参是一个变量，占用内存空间，数据传递单向，实参传给形参，不能倒过来。"
            },
            "位置参数":"位置实参的顺序很重要，请确认函数调用中实参的顺序与函数定义形参的顺序一致",
            "关键字参数（指定参数默认值）":{
                "关键字参数位置":{
                    "默认值位置":"默认值要放在形参的最后一个",
                    "调用函数时":{
                        "1":"关键字参数要放在位置参数后面，否则报错",
                        "2":"指定了关键字参数可以不按照形参的输入顺序",
                        "3":"针对同一形参中，位置参数与关键字参数只能选其一，不能一起使用"
                    }
                    
                }
            },
            "传递任意数量的实参":{
                "*形参":{
                    "含义":"可代表多个数量实参",
                    "调用时要点":"只能使用位置参数",
                    "输出":"输出一个元组，不传值时输出为空元组"
                    
                },
                "**形参":{
                    "输出":"一个字典,不传值时是一个空字典",
                    "调用":"一定要用关键字参数"
                }
            },
            "导入模块中特定（多个）函数":"from module import 函数名（用逗号分开函数名导入多个函数）",
            "使用as 给函数指定别名":"from module import 函数 as 函数指定名",
            "使用as给模块指定别名":"import moudle as 模块别名",
            "导入模块所有函数":"from moudle import *"
            
                
            
        },
        
        
    }
}

pprint.pprint(python)
