import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;

class main{
    public static void main(String args[]) {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = null;
            conn = DriverManager.getConnection("jdbc:mysql://localhost/test","root","password");
            System.out.println("Database is connected");
            conn.close();
        }
        catch(SQLException e1) {
            e1.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

    }
}
