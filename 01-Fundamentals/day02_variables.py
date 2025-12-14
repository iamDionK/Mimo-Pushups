# Day 2: Variables & Data Types
# Goal: Store data in containers and use f-strings for clean output.

# --- DATA INPUT ---
# Strings (Text)
candidate_name = "Future Dev"
target_role = "AI Architect"
focus_area = "Web3 & Automation"

# Integers (Whole Numbers)
day_count = 2
total_days = 100
coffee_cups = 3

# --- LOGIC / OUTPUT ---
# Using an f-string (formatted string) to inject variables directly into text.
# The 'f' before the quotes tells Python to replace {variable} with its value.

print(f"--- DAILY LOG: Day {day_count} of {total_days} ---")
print(f"User: {candidate_name}")
print(f"Current Mission: Pivot to {target_role} specializing in {focus_area}.")

# Simple math with variables
remaining = total_days - day_count
print(f"Days remaining until launch: {remaining}")
print(f"Fuel_level:{coffee_cups} cups"
