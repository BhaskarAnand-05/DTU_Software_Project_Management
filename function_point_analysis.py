a = [
    [3, 4, 6],
    [4, 5, 7],
    [3, 4, 6],
    [7, 10, 15],
    [5, 7, 10]
]

s = [
    "External Inputs",
    "External Output",
    "External Inquiries",
    "Internal Logical files",
    "External Interface Files"
]

h = ["Low", "Average", "High"]

UFP = 0

for i in range(5):
    for j in range(3):
        print(f"Enter Number of {s[i]} with {h[j]} complexity: ", end="")
        x = int(input())
        UFP += a[i][j] * x

fp = [
    "Does the system require reliable backup and recovery",
    "Is data communication required",
    "Are there distributed processing functions",
    "How is the performance",
    "Will the system run in an existing heavily utilized operational environment",
    "Does the system require on-line data entry",
    "Does the on-line data entry require the input to be built over multiple screens or operations",
    "Are the Master files updated on-line",
    "Is the inputs, outputs, files, or enquiries complex",
    "Is internal processing complex",
    "Is the code designed to be reusable",
    "Are conversion and installation included in the design",
    "Is the system designed for multiple installations in different organizations",
    "Is the system designed to facilitate change and ease of use by the user"
]

print("\nEnter")
print("0 for No influence")
print("1 for Incidental")
print("2 for Moderate")
print("3 for Average")
print("4 for Significant")
print("5 for Essential")
print()

F = 0

for i in range(14):
    print()
    print(fp[i])
    x = int(input())
    F += x

CAF = (F * 0.01 + 0.65)
FP = CAF * UFP

print("Statistics:")
print("Unadjusted Function Point =", UFP)
print("Complexity Adjustment Factor =", CAF)
print("Function Points =", FP)
