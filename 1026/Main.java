import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(2, 4, 5);
        Iterator<Integer> iter = list.iterator();
        printStuff(iter);
    }

    public static void printStuff(Iterator<Integer> iter) {
        while (iter.next() != null)  {
            System.out.print(iter.next() + " ");
        }
    }
}
