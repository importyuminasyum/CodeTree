import java.util.Scanner;

public class Main {
    public static final int MAX_N = 100;

    public static int[] grid = new int[MAX_N + 1];
    public static int n;

    public static void paintRange(int start, int end) {
        for(int i = start; i <= end; i++) {
            grid[i]++;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();

            paintRange(start, end);
        }
        // Please write your code here.
        int ans = 0;

        for (int i = 1; i <= 100; i++) {
            ans = Math.max(ans, grid[i]);
        }
        
        System.out.println(ans);
    }
}