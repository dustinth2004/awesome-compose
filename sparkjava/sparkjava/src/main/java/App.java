import static spark.Spark.*;

/**
 * A simple Spark Java application.
 */
public class App {
    /**
     * The main entry point for the application.
     *
     * @param args The command line arguments.
     */
    public static void main(String[] args) {
        port(8080);

        get("/", (req, res) -> "Hello from Docker!");
    }
}
