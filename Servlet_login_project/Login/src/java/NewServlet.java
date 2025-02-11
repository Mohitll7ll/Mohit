import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet(name = "login", urlPatterns = {"/login"})
public class NewServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            String _username = request.getParameter("Name"); // Changed to match the form input name
            String _password = request.getParameter("pass"); // Changed to match the form input name
            if (_username != null && _password != null) {
                if (_username.equals("Mohit") && _password.equals("12345")) {
                    response.sendRedirect("newhtml.html");
                } else {
                    out.println("Invalid Username or Password"); // Added message for invalid credentials
                }
            } else {
                out.println("Empty Username or password");
            }
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}
