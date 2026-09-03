```python
# Candidate list
candidates = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Diana",
    5: "Null vote",
    6: "Blank vote"
}

# Initialize vote count for each candidate
votes = {candidate: 0 for candidate in candidates}


def calculate_percentages(votes, total_votes):
    """Calculate the percentage of votes for each candidate."""

    percentages = {}

    for candidate, quantity in votes.items():
        if total_votes > 0:
            percentages[candidate] = (quantity / total_votes) * 100
        else:
            percentages[candidate] = 0

    return percentages


# Voting process
while True:
    vote = int(
        input(
            "Enter the candidate number (1-6) "
            "or 0 to end the voting: "
        )
    )

    if vote == 0:
        break

    if vote in candidates:
        votes[vote] += 1
    else:
        print("Invalid candidate. Please choose a number from 1 to 6.")


# Calculate results
total_votes = sum(votes.values())
percentages = calculate_percentages(votes, total_votes)


# Display results
print("\nVoting Results:")

for candidate, quantity in votes.items():
    print(f"{candidates[candidate]}: {quantity} votes")

print(f"\nTotal votes: {total_votes}")
print(f"Null votes: {percentages[5]:.2f}%")
print(f"Blank votes: {percentages[6]:.2f}%")
```
