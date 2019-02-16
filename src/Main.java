import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;
public class main {
	try {
		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = null;
		conn = DriverManager.getConnection("jdbc:mysql://localhost/test","root","password");
		System.out.println("Database is connected");
		conn.close();
	}
	catch(Exception e) {
		e.printStackTrace();
	}
	
	
}
