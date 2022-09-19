import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Collections;

public class Silver_1260{
    // Inner Class needs static
    static class Graph {
        boolean[] visited;
        ArrayList<Integer>[] adjacents;
        Graph(int size){
            this.visited = new boolean[size+1];
            this.adjacents = new ArrayList[size+1];
            for (int i = 1; i <= size ; i++) {
                adjacents[i] = new ArrayList<Integer>();
            }
        }
        void addEdge(int n1 , int n2){
            if(!adjacents[n1].contains(n2)){
                adjacents[n1].add(n2);
            }
            if(!adjacents[n2].contains(n1)){
                adjacents[n2].add(n1);
            }
        }

        // Search Fuctions (Dfs & Bfs) //

        //DFS
        public void dfs() {
            dfs(1);
        }
        public void dfs(int index) {
            visited[index] = true;
            visit(index);
            Collections.sort(adjacents[index]);
            for (Integer node : adjacents[index]) {
                if (visited[node]==false) {
                    dfs(node);
                }
            }
        }
        
        //BFS
        public void bfs() {
            bfs(1);
        }
        public void bfs(int index) {
            Queue<Integer> queue = new LinkedList<Integer>();
            queue.add(index);
            visited[index] = true;
            while (!queue.isEmpty()) {
                int parent = queue.poll();
                visit(parent);
                Collections.sort(adjacents[index]);
                for (Integer node : adjacents[parent]) {
                    if (visited[node]==false) {
                        queue.add(node);
                        visited[node] = true;
                    }
                }
            }
        }
        public void InitMarked(){
            for (int i = 1; i < visited.length ; i++) {
                visited[i] = false;
            }
        }
        public void visit(int index) {
            System.out.print(index+" ");
        }
    }//Graph


    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int numberOfNodes = Integer.parseInt(st.nextToken());
        int numberOfEdges = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());
        Graph graph = new Graph(numberOfNodes);
        for (int i = 0; i < numberOfEdges; i++) {
            st = new StringTokenizer(br.readLine());
            graph.addEdge(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        br.close();
        graph.dfs(start);
        System.out.println();
        graph.InitMarked();
        graph.bfs(start);
    }
}
