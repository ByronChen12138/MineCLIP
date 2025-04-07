import minecraft_data

from utils.json_utils import write_json, append_jsonl


def get_obj_names(objects, obj_type, out_path="../outs/"):
    for key, data in objects.items():
        # If the data have a 'displayName' key, set it to the value of 'name'
        new_json = {}

        try:
            if "displayName" in data:
                new_json['name'] = data["displayName"]

            elif 'name' in data:
                new_json['name'] = data["name"]

            else:
                print (f"Key {key} does not have a 'name' or 'displayName' key: {data}")
                continue

        except Exception as e:
            print(f"Error processing {key}: {e}")
            continue

        if obj_type == "blocks":
            new_json['action'] = ["Mining", "Placing", "Crafting", "Smelting"]

        elif obj_type == "items":
            pass

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
                    print(f"Immobile for {key}: {category}")
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
                    print(f"Unknown for {key}: {category}")
                    continue

            else:
                print (f"Un-categorized for {key}: {category}")
                continue


        else:
            print(f"Unknown object type: {obj_type}")
            continue

        append_jsonl(f'{out_path}{obj_type}_name.jsonl', [new_json])


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

    # new_instruments = {}

    # for key, value in instruments.items():
    #     new_instruments[value.get('name')] = value

    # get_obj_names(blocks, "blocks")
    # get_obj_names(items, "items")
    # get_obj_names(new_instruments, "instruments")
    # get_obj_names(materials, "materials")
    get_obj_names(entities, "entities")

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