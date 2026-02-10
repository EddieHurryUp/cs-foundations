public class TypeConversionDemo {
    public static void main(String[] args) {
        // TODO: 演示自动类型提升（int + long, int + double）
        int intValue = 10;
        long longValue = 20L;
        double doubleValue = 30.5;
        long result1 = intValue + longValue; // int 自动提升为 long
        double result2 = intValue + doubleValue; // int 自动提升为 double
        System.out.println("int + long = " + result1);
        System.out.println("int + double = " + result2);

        System.out.println("*".repeat(20));

        // TODO: 演示显式强制类型转换，并观察精度丢失
        double pi = 3.14159;
        int truncated = (int) pi; // 小数被截断
        System.out.println("double -> int: " + truncated);

        long bigLong = 3_000_000_000L;
        int narrowed = (int)bigLong; // 发生截断，数值溢出
        System.out.println("long -> int (overflow): " + narrowed);

        System.out.println("*".repeat(20));

        // TODO: 触发整数溢出（如 int 最大值 + 1），并解释结果
        int maxInt = Integer.MAX_VALUE;
        int overflow = maxInt + 1;
        System.out.println("Integer.MAX_VALUE: " + maxInt);
        System.out.println("Integer.MAX_VALUE + 1: " + overflow);

        System.out.println("*".repeat(20));
        // TODO: 对比 Math.addExact 的溢出行为
        try {
            Math.addExact(maxInt, 1);
        } catch (ArithmeticException e) {
            System.out.println("Math.addExact overflow: " + e.getMessage());
        }

        System.out.println("*".repeat(20));
        // TODO: 演示拆箱空指针（Integer 为空时自动拆箱）
        Integer nullInteger = null;
        try {
            int unboxed = nullInteger; // 触发 NullPointerException
        } catch (NullPointerException e) {
            System.out.println("NullPointerException during unboxing: " + e.getMessage());          
        }

        System.out.println("*".repeat(20));
    }
}
