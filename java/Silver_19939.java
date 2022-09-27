import java.util.Scanner;

public class Silver_19939 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(); // number of balls
        int k = scan.nextInt(); // number of baskets
        scan.close();
        int[] baskets = new int[k];
        // if k baskets, add base to all baskets
        // after, need AT LEAST additional (1+2+3+....+k) balls
        int base = (n-((k*(k+1))/2));
        if (base<0) {
            System.out.println("-1");
            return;
        }
        for (int i = 0; i < baskets.length; i++) {
            baskets[i] = (base / k);
            n -= (base / k);
        }
        if (n==((k*(k+1))/2)) {
            System.out.println(k-1);
        }
        else{
            System.out.println(k);
        }
    }
}