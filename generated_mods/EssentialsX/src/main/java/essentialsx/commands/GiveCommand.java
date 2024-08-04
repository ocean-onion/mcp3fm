package essentialsx.commands;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.StringArgumentType;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.text.LiteralText;

import static net.minecraft.server.command.CommandManager.argument;
import static net.minecraft.server.command.CommandManager.literal;

public class GiveCommand {
    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register(literal("give")
            .then(argument("item", StringArgumentType.word())
            .executes(context -> {
                ServerCommandSource source = context.getSource();
                String itemName = StringArgumentType.getString(context, "item");
                Item item = getItemByName(itemName);
                if (item != null) {
                    ItemStack stack = new ItemStack(item, 1);
                    source.getPlayer().giveItemStack(stack);
                    source.sendFeedback(new LiteralText("Given " + itemName), false);
                } else {
                    source.sendError(new LiteralText("Item not found: " + itemName));
                }
                return 1;
            })));
    }

    private static Item getItemByName(String itemName) {
        switch (itemName.toLowerCase()) {
            case "diamond":
                return Items.DIAMOND;
            case "gold_ingot":
                return Items.GOLD_INGOT;
            case "iron_ingot":
                return Items.IRON_INGOT;
            default:
                return null;
        }
    }
}
