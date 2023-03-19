# Define the dictionary of candidates and their job fit scores
candidates = {
    "John Doe": 10,
    "Jane Smith": 5,
    "Bob Johnson": 8,
    "Sara Davis": 9,
    "Tom Wilson": 6
}

# Sort the dictionary by values (job fit scores) in descending order
sorted_candidates = sorted(
    candidates.items(), key=lambda x: x[1], reverse=True)

# Display the sorted candidates to the recruiter
print("Candidate\tJob Fit Score")
print("-------------------------")
for candidate in sorted_candidates:
    print(f"{candidate[0]}\t\t{candidate[1]}")
