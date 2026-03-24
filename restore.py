import json

with open("d:/1.Projects/Results/BacklogReport/Backlog_Report.html", "r", encoding="utf-8") as f:
    text = f.read()

# Fix the batch size back to 5 for the API stability improvement that was done in "Fixing Backlog Report Loading" session
text = text.replace("i += 25", "i += 5")
text = text.replace("slice(i, i + 25)", "slice(i, i + 5)")
# Same for the sleep delay
text = text.replace("i + 25 < total", "i + 5 < total")
text = text.replace("setTimeout(r, 50)", "setTimeout(r, 300)")

with open("d:/1.Projects/Results/BacklogReport 1/Backlog_Report.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Restore success")
