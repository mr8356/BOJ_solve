import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;
import java.util.StringTokenizer;

//  24479(DFS), 24444(BFS) 문제

public class Silver_24479 {
    // Inner Class needs static
    static class Graph {
        int visitedNodes;
        class Node{
            int data;
            int sequence;
            ArrayList<Node> adjacent;
            boolean marked;
            Node(int data){
                this.data = data;
                this.sequence = 0;
                this.adjacent = new ArrayList<Node>();
                this.marked = false;
            }// constructor
        }//Node

        Node[] nodes;
        Graph(int size){
            this.visitedNodes = 1;
            this.nodes = new Node[size];
            for (int i = 1; i < size; i++) {
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
        void dfsR(Node root){
            if(root == null) return;
            root.sequence = visitedNodes;
            visitedNodes++;
            Collections.sort(root.adjacent, new Comparator<Node>() {
                @Override
                public int compare(Node o1, Node o2) {
                    // 순차 정렬을 해주는 코드(역방향은 부등호를 변경하거나 return 값을 바꿔주면 됨)
                    if(o1.data > o2.data)
                        return +1;
                    else
                        return -1;
                }
            });
            for (Node n : root.adjacent) {
                if (n.marked == false) {
                    n.marked = true;
                    dfsR(n);
                }
            }
        }
    }//Graph


    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int numberOfNodes = Integer.parseInt(st.nextToken());
        int numberOfEdges = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());
        Graph graph = new Graph(numberOfNodes+1);
        for (int i = 0; i < numberOfEdges; i++) {
            st = new StringTokenizer(br.readLine());
            graph.addEdge(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        br.close();
        graph.nodes[start].marked = true;
        graph.dfsR(graph.nodes[start]);
        for (int i = 1; i <= numberOfNodes; i++) {
            System.out.println(graph.nodes[i].sequence);
        }
    }
}
