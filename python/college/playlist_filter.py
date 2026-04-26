# Problem 5: Filter songs by artist name suffix
n = int(input())
songs = input().split()
suffix = input().lower()
matches = [song for song in songs if song.split('-')[1].lower().endswith(suffix)]
if matches:
    print(' '.join(matches))
else:
    print("No matches")
print(len(matches))
if matches:
    shortest_title = min((song.split('-')[0] for song in matches), key=len)
    print(shortest_title)
else:
    print("-")