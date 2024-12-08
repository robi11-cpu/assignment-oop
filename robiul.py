from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# List of your friends' names
friends_names = [
    "Masum", "Rakib", "Maruf", "Taslima", "Ayshi",
    "Maruf", "Rakib", "Hasan", "Abir", "Nafiz",
    "Disha", "Luna", "Sani", "Shuvo", "Darda",
    "Sadia", "Mimtanna", "Galib", "Priya", "Arshi",
    "Aronna", "Saad", "Anik", "Onthy", "Basher", "Galib"
]

# Combine names into a single string
text = " ".join(friends_names)

# Load the shape image of "ROBI"
mask = np.array(Image.open("ROBI.png"))

# Create the word cloud
wordcloud = WordCloud(
    background_color="white",  # Background color
    mask=mask,
    contour_width=1, 
    min_font_size=1,
    max_words=100000
      # Border color
).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Turn off the axes
plt.show()

# Save the word cloud as an image
wordcloud.to_file("robi_wordcloud.png")
