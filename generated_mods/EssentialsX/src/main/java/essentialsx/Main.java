package essentialsx;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.command.v1.CommandRegistrationCallback;
import essentialsx.commands.TpCommand;
import essentialsx.commands.GiveCommand;
import essentialsx.commands.HealCommand;

public class Main implements ModInitializer {
    @Override
    public void onInitialize() {
        System.out.println("Initializing EssentialsX");

        // Register tp command
        CommandRegistrationCallback.EVENT.register((dispatcher, dedicated) -> {
            TpCommand.register(dispatcher);
        });

        // Register give command
        CommandRegistrationCallback.EVENT.register((dispatcher, dedicated) -> {
            GiveCommand.register(dispatcher);
        });

        // Register heal command
        CommandRegistrationCallback.EVENT.register((dispatcher, dedicated) -> {
            HealCommand.register(dispatcher);
        });
    }
}
