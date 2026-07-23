movies = {
    "Action": ["Avengers", "John Wick", "Batman"],
    "Comedy": ["3 Idiots", "Jathi Ratnalu", "Dhamaal"],
    "Horror": ["The Conjuring", "Annabelle", "Insidious"],
    "Romance": ["Titanic", "Sita Ramam", "Hi Nanna"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print("🎬 Movie Recommendation System")
print("\nAvailable Genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ").title()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("⭐", movie)
else:
    print("\nSorry! Genre not found.")