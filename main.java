package battleship;
import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		String array[][] = new String[10][10];
		
		array[0][0] = keyboard.nextLine();
		
		System.out.println("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐");
		System.out.println( "│   │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.print( "│ 1 │ ");
		System.out.print( array[0][0]);
		System.out.print( " │   │   │   │   │   │   │   │   │   │\n");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 2 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 3 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 4 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 5 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 6 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 7 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 8 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│ 9 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
		System.out.println( "│10 │   │   │   │   │   │   │   │   │   │   │");
		System.out.println( "└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘");
	}

}
