public class PrimitiveTypesDemo {
    public static void main(String[] args) {
        // TODO: 声明 8 种基本类型变量，并初始化为有代表性的值
        // byte, short, int, long, float, double, char, boolean
        byte byteVar = 100;
        short shortVar = 10_000;
        int intVar = 100_000;
        long longVar = 10_000_000_000L;
        float floatVar = 3.14f;
        double doubleVar = 3.***;
        char charVar = 'A';
        boolean booleanVar = true;
        System.out.println("byte: " + byteVar);
        System.out.println("short: " + shortVar);
        System.out.println("int: " + intVar);
        System.out.println("long: " + longVar);
        System.out.println("float: " + floatVar);
        System.out.println("double: " + doubleVar);
        System.out.println("char: " + charVar);
        System.out.println("boolean: " + booleanVar);


        // TODO: 输出每个变量的值与类型（可使用 getClass 但基本类型需要先装箱）
        System.out.println("byte type: " + ((Object) byteVar).getClass().getSimpleName());
        System.out.println("short type: " + ((Object) shortVar).getClass().getSimpleName());
        System.out.println("int type: " + ((Object) intVar).getClass().getSimpleName());
        System.out.println("long type: " + ((Object) longVar).getClass().getSimpleName());
        System.out.println("float type: " + ((Object) floatVar).getClass().getSimpleName());
        System.out.println("double type: " + ((Object) doubleVar).getClass().getSimpleName());
        System.out.println("char type: " + ((Object) charVar).getClass().getSimpleName());
        System.out.println("boolean type: " + ((Object) booleanVar).getClass().getSimpleName());


        // TODO: 写出不同进制的整数字面量（如二进制、八进制、十六进制）
        int binary = 0b1010; // 二进制
        int octal = 012;     // 八进制
        int hex = 0xA;       // 十六进制
        System.out.println("binary: " + binary);
        System.out.println("octal: " + octal);
        System.out.println("hex: " + hex);

        System.out.println("=".repeat(30));
        // TODO: 写出 long/float/double 字面量的正确后缀，并尝试省略后缀对比报错
        long longLiteral = 10000000000L; // 正确的 long 字面量
        float floatLiteral = 3.14f;       // 正确的 float 字面
        double doubleLiteral = 3.***; // 正确的 double 字面量
        // long longError = ***; // 省略后缀
        // float floatError = 3.14; // 省略后缀
        System.out.println("long literal: " + longLiteral);
        System.out.println("float literal: " + floatLiteral);
        System.out.println("double literal: " + doubleLiteral);
        System.out.println("=".repeat(30));
        // TODO: 观察 char 与 int 的相互转换（打印字符与对应码点）
        char charA = 'A';
        int codePointA = (int) charA; // char 自动转换为 int
        char charFromCodePoint = (char) codePointA; // int 强制转换为 char
        System.out.println("char: " + charA);
        System.out.println("code point: " + codePointA);
        System.out.println("char from code point: " + charFromCodePoint);
    }
}
