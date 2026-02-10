public class ControlFlowDemo {
    private static int x = 10; // 类成员变量

    public static void main(String[] args) {
        // TODO: 使用 if/else 判断成绩区间，并输出等级
        int score = 85;
        if (score >= 90) {
            System.out.println("优秀");
        } else if (score >= 60) {
            System.out.println("及格");
        } else {
            System.out.println("不及格");
        }

        // TODO: 使用 switch (字符串或枚举) 输出不同分支结果
        String day = "Monday";
        switch (day) {
            case "Monday":
                System.out.println("周一");
                break;
            case "Tuesday":
                System.out.println("周二");
                break;
            default:
                System.out.println("其他");
        }

        // TODO: 使用 for/while/do-while 完成同一任务，并比较差异
        // for 循环
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }
        // while 循环
        int j = 0;
        while (j < 5) {
            System.out.println(j);
            j++;
        }
        // do-while 循环
        int k = 0;
        do {
            System.out.println(k);
            k++;
        } while (k < 5);


        // TODO: 演示 break/continue 的作用范围
        for (int i = 0; i < 5; i++) {
            if (i == 2) {
                break; // 跳出循环
            }
            if (i == 1) {
                continue; // 跳过当前迭代
            }
            System.out.println(i);
        }

        // TODO: 演示变量作用域（同名变量遮蔽）
        int x = 20; // 局部变量，遮蔽同名的类成员变量
        {
            int y = 30; // 块级变量
            System.out.println("block y = " + y);
            System.out.println("local x = " + x);
        }
        System.out.println("local x = " + x);
        System.out.println("field x = " + ControlFlowDemo.x);
    }
}
