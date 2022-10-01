import java.util.HashMap;
import java.util.Scanner;

public class Silver_4358 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        HashMap<String , Double> trees = new HashMap<String , Double>();
        int count = 0;
        while (scan.hasNextLine()) {
            String tree = scan.nextLine();
            if (trees.containsKey(tree)) {
                trees.replace(tree, trees.get(tree)+1);
            } else {
                trees.put(tree,1.0);
            }
            count++;
        }
        final int totalTree = count;
        Object[] treeList = trees.keySet().stream().sorted().toArray();
        for (Object t : treeList) {
            System.out.printf("%s %.4f\n", t.toString(), (trees.get(t.toString())*100)/totalTree);
        }
        scan.close();
    }
}
