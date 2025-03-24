package Inheritance;
// ********************Single level inheritance *********************
public class programmer extends employee{
	int bouns = 1000;
	public static void main(String[] args) {
		programmer P = new programmer();
		System.out.println("Programmer salary is:" +P.salary);
		System.out.println("Bonus of Programmer is:" +P.bouns);
	}
}
