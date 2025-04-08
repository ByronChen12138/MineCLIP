import os
import minecraft_data

from utils.file_utils import append_txt
from utils.json_utils import write_json, append_jsonl, read_jsonl


def get_obj_names(objects, obj_type, out_path="../outs/"):
    # Delete the file if it exists
    try:
        os.remove(f'{out_path}{obj_type}_name.jsonl')
    except OSError:
        pass

    seen = set()

    for key, data in objects.items():
        # If the data have a 'displayName' key, set it to the value of 'name'
        new_json = {}

        try:
            if "displayName" in data:
                if data["displayName"] in seen:
                    print (f"Duplicate name: {data['displayName']}")
                    continue

                new_json['name'] = data["displayName"]
                seen.add(data["displayName"])

            elif 'name' in data:
                if data["name"] in seen:
                    print (f"Duplicate name: {data['name']}")
                    continue

                new_json['name'] = data["name"]
                seen.add(data["name"])

            else:
                print (f"Key {key} does not have a 'name' or 'displayName' key: {data}")
                continue

        except Exception as e:
            print(f"Error processing {key}: {e}")
            continue

        if obj_type == "blocks":
            new_json['action'] = ["Mining", "Placing", "Crafting", "Smelting", "Interacting"]

        elif obj_type == "items":
            if data["name"] == "redstone":
                new_json['action'] = ["Crafting", "Placing", "Mining"]

            # Vehicles
            elif ("banner_pattern" in data["name"] or
                  data["name"] == "saddle" or
                  data["name"] == "oak_boat" or
                  data["name"] == "oak_chest_boat" or
                  data["name"] == "spruce_boat" or
                  data["name"] == "spruce_chest_boat" or
                  data["name"] == "birch_boat" or
                  data["name"] == "birch_chest_boat" or
                  data["name"] == "jungle_boat" or
                  data["name"] == "jungle_chest_boat" or
                  data["name"] == "acacia_boat" or
                  data["name"] == "acacia_chest_boat" or
                  data["name"] == "dark_oak_boat" or
                  data["name"] == "dark_oak_chest_boat" or
                  data["name"] == "mangrove_chest_boat" or
                  data["name"] == "mangrove_boat" or
                  data["name"] == "bucket" or
                  data["name"] == "fire_charge" or
                  data["name"] == "writable_book" or
                  data["name"] == "written_book" or
                  data["name"] == "enchanted_book" or
                  data["name"] == "lead" or
                  data["name"] == "name_tag" or
                  data["name"] == "dragon_breath" or
                  data["name"] == "splash_potion" or
                  data["name"] == "tipped_arrow" or
                  data["name"] == "lingering_potion" or
                  data["name"] == "shulker_shell" or
                  data["name"] == "nautilus_shell"):
                new_json['action'] = ["Crafting", "Interacting"]

            # Tools
            elif (data["name"] == "elytra" or
                  data["name"] == "turtle_helmet" or
                  data["name"] == "bow" or
                  data["name"] == "flint_and_steel" or
                  data["name"] == "wooden_sword" or
                  data["name"] == "wooden_shovel" or
                  data["name"] == "wooden_pickaxe" or
                  data["name"] == "wooden_axe" or
                  data["name"] == "wooden_hoe" or
                  data["name"] == "stone_sword" or
                  data["name"] == "stone_shovel" or
                  data["name"] == "stone_pickaxe" or
                  data["name"] == "stone_axe" or
                  data["name"] == "stone_hoe" or
                  data["name"] == "golden_sword" or
                  data["name"] == "golden_shovel" or
                  data["name"] == "golden_pickaxe" or
                  data["name"] == "golden_axe" or
                  data["name"] == "golden_hoe" or
                  data["name"] == "iron_sword" or
                  data["name"] == "iron_shovel" or
                  data["name"] == "iron_pickaxe" or
                  data["name"] == "iron_axe" or
                  data["name"] == "iron_hoe" or
                  data["name"] == "diamond_sword" or
                  data["name"] == "diamond_shovel" or
                  data["name"] == "diamond_pickaxe" or
                  data["name"] == "diamond_axe" or
                  data["name"] == "diamond_hoe" or
                  data["name"] == "netherite_sword" or
                  data["name"] == "netherite_shovel" or
                  data["name"] == "netherite_pickaxe" or
                  data["name"] == "netherite_axe" or
                  data["name"] == "netherite_hoe" or
                  data["name"] == "leather_helmet" or
                  data["name"] == "leather_chestplate" or
                  data["name"] == "leather_leggings" or
                  data["name"] == "leather_boots" or
                  data["name"] == "chainmail_helmet" or
                  data["name"] == "chainmail_chestplate" or
                  data["name"] == "chainmail_leggings" or
                  data["name"] == "chainmail_boots" or
                  data["name"] == "iron_helmet" or
                  data["name"] == "iron_chestplate" or
                  data["name"] == "iron_leggings" or
                  data["name"] == "iron_boots" or
                  data["name"] == "diamond_helmet" or
                  data["name"] == "diamond_chestplate" or
                  data["name"] == "diamond_leggings" or
                  data["name"] == "diamond_boots" or
                  data["name"] == "golden_helmet" or
                  data["name"] == "golden_chestplate" or
                  data["name"] == "golden_leggings" or
                  data["name"] == "golden_boots" or
                  data["name"] == "netherite_helmet" or
                  data["name"] == "netherite_chestplate" or
                  data["name"] == "netherite_leggings" or
                  data["name"] == "netherite_boots" or
                  data["name"] == "compass" or
                  data["name"] == "recovery_compass" or
                  data["name"] == "bundle" or
                  data["name"] == "fishing_rod" or
                  data["name"] == "clock" or
                  data["name"] == "spyglass" or
                  data["name"] == "shears" or
                  data["name"] == "iron_horse_armor" or
                  data["name"] == "golden_horse_armor" or
                  data["name"] == "diamond_horse_armor" or
                  data["name"] == "leather_horse_armor" or
                  data["name"] == "shield" or
                  data["name"] == "crossbow"):
                new_json['action'] = ["Crafting", "Equipping", "Enchanting", "Repairing"]

            # Collectable Food
            elif (data["name"] == "apple" or
                  data["name"] == "porkchop" or
                  data["name"] == "melon_slice" or
                  data["name"] == "beef" or
                  data["name"] == "rotten_flesh" or
                  data["name"] == "mutton" or
                  data["name"] == "chorus_fruit"):
                new_json['action'] = ["Collecting", "Eating"]

            # Collectable Food (Plantable)
            elif (data["name"] == "carrot" or
                  data["name"] == "potato" or
                  data["name"] == "sweet_berries" or
                  data["name"] == "glow_berries"):
                new_json['action'] = ["Collecting", "Eating", "Planting"]

            # Cookable Food
            elif (data["name"] == "mushroom_stew" or
                  data["name"] == "bread" or
                  data["name"] == "cooked_porkchop" or
                  data["name"] == "golden_apple" or
                  data["name"] == "enchanted_golden_apple" or
                  data["name"] == "cooked_cod" or
                  data["name"] == "cooked_salmon" or
                  data["name"] == "cookie" or
                  data["name"] == "dried_kelp" or
                  data["name"] == "cooked_beef" or
                  data["name"] == "cooked_chicken" or
                  data["name"] == "glistering_melon_slice" or
                  data["name"] == "baked_potato" or
                  data["name"] == "poisonous_potato" or
                  data["name"] == "golden_carrot" or
                  data["name"] == "pumpkin_pie" or
                  data["name"] == "cooked_rabbit" or
                  data["name"] == "rabbit_stew" or
                  data["name"] == "cooked_mutton" or
                  data["name"] == "beetroot_soup" or
                  data["name"] == "suspicious_stew"):
                new_json['action'] = ["Cooking", "Eating"]

            # Ores
            elif (data["name"] == "coal" or
                  data["name"] == "charcoal" or
                  data["name"] == "diamond" or
                  data["name"] == "emerald" or
                  data["name"] == "lapis_lazuli" or
                  data["name"] == "quartz" or
                  data["name"] == "amethyst_shard" or
                  data["name"] == "raw_iron" or
                  data["name"] == "iron_ingot" or
                  data["name"] == "raw_copper" or
                  data["name"] == "copper_ingot" or
                  data["name"] == "raw_gold" or
                  data["name"] == "gold_ingot" or
                  data["name"] == "netherite_ingot" or
                  data["name"] == "netherite_scrap"):

                new_json['action'] = ["Collecting", "Smelting"]

            elif (data["name"] == "bowl" or
                  data["name"] == "totem_of_undying"):
                new_json['action'] = ["Crafting"]

            # Intermediate Materials
            elif ("dye" in data["name"] or
                  "disc_fragment" in data["name"] or
                  data["name"] == "stick" or
                  data["name"] == "paper" or
                  data["name"] == "book" or
                  data["name"] == "glow_ink_sac" or
                  data["name"] == "bone_meal" or
                  data["name"] == "sugar" or
                  data["name"] == "filled_map" or
                  data["name"] == "gold_nugget" or
                  data["name"] == "glass_bottle" or
                  data["name"] == "blaze_powder" or
                  data["name"] == "magma_cream" or
                  data["name"] == "map" or
                  data["name"] == "firework_star" or
                  data["name"] == "nether_brick" or
                  data["name"] == "popped_chorus_fruit" or
                  data["name"] == "iron_nugget" or
                  data["name"] == "heart_of_the_sea" or
                  data["name"] == "goat_horn"):
                new_json['action'] = ["Crafting", "Collecting"]

            # Materials
            elif (data["name"] == "string" or
                  data["name"] == "feather" or
                  data["name"] == "gunpowder" or
                  data["name"] == "flint" or
                  data["name"] == "leather" or
                  data["name"] == "brick" or
                  data["name"] == "clay_ball" or
                  data["name"] == "slime_ball" or
                  data["name"] == "glowstone_dust" or
                  data["name"] == "ink_sac" or
                  data["name"] == "cocoa_beans" or
                  data["name"] == "bone" or
                  data["name"] == "blaze_rod" or
                  data["name"] == "ghast_tear" or
                  data["name"] == "spider_eye" or
                  data["name"] == "fermented_spider_eye" or
                  data["name"] == "nether_star" or
                  data["name"] == "prismarine_crystals" or
                  data["name"] == "rabbit_hide" or
                  data["name"] == "prismarine_shard" or
                  data["name"] == "honeycomb" or
                  data["name"] == "echo_shard"):
                new_json['action'] = ["Collecting"]

            # Seeds
            elif (data["name"] == "wheat_seeds" or
                  data["name"] == "pumpkin_seeds" or
                  data["name"] == "melon_seeds" or
                  data["name"] == "beetroot_seeds" or
                  data["name"] == "beetroot"):
                new_json['action'] = ["Crafting", "Collecting", "Planting"]

            # Buckets
            elif ("music_disc" in data["name"] or
                  data["name"] == "water_bucket" or
                  data["name"] == "lava_bucket" or
                  data["name"] == "powder_snow_bucket" or
                  data["name"] == "milk_bucket" or
                  data["name"] == "pufferfish_bucket" or
                  data["name"] == "salmon_bucket" or
                  data["name"] == "cod_bucket" or
                  data["name"] == "tropical_fish_bucket" or
                  data["name"] == "axolotl_bucket" or
                  data["name"] == "tadpole_bucket" or
                  data["name"] == "rabbit_foot" or
                  data["name"] == "knowledge_book" or
                  data["name"] == "phantom_membrane" or
                  data["name"] == "honey_bottle"):
                new_json['action'] = ["Collecting", "Interacting"]

            # Spawn Eggs
            elif "spawn_egg" in data["name"]:
                new_json['action'] = ["Using"]

            else:
                print(f'IGNORED - "Items" {key}: {data}')
                continue

        # elif obj_type == "instruments":
            # new_json['action'] = ["Playing"]

        elif obj_type == "entities":
            category = data["category"]

            if category == "Passive mobs":
                new_json['action'] = ["Killing", "Breeding", "Taming"]

            elif category == "Hostile mobs":
                new_json['action'] = ["Killing"]

            elif category == "Vehicles":
                new_json['action'] = ["Crafting", "Interacting"]

            elif category == "Projectiles":
                new_json['action'] = ["Throwing"]

            elif category == "Immobile":
                if (data["name"] == "armor_stand" or
                    data ["name"] == "item_frame" or
                    data ["name"] == "glow_item_frame" or
                    data ["name"] == "leash_knot"):

                    new_json['action'] = ["Crafting", "Interacting", "Mining", "Placing"]

                elif data["name"] == "end_crystal":
                    new_json['action'] = ["Crafting", "Interacting", "Mining", "Attacking"]

                elif data["name"] == "painting":
                    new_json['action'] = ["Crafting", "Mining", "Placing"]

                else:
                    print(f'IGNORED - "Immobile" {key}: {data}')
                    continue

            elif category == "UNKNOWN":
                if data["name"] == "lightning_bolt":
                    new_json['action'] = ["Hitting by"]

                elif data["name"] == "player":
                    new_json['action'] = ["Killing"]

                elif data["name"] == "experience_orb":
                    new_json['action'] = ["Collecting"]

                elif data["name"] == "eye_of_ender":
                    new_json['action'] = ["Crafting", "Interacting"]

                elif data["name"] == "tnt":
                    new_json['action'] = ["Crafting", "Igniting", "Mining", "Placing"]


                else:
                    print(f'IGNORED - "UNKNOWN" {key}: {data}')
                    continue

            else:
                print (f"Un-categorized for {key}: {category}")
                continue


        else:
            print(f"Unknown object type: {obj_type}")
            continue

        append_jsonl(f'{out_path}{obj_type}_name.jsonl', [new_json])


def generate_labels(objects, out_path="../labels.txt"):
    if os.path.exists(out_path):
        os.remove(out_path)

    for obj in objects:
        for verb in obj.get('action'):
            append_txt(out_path, f'{verb} {obj["name"]}')


def main():
    mc_data = minecraft_data("1.19")

    # Get the dictionary of all blocks
    blocks = mc_data.blocks_name
    items = mc_data.items_name
    # instruments = mc_data.instruments
    # materials = mc_data.materials
    entities = mc_data.entities_name

    # print(blocks)
    # print(items)
    # print(instruments)
    # print(materials)
    # print(entities)

    new_items = {}

    for key, value in items.items():
        if key not in blocks.keys() and key not in entities.keys():
            new_items[key] = value

    # new_instruments = {}
    # for key, value in instruments.items():
    #     new_instruments[value.get('name')] = value


    get_obj_names(blocks, "blocks")
    get_obj_names(new_items, "items")
    # get_obj_names(new_instruments, "instruments")
    # get_obj_names(materials, "materials")
    get_obj_names(entities, "entities")

    # Generate labels for all objects
    all_objects = []
    all_objects.extend(read_jsonl("../outs/blocks_name.jsonl"))
    all_objects.extend(read_jsonl("../outs/items_name.jsonl"))
    # all_objects.extend(read_jsonl("../outs/instruments_name.jsonl"))
    # all_objects.extend(read_jsonl("../outs/materials_name.jsonl"))
    all_objects.extend(read_jsonl("../outs/entities_name.jsonl"))

    print(len(all_objects))
    generate_labels(all_objects)

    # Merge all dictionaries into one
    all_data = {
        **blocks,
        **items,
        # **new_instruments,
        # **materials,
        **entities,
    }

    # Write the merged dictionary to a JSON file
    write_json("../outs/mc_data.json", all_data)


if __name__ == "__main__":
    main()