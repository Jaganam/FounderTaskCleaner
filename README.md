***Founder Task Cleaner*** is a python script that was created to help startup operators and founders clean up messy, unorganized task lists. It streamlines tasks to reduce clutter, categorizes them, and produces a clarified task list.

**Inspiration**

As someone without a deep technical background, I built this to push myself outside my comfort zone and solve a real problem I’ve seen repeatedly in early-stage startups: founders having to juggle chaotic, unstructured to-do lists. 
This tool reflects how I think about leverage, not by building something overly flashy, but by reducing friction and helping teams move faster. It’s simple by design, and useful by intent.

**How it Works**

In the file labelled "sample_tasks.txt", the user can add or edit tasks, then run the program using python task_cleaner.py. 
The program will output a file labelled "cleaned_tasks.md", which will contain the organized version of the user's task list.

If the input looks like this (the current sample):

Call with Sam
Send email to Samir
call with Sam
Organize Airtable
Email investor update
send email to samir
Review product feedback
Organize Airtable tags

The output will look like this:

Fundraising
- Call with Sam
- Send email to Samir


Ops
- Organize Airtable
- Organize Airtable tags

Product
- Review product feedback

Other

Startup environments can get messy. Going from the ground up is not an easy task by any measure. This tool turns chaos into clarity with one script, giving founders a quick way to focus on what matters most.

Mahamadou Jagana

Update Notes
v1.1

This version of Founder Task Cleaner expands on the original script by adding logic to help founders not only clean and organize their task lists, but also prioritize them. I originally sought to make a standalone script that prioritizes lists, but figured it could only make my preexisting script better. The tool now supports triage-style sorting to better reflect how early-stage founders may think and operate.

What's New:

*Task Triage Buckets*
Tasks are now categorized into three actionable groups:
- 🔴 Must Act
- 🟡 Delegate
- 🟣 Track Later

*Keyword-Based Sorting*
Tasks are routed into categories using simple keyword logic that reflects typical startup workflows

*Improved Output Format*
The output file is now grouped by action category, making it easier to scan and execute

*Expanded Purpose*
The tool has shifted from basic organization to a lightweight decision-support mimic assistant designed to help founders focus on what matters most and protect their time

This update is built on the same intent as the original version, and reflects how I approach operational leverage in messy, fast-moving environments.

Mahamadou Jagana
