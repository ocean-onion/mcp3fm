package essentialsx.commands;

import com.mojang.brigadier.CommandDispatcher;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.LiteralText;

import static net.minecraft.server.command.CommandManager.literal;

public class HealCommand {
    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register(literal("heal")
            .executes(context -> {
                ServerCommandSource source = context.getSource();
                ServerPlayerEntity player = source.getPlayer();
                player.setHealth(player.getMaxHealth());
                source.sendFeedback(new LiteralText("You have been healed!"), false);
                return 1;
            }));
    }
}
