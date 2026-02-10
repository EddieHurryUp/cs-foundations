---
title: Java 复习笔记框架
tags: [java, programming, review]
level: core
updated: 2026-02-10
---

# Java 复习笔记框架

用于系统回忆与补全 Java 核心知识点。

## 基础语法与类型系统

### 问答

- Java 的 8 种基本类型分别是什么？各自的位数与取值范围如何？
  - byte：8位，有符号，范围-128 ～ 127
  - short：16位，有符号，范围-32，768～32，767
  - int：32位，有符号，范围-***～***
  - long：64位，有符号，范围-9223372036854775808～9223372036854775
  - float：32位，IEEE754单精度，约7位十进制有效数字
  - double：64位，IEEE754单精度，约15-16位十进制有效数字
  - char：16位，无符号，范围0-65535（UTF-16 code unit）
  - boolean：只有true/false（大小未被JVM规范固定）
- `int`、`long`、`float`、`double` 的字面量写法有哪些注意点？
  - 整数字面量默认是int，需要L/l才是long，123是int，123L是long
  - 整数字面量可写2、8、16进制，0b1010、012、0xff
  - 浮点字面量默认是double，需要F/f才是float，3.14是double，3.14f是float
  - 浮点字面量必须有小数点或指数1.0\1e3
- 装箱与拆箱发生在什么场景？可能带来哪些性能或空指针风险？
  - 装箱：基本类型自动转换为包装类型（如 `int -> Integer`），常见在集合/泛型、作为 `Object` 传参、需要 `null` 表示时
  - 拆箱：包装类型自动转回基本类型（如 `Integer -> int`），常见在算术运算、比较、赋值给基本类型变量时
  - 性能风险：频繁装箱/拆箱会创建大量对象、增加 GC 压力，循环中尤其明显
  - 空指针风险：拆箱时如果包装类型为 `null` 会触发 `NullPointerException`，例如 `Integer a = null; int b = a;`
- `==` 与 `equals` 在基本类型与引用类型上的区别是什么？
  - 基本类型：`==` 比较数值是否相等，`equals` 不能用于基本类型
  - 引用类型：`==` 比较引用是否同一对象（地址）
  - `equals`：默认继承自 `Object` 时等价于 `==`；很多类（如 `String`、包装类）重写为“内容相等”
  ```java
  String s1 = new String("a");
  String s2 = new String("a");
  System.out.println(s1 == s2);      // false
  System.out`.println(s1.equals(s2)); // true
  ```
- 变量的作用域与生命周期如何区分？局部变量与成员变量的默认值有什么差异？
  - 作用域：变量可被访问的代码区域
  - 生命周期：变量从创建到失效的时间段
  - 局部变量：方法体/代码块内声明，仅在该块内可见；必须显式初始化
  - 成员变量：类内、方法外声明（包含实例变量与静态变量）；有默认值
  - 成员变量默认值：数值型为 0，`boolean` 为 false，引用类型为 null，`char` 为 `\u0000`


### 实操练习

- 基本类型与字面量：`notes/01-programming/java-review-exercises/basic-syntax/PrimitiveTypesDemo.java`
- 类型转换与溢出：`notes/01-programming/java-review-exercises/basic-syntax/TypeConversionDemo.java`
- 控制流与作用域：`notes/01-programming/java-review-exercises/basic-syntax/ControlFlowDemo.java`
- 方法重载与可变参数：`notes/01-programming/java-review-exercises/basic-syntax/MethodOverloadDemo.java`
- 数组与索引边界：`notes/01-programming/java-review-exercises/basic-syntax/ArrayBasicsDemo.java`

## 面向对象与设计原则

- 

## 常用语言特性

- 

## 字符串与常用类库

- 

## 集合框架

- 

## 泛型与类型擦除

- 

## 异常处理

- 

## 注解与反射

- 

## I/O 与 NIO

- 

## 并发与多线程

- 

## JVM 与内存模型

- 

## 性能优化与调优

- 

## 构建与工程化

- 

## 测试与质量保障

- 

## 安全与常见漏洞

- 

## 常见坑与排查

- 

## 面试高频问题

- 

## References

- 

## 今日总结（2026-02-10）

### 错误与订正

- 基本类型遗漏 `byte`、`short`，补全 8 种类型与位数/范围
- 字面量规则错误：整数默认 `int`，`long` 需 `L`；浮点默认 `double`，`float` 需 `F`
- 误以为 `equals` 只比较“数值”，实际上由具体类实现；`==` 对引用比较地址
- 误把成员变量当作局部变量的一种，纠正为“类成员变量 vs 局部变量”
- 误认为“泛型集合类型可变”，纠正为“元素类型固定，长度可变”

### 收获

- 清楚了装箱/拆箱的触发场景与 NPE 风险
- 理解数组初始化与长度规则：初始化器不与长度混写
- 理解 varargs 本质是数组，`...` 仅在参数定义处使用
- 通过代码演示掌握类型转换、溢出、控制流与作用域遮蔽
