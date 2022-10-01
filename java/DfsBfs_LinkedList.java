import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;


public class DfsBfs_LinkedList {
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
                this.nodes[i] = new Node(i);
            }
        }// constructor

        void addEdge(int i1 , int i2){
            Node n1 = nodes[i1];
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
            root.marked = true;
            while (!stack.isEmpty()) {
                Node parent = stack.pop();
                for (Node child : parent.adjacent) {
                    if (!child.marked) {
                        child.marked = true;
                        stack.push(child);
                    }
                }//for
                visit(parent);
            }//while
        }

        //DFS Recursion
        void dfsR(Node root){
            root.marked = true;
            visit(root);
            for (Node n : root.adjacent) {
                if (n.marked == false) {
                    dfsR(n);
                }
            }
        }

        //BFS
        public void bfs() {
            bfs(0);
        }
        public void bfs(int index) {
            Node root = nodes[index];
            Queue<Node> queue = new LinkedList<Node>();
            queue.add(root);
            root.marked = true;
            while (!queue.isEmpty()) {
                Node parent = queue.poll();
                for (Node child : parent.adjacent) {
                    if (!child.marked) {
                        child.marked = true;
                        queue.add(child);
                    }
                }//for
                visit(parent);
            }//while
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
        Graph graph = new Graph(numberOfNodes);

        for (int i = 0; i < numberOfEdges; i++) {
            graph.addEdge(scan.nextInt(), scan.nextInt());
        }
        graph.dfs(start); //startIndex = start - 1
        graph.dfsR(graph.nodes[start]);
        scan.close();
    }
}
