package Inheritance;
//************************ Multilevel inheritance ********************************
public class tester extends programmer{
	int bonus1 = 500;
	public static void main(String[] args) {
		tester T = new tester();
		System.out.println("Salary of Programmer is:" +T.salary);
		System.out.println("Bonus of Programmer is:" +T.bouns);
		System.out.println("Bonus of Tester is:" +T.bonus1);
	}

}
