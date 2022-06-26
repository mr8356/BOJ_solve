import java.util.Scanner;
//Silver_2477.java
public class Sliver_2839 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int five = n/5;
        int left = n%5;
        switch (left) {
            case 1:
                if(five>=1)
                    System.out.println(five+1);
                else
                    System.out.println(-1);
                break;
            case 2:
                if(five>=2)
                    System.out.println(five+2);
                else
                    System.out.println(-1);
                break;
            case 3:
                    System.out.println(five+1);
                break;
            case 4:
                if(five>=1)
                    System.out.println(five+2);
                else
                    System.out.println(-1);
                break;
            default:
                System.out.println(five);
                break;
        }
    }
}
