import java.io. BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class F {
    public void read(){
        Path ruta = Paths.get(first:"note.txt");
        try (BufferedReader br = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
            String linea;
            while ((linea = br.readLine() ) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
Run | Debug
public static void main(String[] args){
    F f =new F();
    f.read();
 }
