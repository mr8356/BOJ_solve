import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
//Silver_11286.java
public class Silver_11286 {
    public static void main(String[] args) throws NumberFormatException, IOException   {
        // final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner scan = new Scanner(System.in);
        // int n = Integer.parseInt(br.readLine());// 1~n
        int n  = scan.nextInt();
        int input;
        // 인자에 Comparator를 넣는데, 스스로 MyAbsIntComparator 라는 클래스를 만들어서 했습니다.
        MyAbsIntComparator absComparator = new MyAbsIntComparator();
        PriorityQueue<Integer> absQueue = new PriorityQueue<Integer>(absComparator);
        for (int i = 0; i < n; i++) {
            // input = Integer.parseInt(br.readLine());
            input = scan.nextInt();
            if (input!=0) {
                absQueue.add(input);
            } else {
                if (!absQueue.isEmpty()) {
                    System.out.println(absQueue.poll());
                }
                else{
                    System.out.println(0);
                }
            }
        }
        scan.close();
    }

}

// 우선순위 비교 클래스 생성
class MyAbsIntComparator implements Comparator<Integer>{
    @Override
    public int compare(Integer o1, Integer o2) {
        int x1 = Math.abs(o1);
        int x2 = Math.abs(o2);
        if (x1 > x2) {
            return 1;
        }
        else if(x1 < x2) {
            return -1;
        }
        else{
            if(o1 == o2){
                return 0;
            }
            else{
                if(o1>o2)
                    return 1;
                else
                    return -1;
            }
        }
    }
}