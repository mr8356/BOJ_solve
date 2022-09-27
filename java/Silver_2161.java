import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Silver_2161 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        Queue<Integer> cards = new LinkedList<Integer>();
        Queue<Integer> discard = new LinkedList<Integer>();
        for (int i = 1; i <= n; i++) {
            cards.add(i);
        }
        int tempCard;
        while (cards.size() > 1) {
            tempCard = cards.poll();
            discard.add(tempCard);
            if (cards.size()==1) {
                break;
            }
            tempCard = cards.poll();
            cards.add(tempCard);
        }
        for (Integer i : discard) {
            System.out.print(i+" ");
        }
        System.out.print(cards.poll());
    }
}
