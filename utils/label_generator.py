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

                elif "Planks" in data["displayName"]:
                    if "Planks" in seen:
                        print (f"Duplicate type: 'Planks' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Planks"
                        seen.add("Planks")
                    continue

                elif "Sapling" in data["displayName"] or "Propagule" in data["displayName"] or "Bamboo Shoot" in data["displayName"]:
                    if "Sapling" in seen:
                        print (f"Duplicate type: 'Sapling' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Sapling"
                        seen.add("Sapling")
                    continue

                elif "Log" in data["displayName"] or "Crimson Stem" in data["displayName"] or "Warped Stem" in data["displayName"]:
                    if "Log" in seen:
                        print (f"Duplicate type: 'Log' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Log"
                        seen.add("Log")
                    continue

                elif "Leaves" in data["displayName"] or data["displayName"] == "Mangrove Roots":
                    if "Leaves" in seen:
                        print (f"Duplicate type: 'Leaves' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Leaves"
                        seen.add("Leaves")
                    continue

                elif "Wood" in data["displayName"] or "Crimson Hyphae" in data["displayName"] or "Warped Hyphae" in data["displayName"]:
                    if "Wood" in seen:
                        print (f"Duplicate type: 'Wood' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Wood"
                        seen.add("Wood")
                    continue

                elif "Glass" in data["displayName"]:
                    if "Glass" in seen:
                        print (f"Duplicate type: 'Glass' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Glass"
                        seen.add("Glass")
                    continue

                elif "Wool" in data["displayName"]:
                    if "Wool" in seen:
                        print (f"Duplicate type: 'Wool' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Wool"
                        seen.add("Wool")
                    continue

                elif "Stairs" in data["displayName"]:
                    if "Stairs" in seen:
                        print (f"Duplicate type: 'Stairs' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Stairs"
                        seen.add("Stairs")
                    continue

                elif "Sign" in data["displayName"]:
                    if "Sign" in seen:
                        print (f"Duplicate type: 'Sign' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Sign"
                        seen.add("Sign")
                    continue

                elif "Door" in data["displayName"]:
                    if "Door" in seen:
                        print (f"Duplicate type: 'Door' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Door"
                        seen.add("Door")
                    continue

                elif "Copper" in data["displayName"]:
                    if "Copper" in seen:
                        print (f"Duplicate type: 'Copper' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Copper"
                        seen.add("Copper")
                    continue

                elif "Concrete" in data["displayName"]:
                    if "Concrete" in seen:
                        print (f"Duplicate type: 'Concrete' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Concrete"
                        seen.add("Concrete")
                    continue

                elif "Plate" in data["displayName"]:
                    if "Plate" in seen:
                        print (f"Duplicate type: 'Plate' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Plate"
                        seen.add("Plate")
                    continue

                elif "Button" in data["displayName"]:
                    if "Button" in seen:
                        print (f"Duplicate type: 'Button' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Button"
                        seen.add("Button")
                    continue

                elif "Wall" in data["displayName"]:
                    if "Wall" in seen:
                        print (f"Duplicate type: 'Wall' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Wall"
                        seen.add("Wall")
                    continue

                # Flower
                elif (data["name"] == "dandelion" or
                      data["name"] == "blue_orchid" or
                      data["name"] == "allium" or
                      data["name"] == "azure_bluet" or
                      data["name"] == "red_tulip" or
                      data["name"] == "orange_tulip" or
                      data["name"] == "white_tulip" or
                      data["name"] == "pink_tulip" or
                      data["name"] == "oxeye_daisy" or
                      data["name"] == "cornflower" or
                      data["name"] == "wither_rose" or
                      data["name"] == "lily_of_the_valley" or
                      "potted_" in data["name"] or
                      data["name"] == "sunflower" or
                      data["name"] == "lilac" or
                      data["name"] == "peony" or
                      data["name"] == "poppy"):

                    if "Flower" in seen:
                        print(f"Duplicate type: 'Flower' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Flower"
                        seen.add("Flower")
                    continue

                # Fence
                elif "Fence" in data["displayName"]:
                    if "Fence" in seen:
                        print(f"Duplicate type: 'Fence' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Fence"
                        seen.add("Fence")
                    continue

                # Carpet
                elif "Carpet" in data["displayName"]:
                    if "Carpet" in seen:
                        print(f"Duplicate type: 'Carpet' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Carpet"
                        seen.add("Carpet")
                    continue

                # Trapdoor
                elif "Trapdoor" in data["displayName"]:
                    if "Trapdoor" in seen:
                        print(f"Duplicate type: 'Trapdoor' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Trapdoor"
                        seen.add("Trapdoor")
                    continue

                # Bars
                elif "Bars" in data["displayName"]:
                    if "Bars" in seen:
                        print (f"Duplicate type: 'Bars' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Bars"
                        seen.add("Bars")
                    continue

                # Bricks
                elif "Bricks" in data["displayName"]:
                    if "Bricks" in seen:
                        print (f"Duplicate type: 'Bricks' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Bricks"
                        seen.add("Bricks")
                    continue

                # Anvil
                elif "Anvil" in data["displayName"]:
                    if "Anvil" in seen:
                        print (f"Duplicate type: 'Anvil' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Anvil"
                        seen.add("Anvil")
                    continue

                # Cauldron
                elif "Cauldron" in data["displayName"]:
                    if "Cauldron" in seen:
                        print (f"Duplicate type: 'Cauldron' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Cauldron"
                        seen.add("Cauldron")
                    continue

                # Terracotta
                elif "Terracotta" in data["displayName"]:
                    if "Terracotta" in seen:
                        print (f"Duplicate type: 'Terracotta' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Terracotta"
                        seen.add("Terracotta")
                    continue

                # Slab
                elif "Slab" in data["displayName"]:
                    if "Slab" in seen:
                        print (f"Duplicate type: 'Slab' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Slab"
                        seen.add("Slab")
                    continue

                elif "Bed" in data["displayName"]:
                    if "Bed" in seen:
                        print (f"Duplicate type: 'Bed' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Bed"
                        seen.add("Bed")
                    continue

                elif "Shulker Box" in data["displayName"]:
                    if "Shulker Box" in seen:
                        print (f"Duplicate type: 'Shulker Box' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Shulker Box"
                        seen.add("Shulker Box")
                    continue

                elif "Coral Block" in data["displayName"]:
                    if "Coral Block" in seen:
                        print (f"Duplicate type: 'Coral Block' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Coral Block"
                        seen.add("Coral Block")
                    continue

                elif "Coral" in data["displayName"]:
                    if data["displayName"] in seen:
                        print(f"Duplicate name: {data['displayName']}")
                        continue

                    new_json['name'] = data["displayName"]
                    seen.add(data["displayName"])

                elif "Vines" in data["displayName"]:
                    if "Vines" in seen:
                        print (f"Duplicate type: 'Vines' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Vines"
                        seen.add("Vines")
                    continue

                elif "Candle" in data["displayName"]:
                    if "Candle" in seen:
                        print (f"Duplicate type: 'Candle' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Candle"
                        seen.add("Candle")
                    continue

                elif "Amethyst Cluster" in data["displayName"] or "Amethyst Bud" in data["displayName"]:
                    if "Amethyst Cluster" in seen:
                        print (f"Duplicate type: 'Amethyst Cluster' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Amethyst Cluster"
                        seen.add("Amethyst Cluster")
                    continue

                elif "Dripleaf" in data["displayName"]:
                    if "Dripleaf" in seen:
                        print (f"Duplicate type: 'Dripleaf' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Dripleaf"
                        seen.add("Dripleaf")
                    continue

                elif "Deepslate" in data["displayName"]:
                    if "Deepslate" in seen:
                        print (f"Duplicate type: 'Deepslate' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Deepslate"
                        seen.add("Deepslate")
                    continue

                elif "Froglight" in data["displayName"]:
                    if "Froglight" in seen:
                        print (f"Duplicate type: 'Froglight' name: {data['displayName']}")
                    else:
                        new_json['name'] = "Froglight"
                        seen.add("Froglight")
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
            # new_json['action'] = ["Mining", "Placing", "Crafting", "Smelting", "Interacting"]

            # Pre-defined types:
            # Planks
            if data["displayName"] == "Planks":
                new_json['action'] = ["Crafting", "Placing", "Collecting", "Smelting"]
                continue

            # Sapling / Propagule
            elif data["displayName"] == "Sapling":
                new_json['action'] = ["Planting", "Collecting"]
                continue

            elif data["displayName"] == "Log":
                new_json['action'] = ["Placing", "Collecting", "Smelting"]
                continue

            # Breaking-only blocks
            elif ("Fern" in data["displayName"] or
                  "Bush" in data["displayName"] or
                  "Seagrass" in data["displayName"] or
                  "Dripleaf" in data["displayName"] or
                  "Coral" in data["displayName"] or
                  "Vines" in data["displayName"] or
                  "Amethyst Cluster" in data["displayName"] or
                  data["displayName"] == "Leaves" or
                  data["displayName"] == "Grass" or
                  data["displayName"] == "Spawner" or
                  data["displayName"] == "Snow" or
                  data["displayName"] == "Glow Lichen" or
                  data["displayName"] == "Lily Pad" or
                  data["displayName"] == "Nether Wart" or
                  data["displayName"] == "Cocoa" or
                  data["displayName"] == "Flower Pot" or
                  data["displayName"] == "Tall Grass" or
                  data["displayName"] == "Chorus Flower" or
                  data["displayName"] == "Beetroots" or
                  data["displayName"] == "Frosted Ice" or
                  data["displayName"] == "Chorus Plant" or
                  data["displayName"] == "End Gateway" or
                  data["displayName"] == "Sea Pickle" or
                  data["displayName"] == "Warped Fungus" or
                  data["displayName"] == "Warped Roots" or
                  data["displayName"] == "Nether Sprouts" or
                  data["displayName"] == "Crimson Fungus" or
                  data["displayName"] == "Crimson Roots" or
                  data["displayName"] == "Bee Nest" or
                  data["displayName"] == "Budding Amethyst" or
                  data["displayName"] == "Pointed Dripstone" or
                  data["displayName"] == "Azalea" or
                  data["displayName"] == "Flowering Azalea" or
                  data["displayName"] == "Mud" or
                  data["displayName"] == "Frogspawn" or
                  data["displayName"] == "Cobweb"):

                new_json['action'] = ["Breaking", "Collecting"]
                continue

            elif data["displayName"] == "Wood":
                new_json['action'] = ["Placing", "Collecting", "Crafting"]
                continue

            elif data["displayName"] == "Bamboo":
                new_json['action'] = ["Planting", "Collecting", "Crafting"]
                continue

            elif data["displayName"] == "Glass":
                new_json['action'] = ["Placing", "Breaking", "Dying"]
                continue

            elif data["displayName"] == "Wool" or data["displayName"] == "Terracotta" or data["displayName"] == "Candle":
                new_json['action'] = ["Placing", "Collecting", "Dying"]
                continue

            elif (data["displayName"] == "Flower" or
                  data["displayName"] == "Red Mushroom" or
                  data["displayName"] == "Wheat Crops" or
                  data["displayName"] == "Sugar Cane" or
                  data["displayName"] == "Kelp" or
                  data["displayName"] == "Kelp Plant" or
                  data["displayName"] == "Brown Mushroom"):

                new_json['action'] = ["Collecting", "Cooking", "Planting", "Crafting"]
                continue

            # Air
            if data["name"] == "air":
                print(f'IGNORED - "Air"')
                continue

            elif "Banner" in data["displayName"]:
                print(f'IGNORED - "Banner": {data["displayName"]}')
                continue

            elif "Smooth" in data["displayName"]:
                print(f'IGNORED - "Smooth Blocks": {data["displayName"]}')
                continue

            # Food
            elif (data["name"] == "melon" or
                  data["name"] == "turtle_egg" or
                  data["name"] == "pumpkin"):
                new_json['action'] = ["Planting", "Eating", "Collecting"]
                continue

            # Food Stem
            elif (data["name"] == "melon_stem" or
                  data["name"] == "pumpkin_stem"):
                new_json['action'] = ["Planting", "Collecting"]
                continue

            elif data["name"] == "cake":
                new_json['action'] = ["Placing", "Eating", "Making"]
                continue

            elif data["name"] == "carved_pumpkin":
                new_json['action'] = ["Placing", "Collecting", "Crafting", "Equipping"]
                continue

            elif data["name"] == "nether_portal" or data["name"] == "end_portal":
                new_json['action'] = ["Making", "Using"]
                continue

            elif data["name"] == "farmland":
                new_json['action'] = ["Breaking", "Tilling", "Farming on"]
                continue

            # Water and Lava
            elif (data["name"] == "water" or
                  data["name"] == "lava"):
                new_json['action'] = ["Collecting", "Placing", "Swimming in"]

            # Beds
            elif "Bed" in data["displayName"]:
                new_json['action'] = ["Crafting", "Placing", "Sleeping on", "Breaking"]

            # Smeltable Blocks
            elif ("asdasada" in data["name"] or
                  data["name"] == "stone" or
                  data["name"] == "cobblestone" or
                  data["name"] == "sand" or
                  data["name"] == "red_sand" or
                  data["name"] == "sponge" or
                  data["name"] == "wet_sponge" or
                  data["name"] == "cactus" or
                  data["name"] == "netherrack" or
                  data["name"] == "quartz_block" or
                  data["name"] == "chiseled_quartz_block"):

                new_json['action'] = ["Placing", "Collecting", "Smelting"]

            # Craftable Blocks
            elif ("Stairs" in data["displayName"] or
                  "Bricks" in data["displayName"] or
                  "Wall" in data["displayName"] or
                  "Carpet" in data["displayName"] or
                  "sandstone" in data["name"] or
                  "Copper" in data["displayName"] or
                  data["name"] == "granite" or
                  data["name"] == "polished_granite" or
                  data["name"] == "diorite" or
                  data["name"] == "polished_diorite" or
                  data["name"] == "andesite" or
                  data["name"] == "polished_andesite" or
                  data["name"] == "coarse_dirt" or
                  data["name"] == "muddy_mangrove_roots" or
                  data["name"] == "lapis_block" or
                  data["name"] == "gold_block" or
                  data["name"] == "iron_block" or
                  data["name"] == "mossy_cobblestone" or
                  data["name"] == "diamond_block" or
                  data["name"] == "ice" or
                  data["name"] == "snow_block" or
                  data["name"] == "basalt" or
                  data["name"] == "polished_basalt" or
                  data["name"] == "glowstone" or
                  data["name"] == "packed_mud" or
                  data["name"] == "emerald_block" or
                  data["name"] == "redstone_block" or
                  data["name"] == "quartz_pillar" or
                  data["name"] == "prismarine" or
                  data["name"] == "dark_prismarine" or
                  data["name"] == "slime_block" or
                  data["name"] == "sea_lantern" or
                  data["name"] == "coal_block" or
                  data["name"] == "packed_ice" or
                  data["name"] == "end_rod" or
                  data["name"] == "purpur_block" or
                  data["name"] == "purpur_pillar" or
                  data["name"] == "dried_kelp_block" or
                  data["name"] == "conduit" or
                  data["name"] == "beehive" or
                  data["name"] == "honey_block" or
                  data["name"] == "honeycomb_block" or
                  data["name"] == "respawn_anchor" or
                  data["name"] == "lodestone" or
                  data["name"] == "blackstone" or
                  data["name"] == "polished_blackstone" or
                  data["name"] == "chiseled_polished_blackstone" or
                  data["name"] == "gilded_blackstone" or
                  data["name"] == "amethyst_block"):

                new_json['action'] = ["Placing", "Collecting", "Crafting"]

            # Craftable and Smeltable Blocks
            elif ("asdasada" in data["name"] or
                  data["name"] == "planks" or
                  data["name"] == "clay"):
                new_json['action'] = ["Placing", "Collecting", "Crafting", "Smelting"]

            # Non-craftable and non-smeltable Blocks
            elif ("Concrete" in data["displayName"] or
                  "Coral Block" in data["displayName"] or
                  "Deepslate" in data["displayName"] or
                  "Froglight" in data["displayName"] or
                  data["name"] == "grass_block" or
                  data["name"] == "dirt" or
                  data["name"] == "podzol" or
                  data["name"] == "gravel" or
                  data["name"] == "obsidian" or
                  data["name"] == "soul_sand" or
                  data["name"] == "soul_soil" or
                  data["name"] == "infested_stone" or
                  data["name"] == "infested_cobblestone" or
                  data["name"] == "infested_stone_bricks" or
                  data["name"] == "infested_mossy_stone_bricks" or
                  data["name"] == "infested_cracked_stone_bricks" or
                  data["name"] == "infested_chiseled_stone_bricks" or
                  data["name"] == "brown_mushroom_block" or
                  data["name"] == "red_mushroom_block" or
                  data["name"] == "mushroom_stem" or
                  data["name"] == "mycelium" or
                  data["name"] == "end_stone" or
                  data["name"] == "dragon_egg" or
                  data["name"] == "skeleton_skull" or
                  data["name"] == "wither_skeleton_skull" or
                  data["name"] == "zombie_head" or
                  data["name"] == "player_head" or
                  data["name"] == "creeper_head" or
                  data["name"] == "dragon_head" or
                  data["name"] == "dirt_path" or
                  data["name"] == "magma_block" or
                  data["name"] == "nether_wart_block" or
                  data["name"] == "bone_block" or
                  data["name"] == "blue_ice" or
                  data["name"] == "warped_nylium" or
                  data["name"] == "warped_wart_block" or
                  data["name"] == "crimson_nylium" or
                  data["name"] == "shroomlight" or
                  data["name"] == "ancient_debris" or
                  data["name"] == "crying_obsidian" or
                  data["name"] == "tuff" or
                  data["name"] == "calcite" or
                  data["name"] == "powder_snow" or
                  data["name"] == "sculk_sensor" or
                  data["name"] == "sculk" or
                  data["name"] == "sculk_vein" or
                  data["name"] == "sculk_catalyst" or
                  data["name"] == "sculk_shrieker" or
                  data["name"] == "dripstone_block" or
                  data["name"] == "moss_block"):

                new_json['action'] = ["Placing", "Collecting"]

            # Ores
            elif "ore" in data["name"]:
                new_json['action'] = ["Mining", "Smelting", "Collecting"]

            # Non-Interactable Tool Blocks
            elif ("Fence" in data["displayName"] or
                  "Bars" in data["displayName"] or
                  "Slab" in data["displayName"] or
                  "rail" in data["name"] or
                  data["name"] == "soul_torch" or
                  data["name"] == "torch" or
                  data["name"] == "redstone_torch" or
                  data["name"] == "ladder" or
                  data["name"] == "sticky_piston" or
                  data["name"] == "piston" or
                  data["name"] == "piston_head" or
                  data["name"] == "bookshelf" or
                  data["name"] == "redstone_wire" or
                  data["name"] == "repeater" or
                  data["name"] == "chain" or
                  data["name"] == "redstone_lamp" or
                  data["name"] == "beacon" or
                  data["name"] == "comparator" or
                  data["name"] == "daylight_detector" or
                  data["name"] == "hopper" or
                  data["name"] == "scaffolding" or
                  data["name"] == "barrel" or
                  data["name"] == "grindstone" or
                  data["name"] == "bell" or
                  data["name"] == "lantern" or
                  data["name"] == "soul_lantern" or
                  data["name"] == "campfire" or
                  data["name"] == "soul_campfire" or
                  data["name"] == "target" or
                  data["name"] == "lightning_rod" or
                  data["name"] == "jack_o_lantern"):

                new_json['action'] = ["Placing", "Collecting", "Crafting"]

            # Tool Blocks
            elif ("Sign" in data["displayName"] or
                  "Door" in data["displayName"] or
                  "Trapdoor" in data["displayName"] or
                  "Plate" in data["displayName"] or
                  "Button" in data["displayName"] or
                  "Cauldron" in data["displayName"] or
                  "Shulker Box" in data["displayName"] or
                  "Anvil" in data["displayName"] or
                  data["name"] == "dispenser" or
                  data["name"] == "note_block" or
                  data["name"] == "tnt" or
                  data["name"] == "chest" or
                  data["name"] == "crafting_table" or
                  data["name"] == "furnace" or
                  data["name"] == "lever" or
                  data["name"] == "jukebox" or
                  data["name"] == "enchanting_table" or
                  data["name"] == "brewing_stand" or
                  data["name"] == "tripwire_hook" or
                  data["name"] == "tripwire" or
                  data["name"] == "dropper" or
                  data["name"] == "loom" or
                  data["name"] == "smoker" or
                  data["name"] == "blast_furnace" or
                  data["name"] == "cartography_table" or
                  data["name"] == "fletching_table" or
                  data["name"] == "lectern" or
                  data["name"] == "smithing_table" or
                  data["name"] == "stonecutter" or
                  data["name"] == "observer" or
                  data["name"] == "composter"):

                new_json['action'] = ["Crafting", "Placing", "Collecting", "Using"]

            else:
                print(f'IGNORED - "Blocks" {key}: {data}')
                continue


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

                new_json['action'] = ["Crafting", "Using"]

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

                new_json['action'] = ["Crafting", "Enchanting", "Repairing", "Using", "Using Enhanced"]

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

                    new_json['action'] = ["Crafting", "Interacting", "Breaking", "Placing"]

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