import java.util.Scanner;

public class Silver_1436 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        int cnt = 0;
        int asw = 660;
        while(n > cnt){
            asw++;
            int temp = asw;
            while (temp>600) {
                if(temp%1000 == 666){
                    cnt++;
                    break;
                }
                else{
                    temp/=10;
                }
            }
        }
        System.out.println(asw);
    }
}
