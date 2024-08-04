import org.bukkit.plugin.PluginDescriptionFile;
import java.io.File;
import java.util.jar.JarFile;
import org.yaml.snakeyaml.Yaml;
import java.io.InputStream;
import java.util.Map;

public class PluginParser {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java PluginParser <plugin-jar-file>");
            return;
        }

        String pluginJarPath = args[0];
        try {
            JarFile jarFile = new JarFile(new File(pluginJarPath));
            InputStream input = jarFile.getInputStream(jarFile.getEntry("plugin.yml"));
            Yaml yaml = new Yaml();
            Map<String, Object> data = yaml.load(input);

            System.out.println("Plugin Name: " + data.get("name"));
            System.out.println("Plugin Version: " + data.get("version"));
            System.out.println("Main Class: " + data.get("main"));
            System.out.println("Commands: " + data.get("commands"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
