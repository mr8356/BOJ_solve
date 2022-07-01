import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Silver_11279 {
    public static void main(String[] args) throws NumberFormatException, IOException   {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());// 1~n
        int input;
        // 인자에 Comparator를 넣는데, 스스로 MyReverseIntComparator 라는 클래스를 만들어서 했습니다.
        MyReverseIntComparator maxComparator = new MyReverseIntComparator();
        PriorityQueue<Integer> maxQueue = new PriorityQueue<Integer>(maxComparator);
        ///////////////////////////////////////////////////////////////////////////////
        // 단순히 최대 큐면, 정렬을 정반대로 하면 되므로 아래 처럼 입력해서 클래스 생성없이 가능
        //PriorityQueue<Integer> maxQueue = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            input = Integer.parseInt(br.readLine());
            if (input>0) {
                maxQueue.add(input);
            } else {
                if (!maxQueue.isEmpty()) {
                    System.out.println(maxQueue.poll());
                }
                else{
                    System.out.println(0);
                }
            }
        }
        br.close();
    }

}

// 우선순위 비교 클래스 생성
class MyReverseIntComparator implements Comparator<Integer>{
    @Override
    public int compare(Integer o1, Integer o2) {
        if ((int) o1 > (int) o2) {
            return -1;
        }
        else if((int) o1 < (int) o2) {
            return 1;
        }
        else{
            return 0;
        }
    }
}