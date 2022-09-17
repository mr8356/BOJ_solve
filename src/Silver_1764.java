import java.util.HashSet;
import java.util.Scanner;

public class Silver_1764 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int N  = scan.nextInt(); // un hear
        int M = scan.nextInt(); // un see
        //un hear people set
        HashSet<String> peoples =  new HashSet<String>();
        for (int i = 0; i < N; i++) {
            peoples.add(scan.next());
        }
        // un see & hear
        HashSet<String> stragers  = new HashSet<String>();
        int numberOfStrangers = 0;
        for (int i = 0; i < M; i++) {
            String input = scan.next();
            if (peoples.contains(input)) {
                stragers.add(input);
                numberOfStrangers++;
            }
        }
        System.out.println(numberOfStrangers);
        // sorting sets and print
        stragers.stream().sorted().forEach(System.out::println);
    }
}
