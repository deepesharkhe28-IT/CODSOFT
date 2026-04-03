import csv

movies = []

with open("Movie recommendation/movies.csv", "r") as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        movies.append(row)

print(movies[0])  # DEBUG

user_genre = input("Enter your favorite genre: ").lower()

recommendations = []

for movie in movies:
    genre = movie.get("genre", "").lower()
    if user_genre in genre:
        recommendations.append(movie)

if recommendations:
    print("\n🔥 Recommended Movies:\n")
    for movie in recommendations:
        print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
else:
    print("No recommendations found.")