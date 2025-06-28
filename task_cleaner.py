with open("sample_tasks.txt", "r") as file:
    tasks = file.readlines()

cleaned = set(task.strip().lower() for task in tasks if task.strip())

triaged = {"Must Act": [], "Delegate": [], "Track Later": []}

for task in cleaned:
    if any(keyword in task for keyword in ["email", "call", "update", "build", "follow up", "revisit"]):
        triaged["Must Act"].append(task)
    elif any(keyword in task for keyword in ["ask", "ping", "check with", "send to", "send"]):
        triaged["Delegate"].append(task)
    elif any(keyword in task for keyword in ["explore", "maybe", "idea"]):
        triaged["Track Later"].append(task)
    else:
        triaged["Must Act"].append(task)  # default bucket

with open("cleaned_tasks.md", "w") as out:
    out.write("# Task Triage – Chaos to Clarity (v1)\n\n")
    
    for category, tasks in triaged.items():
        icon = {
            "Must Act": "🔴",
            "Delegate": "🟡",
            "Track Later": "🟣"
        }[category]
        
        out.write(f"## {icon} {category}\n\n")
        for t in tasks:
            out.write(f"- {t.capitalize()}\n")
        out.write("\n")

print("✅ Task triage complete. See cleaned_tasks.md!")

