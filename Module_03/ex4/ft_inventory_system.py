import sys

def inventory_analysis():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Missing arguments. "
            f"Usage: python3 {sys.argv[0]} item:count item:count ...")
        else:
            args = sys.argv[1:]
            inventory = dict()

            for arg in sys.argv[1:]:
                if ":" in arg:
                    item, count = arg.split(':')
                    if not int(count) or int(count) <= 0:
                        raise ValueError(f"Count must be a positive integer. "
                        f"Usage: python3 {sys.argv[0]} item:count item:count...")
                    else:
                        inventory.update({item: int(count)})
                        
                else:
                    raise ValueError(f"Wrong input format. "
                    f"Usage: python3 {sys.argv[0]} item:count item:count...")
            
            total = sum(inventory.values())
            print("=== Inventory System Analysis ===")
            print(f"Total items in inventory: {total}")
            print(f"Unique item types: {len(inventory.keys())}")

            print("\n=== Current Inventory ===")

            max_val = max(inventory.values())
            min_val = min(inventory.values())

            while max_val >= min_val:
                for item, count in inventory.items():
                    if count == max_val:
                        percentage = (count / total) * 100
                        unit_label = "unit" if count == 1 else "units"
                        print(f"{item}: {count} {unit_label} ({percentage:.1f}%)")
                max_val -= 1
            
            print("\n=== Inventory statistics ===")

            max_val = max(inventory.values())

            most_key = max(inventory, key = inventory.get)
            print(f"Most abundant: {most_key} ({max_val})")

            least_key = min(inventory, key = inventory.get)
            print(f"Least abundant: {least_key} ({min_val})")

            print("\n=== Item Categories ===")
            moderate = {}
            scarce = {}

            for item, count in inventory.items():
                if count >= 5:
                    moderate[item] = count
                else:
                    scarce[item] = count
            print(f"Moderate: {moderate}")
            print(f"Scarce: {scarce}")
        
            print("\n=== Management Suggestions ===")
            restock = []
            for item, count in inventory.items():
                if count <= 1 or count == min_val:
                    restock.append(item)
            print(f"Restock needed: {restock}")

            print("\n=== Dictionary Properties Demo ===")
            dict_keys = []
            dict_values = []
            for item, count in inventory.items():
                dict_keys.append(item)
                dict_values.append(count)
            print(f"Dictionary keys: {dict_keys}")
            print(f"Dictionary values: {dict_values}")

            lookup = inventory.get('sword')

            if lookup is not None:
                is_in_inventory = True
            else:
                is_in_inventory = False
            print(f"Sample lookup - 'sword' in inventory: {is_in_inventory}")

    except ValueError as e:
        print(e)
    



if __name__ == "__main__":
    inventory_analysis()