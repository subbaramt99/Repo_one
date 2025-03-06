package Encapsulation;

public class Person {
	// Private variables 
	private String name;
	private int age;
	
	// Constructor
	public Person (String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	// Getting name 
	public String getName() {
		return name;
	}
	
	// Setting name
	public void setName(String name) {
		this.name = name;
	}
	
	// Getting age 
	public int getAge () {
		return age;
	}
	
	// Setting age
	public void setAge(int age) {
		this.age = age;
	}

}
