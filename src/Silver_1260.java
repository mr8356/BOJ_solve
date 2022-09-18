import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Silver_1260{
    // Inner Class needs static
    static class Graph {
        class Node{
            int data;
            LinkedList<Node> adjacent;
            boolean marked;
            Node(int data){
                this.data = data;
                this.adjacent = new LinkedList<Node>();
                this.marked = false;
            }// constructor
        }//Node

        Node[] nodes;
        Graph(int size){
            this.nodes = new Node[size];
            for (int i = 0; i < size; i++) {
                this.nodes[i] = new Node(i); //size:4 -> 1 2 3 4
            }
        }// constructor

        void addEdge(int i1 , int i2){
            Node n1 = nodes[i1]; // 5 -> [4]
            Node n2 = nodes[i2];
            if(!n1.adjacent.contains(n2)){
                n1.adjacent.add(n2);
            }
            if(!n2.adjacent.contains(n1)){
                n2.adjacent.add(n1);
            }
        }

        // Search Fuctions (Dfs & Bfs) //

        //DFS
        public void dfs() {
            dfs(0);
        }
        public void dfs(int index) {
            Node root = nodes[index];
            Stack<Node> stack = new Stack<Node>();
            stack.push(root);
            while (!stack.isEmpty()) {
                Node parent = stack.pop();
                if (parent.marked) {
                    continue;
                }
                parent.marked  = true;
                visit(parent);
                Collections.sort(parent.adjacent, new Comparator<Node>() {
                    @Override
                    public int compare(Node o1, Node o2) {
                        // 순차 정렬을 해주는 코드(역방향은 부등호를 변경하거나 return 값을 바꿔주면 됨)
                        // if(o1.n > o2.n) : 정순
                        if(o1.data < o2.data)// 역순
                            return +1;
                        else
                            return -1;
                    }
                });
                for (Node child : parent.adjacent) {
                    if (!child.marked) {
                        stack.push(child);
                    }
                }//for
            }//while
        }
        
        //BFS
        public void bfs() {
            bfs(0);
        }
        public void bfs(int index) {
            Node root = nodes[index];
            Queue<Node> queue = new LinkedList<Node>();
            queue.add(root);
            while (!queue.isEmpty()) {
                Node parent = queue.poll();
                if (parent.marked) {
                    continue;
                }
                parent.marked = true;
                Collections.sort(parent.adjacent, new Comparator<Node>() {
                    @Override
                    public int compare(Node o1, Node o2) {
                        // 순차 정렬을 해주는 코드(역방향은 부등호를 변경하거나 return 값을 바꿔주면 됨)
                        if(o1.data > o2.data) //정순
                            return +1;
                        else
                            return -1;
                    }
                });
                for (Node child : parent.adjacent) {
                    if (!child.marked) {
                        queue.add(child);
                    }
                }//for
                visit(parent);
            }//while
        }
        public void InitMarked(){
            for (Node n : this.nodes) {
                n.marked = false;
            }
        }
        public void visit(Node n) {
            System.out.print(n.data+" ");
        }
    }//Graph


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numberOfNodes = scan.nextInt();
        int numberOfEdges = scan.nextInt();
        int start = scan.nextInt();
        Graph graph = new Graph(numberOfNodes+1);

        for (int i = 0; i < numberOfEdges; i++) {
            graph.addEdge(scan.nextInt(), scan.nextInt());
        }
        graph.dfs(start);
        System.out.println();
        graph.InitMarked();
        graph.bfs(start);
        scan.close();
    }
}
