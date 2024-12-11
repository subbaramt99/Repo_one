package Inheritance;

import Hierarchical_Inheritance.maths;
import Hierarchical_Inheritance.physics;
import Hierarchical_Inheritance.social;
import Hierarchical_Inheritance.student;

public class Hybrid {
	
	public static void main(String[] args) {
		student Std = new student();
		physics P = new physics();
		maths M = new maths();
		social S = new social();
		
		Std.S_student();
		P.S_student();
		P.P_physics();
		M.S_student();
		S.S_student();
		S.S_social();
	}
	

}

