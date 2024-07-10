import random

def get_valid_input(prompt):
    """Prompt the user for input and validate that it's not empty."""
    while True:
        response = input(prompt).strip()
        if response:
            return response
        else:
            print("Input cannot be empty. Please try again.")

def generate_descriptive_band_name(city, pet):
    """Generate a band name using descriptive elements and user inputs."""
    adjectives = ["Mighty", "Rocking", "Electric", "Mystic", "Groovy", "Funky", "Cosmic", "Wild", "Silent", "Thunderous", "Velvet"]
    nouns = ["Vibes", "Echoes", "Beats", "Rhythms", "Notes", "Tunes", "Harmonies", "Melodies", "Symphony", "Chords"]
    descriptors = ["The", "The Great", "The Amazing", "The Fantastic", "The Incredible", "The Legendary"]
    suffixes = ["Band", "Crew", "Ensemble", "Tribe", "Collective", "Squad", "Gang", "Project", "Orchestra"]

    band_name_formats = [
        f"{random.choice(descriptors)} {city} {pet}",
        f"{pet} {random.choice(suffixes)}",
        f"{city} {random.choice(suffixes)}",
        f"{random.choice(adjectives)} {pet} of {city}",
        f"{random.choice(adjectives)} {city} {random.choice(nouns)}",
        f"{random.choice(descriptors)} {pet}",
        f"{city} {random.choice(nouns)}",
        f"{random.choice(adjectives)} {pet} {random.choice(suffixes)}",
        f"{random.choice(descriptors)} {random.choice(adjectives)} {pet}",
        f"{random.choice(adjectives)} {city} {pet}"
    ]
    
    return random.choice(band_name_formats)

def main():
    """Main function to run the Band Name Generator."""
    print("Welcome to the Band Name Generator.")
    
    # Get user inputs with validation
    city = get_valid_input("What's the name of the city you grew up in?\n")
    pet = get_valid_input("What's your pet's name?\n")
    
    # Generate and display a band name
    band_name = generate_descriptive_band_name(city, pet)
    print(f"Your band name could be '{band_name}'.")

# Run the main function to start the Band Name Generator
if __name__ == "__main__":
    main()
