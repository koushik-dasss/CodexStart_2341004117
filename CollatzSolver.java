import java.util.ArrayList;

public class CollatzSolver {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java CollatzSolver <number>");
            return;
        }

        int n = Integer.parseInt(args[0]);

        ArrayList<Integer> sequence = generateCollatzSequence(n);

        // Print the sequence
        for (int num : sequence) {
            System.out.print(num + " ");
        }

        System.out.println("Program completed.");
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
