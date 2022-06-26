import java.util.Scanner;

public class Silver_1436 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(); // nth count
        scan.close();
        int cnt = 0; //count
        int asw = 660; // answer
        while(n > cnt){
            asw++;
            int temp = asw;
            while (temp>=666) {
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
