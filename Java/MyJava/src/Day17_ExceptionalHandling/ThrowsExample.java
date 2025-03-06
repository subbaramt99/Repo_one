package Day17_ExceptionalHandling;

import java.io.FileReader;
import java.io.IOException;

public class ThrowsExample {
	static void readFile() throws IOException {
		FileReader file = new FileReader("putty.txt");
	}
	public static void main(String[] args) {
		try {
			readFile();
		}
		catch(IOException e) {
			System.out.println("File is not found");
		}
	}
}
