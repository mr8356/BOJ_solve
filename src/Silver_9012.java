import java.util.Scanner;
import java.util.Stack;

public class Silver_9012 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.nextLine();
        String[] str = new String[n];
        for (int i = 0; i < n; i++) {
            str[i] = scan.nextLine();
        }
        scan.close();
        Stack pair = new Stack<Character>();
        for (int i = 0; i < n; i++) {
            pair.clear();
            char[] chars = str[i].toCharArray();
            for (int j = 0; j < chars.length; j++) {
                if(chars[j]=='('){
                    pair.add('(');
                }
                else if(chars[j]==')'){
                    if (pair.empty()) {
                        pair.add("E");
                        break;
                    }
                    else{
                        pair.pop();
                    }
                }
                
            }
            if (pair.empty()) {
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }

        }
    }
}
