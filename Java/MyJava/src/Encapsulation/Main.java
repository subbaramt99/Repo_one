package Encapsulation;

public class Main {
	public static void main (String[] args) {
		Person person = new Person("subbaram", 26);
		
		System.out.println(person.getName());
		System.out.println(person.getAge());
		person.setName("Samurai");
		person.setAge(23);
		
		System.out.println(person.getName());
		System.out.println(person.getAge());
	}

}
