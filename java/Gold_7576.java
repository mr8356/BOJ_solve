import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Gold_7576 {
    static Queue<Tomato> queue;
    static int boxWidth;
    static int boxHeight;
    static int[][] box;
    
    static class Tomato{
        int x;
        int y;
        int time;
        Tomato(int x , int y){
            this.x = x;
            this.y = y;
            this.time = 0;
        }
        Tomato(int x , int y , int time){
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }
    static boolean isinside(int x , int y){
        if( x>=0 && x<boxWidth)
            if( y>=0 && y<boxHeight)
                return true;
        return false;
    }
    static int bfs(){
        int cnt = 0;
        while (!queue.isEmpty()) {
            Tomato ripe = queue.poll();
            if (isinside(ripe.x+1 , ripe.y) && box[ripe.x+1][ripe.y] == 0) {
                queue.add(new Tomato(ripe.x+1, ripe.y , ripe.time + 1));
                box[ripe.x+1][ripe.y] = 1;
                cnt = ripe.time + 1;

            }
            if (isinside(ripe.x-1 , ripe.y) && box[ripe.x-1][ripe.y] == 0) {
                queue.add(new Tomato(ripe.x-1, ripe.y , ripe.time + 1));
                box[ripe.x-1][ripe.y] =1;
                cnt = ripe.time + 1;

            }
            if (isinside(ripe.x , ripe.y+1) && box[ripe.x][ripe.y+1] == 0) {
                queue.add(new Tomato(ripe.x, ripe.y+1 , ripe.time + 1));
                box[ripe.x][ripe.y+1] = 1;
                cnt = ripe.time + 1;

            }
            if (isinside(ripe.x , ripe.y-1) && box[ripe.x][ripe.y-1] == 0) {
                queue.add(new Tomato(ripe.x, ripe.y-1 , ripe.time + 1));
                box[ripe.x][ripe.y-1] = 1;
                cnt = ripe.time + 1;
            }
            //
        }
        for (int i = 0; i < boxWidth; i++) {
            for (int j = 0; j < boxHeight; j++) {
                if(box[i][j] == 0)
                    return -1;
            }
        }
        return cnt;
    }
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        boxWidth = Integer.parseInt(st.nextToken());
        boxHeight = Integer.parseInt(st.nextToken());
        box = new int[boxWidth][boxHeight];
        queue = new LinkedList<Tomato>();
        for (int i = 0; i < boxHeight; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < boxWidth; j++) {
                int input = Integer.parseInt(st.nextToken());
                box[j][i] = input;
                if (input == 1) {
                    queue.add(new Tomato(j, i));
                }
            }
        }
        br.close();
        System.out.println(bfs());
    }
}
