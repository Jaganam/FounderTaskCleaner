with open("sample_tasks.txt", "r") as file:
    tasks = file.readlines()

cleaned = set(task.strip().lower() for task in tasks if task.strip())

categorized = {"Ops": [], "Fundraising": [], "Product": [], "Other": []}

for task in cleaned:
    if "email" in task or "call" in task:
        categorized["Fundraising"].append(task)
    elif "organize" in task or "airtable" in task:
        categorized["Ops"].append(task)
    elif "product" in task:
        categorized["Product"].append(task)
    else:
        categorized["Other"].append(task)

with open("cleaned_tasks.md", "w") as out:
    for category, tasks in categorized.items():
        out.write(f"## {category}\n")
        for t in tasks:
            out.write(f"- {t.capitalize()}\n")
        out.write("\n")

print("✅ Tasks cleaned and saved to cleaned_tasks.md")
