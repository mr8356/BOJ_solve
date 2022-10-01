import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Gold_2589 {
    static int boxWidth;
    static int boxHeight;
    static boolean[][] box;
    
    static class Land{
        int x;
        int y;
        int time;
        Land(int x , int y){
            this.x = x;
            this.y = y;
            this.time = 0;
        }
        Land(int x , int y , int time){
            this.x = x;
            this.y = y;
            this.time = time;
        }
        boolean isSame(Land otherLand){
            if(this.x == otherLand.x && this.y == otherLand.y){
                return true;
            }
            return false;
        }
    }
    static boolean isInside(int x , int y){
        if( x>=0 && x<boxWidth)
            if( y>=0 && y<boxHeight)
                return true;
        return false;
    }
    static int bfs(Land l1){
        Queue<Land> queue = new LinkedList<Land>();
        queue.add(l1);
        boolean[][] boxCopy = box.clone();
        int distance =10;
        while (!queue.isEmpty()) {
            Land startLand = queue.poll();
            if (isInside(startLand.x+1 , startLand.y) && boxCopy[startLand.x+1][startLand.y]) {
                queue.add(new Land(startLand.x+1, startLand.y , startLand.time + 1));
                boxCopy[startLand.x+1][startLand.y] = false;
                distance =Math.max(distance, startLand.time+1);

            }
            if (isInside(startLand.x-1 , startLand.y) && boxCopy[startLand.x-1][startLand.y]) {
                queue.add(new Land(startLand.x-1, startLand.y , startLand.time + 1));
                boxCopy[startLand.x-1][startLand.y] =false;
                distance =Math.max(distance, startLand.time+1);

            }
            if (isInside(startLand.x , startLand.y+1) && boxCopy[startLand.x][startLand.y+1]) {
                queue.add(new Land(startLand.x, startLand.y+1 , startLand.time + 1));
                boxCopy[startLand.x][startLand.y+1] = false;
                distance =Math.max(distance, startLand.time+1);

            }
            if (isInside(startLand.x , startLand.y-1) && boxCopy[startLand.x][startLand.y-1]) {
                queue.add(new Land(startLand.x, startLand.y-1 , startLand.time + 1));
                boxCopy[startLand.x][startLand.y-1] = false;
                distance =Math.max(distance, startLand.time+1);
            }
        }
        return distance; // can't go (except from 보물섬)
    }
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        boxHeight = Integer.parseInt(st.nextToken());
        boxWidth = Integer.parseInt(st.nextToken());
        box = new boolean[boxWidth][boxHeight];
        ArrayList<Land> lands = new ArrayList<Land>();
        for (int i = 0; i < boxHeight; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < boxWidth; j++) {
                if (input[j] == 'W') {
                    box[j][i] = false;// can't go across
                }
                else{
                    box[j][i] = true; // L -> can go across
                    lands.add(new Land(j, i));
                }
            }
        }
        br.close();
        int maxTime = -1;
        // 백트래킹 알고리즘(조합). 순서쌍 임의로 2개씩 뽑고 중복 제거.
        for (Land land : lands) {
            maxTime = Math.max(bfs(land), maxTime);
        }
        System.out.println(maxTime);
    }
}
