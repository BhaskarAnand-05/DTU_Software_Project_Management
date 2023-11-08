print("Enter the number of screens:")
screens = float(input())
print("Enter the number of reports:")
reports = float(input())
print("Enter the number of 3GL components:")
gl_components = float(input())

print("Enter the number of view contains of screen:")
view_contains = float(input())
print("Enter the number of data tables in screen:")
data_tables_s = float(input())
print("Enter the number of sections in reports:")
sections = float(input())
print("Enter the number of data tables in reports:")
data_tables_r = float(input())

complexity_s = 0
complexity_r = 0

if view_contains < 3:
    if data_tables_s < 4:
        complexity_s = 1
    elif 4 <= data_tables_s < 8:
        complexity_s = 1
    else:
        complexity_s = 2
elif 3 <= view_contains < 8:
    if data_tables_s < 4:
        complexity_s = 1
    elif 4 <= data_tables_s < 8:
        complexity_s = 2
    else:
        complexity_s = 3
else:
    if data_tables_s < 4:
        complexity_s = 2
    elif 4 <= data_tables_s < 8:
        complexity_s = 3
    else:
        complexity_s = 3

if sections <= 1:
    if data_tables_r < 4:
        complexity_r = 2
    elif 4 <= data_tables_r < 8:
        complexity_r = 2
    else:
        complexity_r = 5
elif 2 <= sections <= 3:
    if data_tables_r < 4:
        complexity_r = 2
    elif 4 <= data_tables_r < 8:
        complexity_r = 5
    else:
        complexity_r = 8
else:
    if data_tables_r < 4:
        complexity_r = 5
    elif 4 <= data_tables_r < 8:
        complexity_r = 8
    else:
        complexity_r = 8

object_point = screens * complexity_s + reports * complexity_r + gl_components * 10
print("Object point value is:", object_point)

print("Enter the percentage reuse value:")
reuse = float(input())
NOP = (object_point * (100 - reuse)) / 100
print("New object point value is:", NOP)

print("Enter the value of productivity rate:")
print("Very Low: 4")
print("Low: 7")
print("Nominal: 13")
print("High: 25")
print("Very High: 50")
prod = float(input())

effort = NOP / prod
print("Effort required is:", effort)
