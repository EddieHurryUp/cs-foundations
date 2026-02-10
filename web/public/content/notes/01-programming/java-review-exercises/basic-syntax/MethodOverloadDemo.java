public class MethodOverloadDemo {
    public static void main(String[] args) {
        // TODO: 调用不同的 add 重载方法，观察编译器选择规则
        System.out.println(add(1, 2));          // 应该调用 add(int, int)
        System.out.println(add(1L, 2L));        // 应该调用 add(long, long)
        System.out.println(add(1.0, 2.0));      // 应该调用 add(double, double)
        // TODO: 演示可变参数与数组重载的优先级
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println(add(arr));           // 应该调用 add(int... nums)

        // TODO: 观察装箱/拆箱在重载选择中的影响
        Integer a = 1, b = 2;
        System.out.println(add(a, b));          // 应该调用 add(int, int)
    }

    // TODO: 编写 add(int, int), add(long, long), add(double, double)
    private static int add(int a, int b) {
        System.out.println("调用了 add(int, int)");
        return a + b;
    }

    private static long add(long a, long b) {
        System.out.println("调用了 add(long, long)");
        return a + b;
    }

    private static double add(double a, double b) {
        System.out.println("调用了 add(double, double)");
        return a + b;
    }
    // TODO: 再编写 add(int... nums)
    private static int add(int... nums) {
        System.out.println("调用了 add(int... nums)");
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }
}
