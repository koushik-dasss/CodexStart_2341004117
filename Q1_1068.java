import java.util.ArrayList;
import java.util.Scanner;

public class CollatzConjecture {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();

        ArrayList<Integer> sequence = generateCollatzSequence(n);

        // Print the sequence
        for (int num : sequence) {
            System.out.print(num + " ");
        }
    }

    private static ArrayList<Integer> generateCollatzSequence(int n) {
        ArrayList<Integer> sequence = new ArrayList<>();
        while (n != 1) {
            sequence.add(n);
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
        }
        sequence.add(1); // Add the last element (1) to the sequence
        return sequence;
    }
}
