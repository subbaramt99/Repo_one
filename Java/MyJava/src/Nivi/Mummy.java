package Nivi;
import Subbu.Daddy;

public class Mummy {


	public static void task1() {
		System.out.println("Mummy is doing public work");
	}
	private static void task2() {
		System.out.println("Mummy is doing private work");
		Daddy.task1();
	}
    public static void main(String[] args) {
        System.out.println("Hello World mummy");
        Daddy.task1();
        Mummy.task2();
    }
}
