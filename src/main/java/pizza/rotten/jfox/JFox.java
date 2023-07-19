package pizza.rotten.jfox;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class JFox {

    static boolean hadError = false;

    public static void main(String[] args) throws IOException {
        if (args.length > 1) {
            System.out.println("Usage: jfox [script]");
            System.exit(64);
        } else if (args.length == 1) {
            runFile(args[0]);
        } else {
            runPrompt();
        }
    }

    private static void runFile(String path) throws IOException {
        byte[] bytes = Files.readAllBytes(Paths.get(path));
        run(new String(bytes, Charset.defaultCharset()));

        if (hadError) System.exit(65);
    }

    private static void runPrompt() throws IOException {
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input);

        System.out.println("*** Welcome to Fox (Fabian's Lox) ***\n");
        for (;;) {
            System.out.print("\uD83E\uDD8A ");
            String line = reader.readLine();
            if (line == null) break;
            run(line);

            // if there has been an error, reset it for the next user input
            hadError = false;
        }
    }

    private static void run(String source) {
        Scanner scanner = new Scanner(source);
        List<Token> tokens = scanner.scanTokens();

        // For now, just print the tokens
        for (Token token : tokens) {
            System.out.println(token);
        }
    }

    static void error(int line, String message) {
        hadError = true;
        report(line, "", message);
    }

    private static void report(int line, String where, String message) {
        System.err.println("[line "+line+"] Error " + where + ": "+ message);
    }
}
