public class Main {

    public static double function(double x) {
        return ((x + 1) * Math.pow((x - 1), 4));
    }

    public static void main(String[] args) {
        // function: (x+1)(x-1)^4 = 0

        double a = -1.5; // dolna granica przedziału
        double b = -0.75; // górna granica przedziału
        double epsilon = 0.1; // epsilon
        int maxIter = 100; // maksymalna liczba iteracji aby uniknąć pętli nieskończonej
        double c; // punkt środkowy
        double f_c; // wartość funkcji w punkcie środkowym

        for (int i = 0; i < maxIter; i++) {
            c = (a + b) / 2;
            f_c = function(c);

            if (Math.abs(f_c) < epsilon) {
                System.out.println("liczba z granic tolerncji\n");
                System.out.println("iteracja: " + (i + 1));
                System.out.println("punkt środkowy: " + c);
                System.out.println("wartość funkcji: " + f_c + "\n");
                break;
            } else if (f_c * function(a) < 0) {
                System.out.println("liczba z lewego końca przedziału\n");
                System.out.println("iteracja: " + (i + 1));
                System.out.println("punkt środkowy: " + c);
                System.out.println("wartość funkcji: " + f_c + "\n");
                b = c;
            } else {
                System.out.println("liczba z prawgo końca przedziłu\n");
                System.out.println("iteracja: " + (i + 1));
                System.out.println("punkt środkowy: " + c);
                System.out.println("wartość funkcji: " + f_c + "\n");
                a = c;
            }
        }
    }
}