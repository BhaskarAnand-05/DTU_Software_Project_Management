print("Enter effort in Person-Year: ")
Effort = float(input())
print()

# Change effort to person-months
Effort = Effort * 12

LOC_SEL = 0
LOC_WF = 0

LOC_SEL = round((Effort / 1.4) ** (1 / 0.93) * 1000)
LOC_WF = round((Effort / 5.2) ** (1 / 0.91) * 1000)

print("LOC_SEL:", LOC_SEL, "LOC")
print("LOC_WF:", LOC_WF, "LOC")
print()

Duration_SEL = round(4.6 * (LOC_SEL / 1000) ** 0.26)
Duration_WF = round(4.1 * (LOC_WF / 1000) ** 0.36)

print("Duration_SEL:", Duration_SEL, "months")
print("Duration_WF:", Duration_WF, "months")
print()

Productivity_SEL = LOC_SEL / (Effort / 12)
Productivity_WF = LOC_WF / (Effort / 12)

print("Productivity_SEL:", Productivity_SEL, "LOC / Person-Years")
print("Productivity_WF:", Productivity_WF, "LOC / Person-Years")
print()
