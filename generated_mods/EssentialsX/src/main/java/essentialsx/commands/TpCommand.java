package essentialsx.commands;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.StringArgumentType;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.LiteralText;
import net.minecraft.util.math.BlockPos;

import static net.minecraft.server.command.CommandManager.argument;
import static net.minecraft.server.command.CommandManager.literal;

public class TpCommand {
    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register(literal("tp")
            .then(argument("target", StringArgumentType.word())
            .executes(context -> {
                ServerCommandSource source = context.getSource();
                String targetName = StringArgumentType.getString(context, "target");
                ServerPlayerEntity targetPlayer = source.getServer().getPlayerManager().getPlayer(targetName);
                if (targetPlayer != null) {
                    BlockPos targetPos = targetPlayer.getBlockPos();
                    source.getPlayer().teleport(targetPos.getX(), targetPos.getY(), targetPos.getZ());
                    source.sendFeedback(new LiteralText("Teleported to " + targetName), false);
                } else {
                    source.sendError(new LiteralText("Player not found: " + targetName));
                }
                return 1;
            })));
    }
}
