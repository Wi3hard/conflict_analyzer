import json

def load_conflicts():
    with open("conflicts.json") as f:
        return json.load(f)

def analyze(conflict_name):
    db = load_conflicts()
    conflict = db.get(conflict_name)
    if conflict:
        print(f"\nConflict: {conflict_name}")
        for key, val in conflict.items():
            print(f"{key.title()}: {', '.join(val) if isinstance(val, list) else val}")
    else:
        print("Conflict not found.")

if __name__ == "__main__":
    name = input("Enter conflict name: ")
    analyze(name)
