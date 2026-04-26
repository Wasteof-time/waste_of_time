# Problem 6: Autocomplete author names by suffix
n = int(input())
authors = input().split()
suffix = input().lower()
matches = [author for author in authors if author.lower().endswith(suffix)]
if matches:
    print(' '.join(matches))
else:
    print("No suggestions")
print(len(matches))
if matches:
    longest_author = max(matches, key=len)
    print(longest_author)
else:
    print("-")