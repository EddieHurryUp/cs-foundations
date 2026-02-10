import java.util.Arrays;

public class ArrayBasicsDemo {
    public static void main(String[] args) {
        // TODO: 创建并初始化一维数组与二维数组
        int[] oneD = {1, 2, 3, 5};
        int[][] twoD = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        // TODO: 使用索引赋值与遍历（for-each 与 for）
        for (int i = 0; i < oneD.length; i++) {
            System.out.println("oneD[" + i + "] = " + oneD[i]);
        }
        for (int[] row : twoD) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }

        // TODO: 演示数组越界异常
        try {
            System.out.println(oneD[10]); // 访问不存在的索引
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught an ArrayIndexOutOfBoundsException: " + e.getMessage());
        }

        // TODO: 使用 Arrays 工具类进行排序与比较
        int[] arr1 = {3, 1, 4, 1, 5};
        int[] arr2 = {3, 1, 4, 1, 5};
        Arrays.sort(arr1, 0, 3);
        System.out.println("Sorted arr1: " + Arrays.toString(arr1));
        System.out.println("arr1 equals arr2: " + Arrays.equals(arr1, arr2));
        // TODO: 演示数组与泛型集合的差异（类型固定、长度固定）
        // 数组：元素类型固定、长度固定
        // 泛型集合：元素类型固定（由泛型参数决定）、长度可变
        int[] fixedArray = new int[2];
        fixedArray[0] = 1;
        fixedArray[1] = 2;
        System.out.println("array length = " + fixedArray.length);

        java.util.List<Integer> list = new java.util.ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3); // 长度可变
        System.out.println("list size = " + list.size());
    }
}
