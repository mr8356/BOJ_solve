import java.util.Scanner;

//Silver_2805.java
public class Silver_2805 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(); // numbers of trees
        int m = scan.nextInt(); // need m meters
        int[] trees = new int[n]; //height of trees
        int MAX = 0;
        for (int i = 0; i < n; i++) {
            trees[i] = scan.nextInt();
            if (trees[i]>MAX) {
                MAX = trees[i];
            }
        }
        scan.close();
        int low = 0;
        int high = MAX;
        int H = 0; //answer
        while (low<=high) {
            int mid = (low+high)/2;
            long count = 0; //gained trees
            for (int tree : trees) {
                if(tree>mid)
                    count+= (tree - mid);
            }
            if (m <= count) {
                low = mid + 1;
                if(mid >= H) //higher the better
                    H = mid;
            }
            else{// m > count 
                high = mid - 1;
            }
        }
        System.out.println(H);
    }
}

