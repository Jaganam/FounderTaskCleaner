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
- Call with sam
- Send email to samir

Ops
- Organize airtable
- Organize airtable tags

Product
- Review product feedback

Other

Startup environments can get messy. Going from the ground up is not an easy task by any measure. This tool turns chaos into clarity with one script, giving founders a quick way to focus on what matters most.
