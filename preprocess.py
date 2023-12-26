import re

# Function to preprocess a line of lyrics
def preprocess_lyrics(line):
    # Lowercase the text
    line = line.lower()
    
    # Remove punctuation and special characters (except for ')
    line = re.sub(r'[^a-zA-Z0-9\s\']', '', line)
    
    # Remove extra white spaces
    line = ' '.join(line.split())
    
    return line

# Define input and output file paths
input_file = "lyrics.txt"  # Replace with the path to your input file
output_file = "processed-lyrics.txt"

# Read lyrics from the input file
with open(input_file, 'r', encoding='utf-8') as file:
    lyrics = file.readlines()

# Preprocess each line of lyrics
processed_lyrics = [preprocess_lyrics(line) for line in lyrics]

# Save the processed lyrics to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(processed_lyrics))

print("Lyrics preprocessing complete. Processed lyrics saved to 'processed-lyrics.txt'.")

# Now, you can open the processed lyrics from the output_file for further processing or analysis.
