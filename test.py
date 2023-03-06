from summa.summarizer import summarize
from summa import keywords

input_text = "We have added a new feature that allows users to customize their settings. This involved updating the front-end UI to display the new options and adding new code to the backend to handle the user preferences. We have tested the feature extensively and are confident that it will be well-received by our users."

# Extract keywords from the input text
keywords = keywords.keywords(input_text)

# Summarize the input text
summary = summarize(input_text, ratio=0.4)

# Print the keywords and summary
print("Keywords:", keywords)
print("Summary:", summary)