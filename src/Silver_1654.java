import java.util.Scanner;

//Silver_1654.java
public class Silver_1654 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int k = scan.nextInt(); // 랜선 갯수
        int n = scan.nextInt(); // goal
        int[] cables = new int[k];
        int max = 0;
        for (int i = 0; i < k; i++) {
            cables[i] = scan.nextInt();
            if(cables[i]>max)
                max = cables[i];
        }
        scan.close();
        long ans = 0 ; // 정답 길이
        long low = 1; // MIN length of one cable
        long high = max;// MAX length of one cable
        long mid; //length of one cable
        while (low<=high) {
            mid = (low+high)/2;
            int count = 0;
            for (int i = 0; i <k; i++) {
                count += (cables[i]/mid);
            }
            if(count < n)
                high = mid - 1;
            else{//count >= n
                low = mid +1;
                if(ans < mid)
                    ans = mid;
            }
        }
        System.out.println(ans);
    }
}

