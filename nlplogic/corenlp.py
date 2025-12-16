from textblob import TextBlob
import wikipedia

# Optional: improve search suggestions and set language
wikipedia.set_lang("en")


def summarize_wiki(name):
    print(f"Finding summary for Wikipedia page: '{name}'")
    try:
        # This returns the actual summary text as a string
        summary = wikipedia.summary(name, sentences=10)  # limit to ~10 sentences
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        print(
            f"Disambiguation page found. Possible options: {e.options[:5]}"
        )  # show first 5
        # Optionally auto-pick the best match, e.g., one containing "programming"
        for option in e.options:
            if "programming" in option.lower() or "python" in option.lower():
                print(f"Trying disambiguation option: {option}")
                return wikipedia.summary(option, sentences=10)
        print("No suitable match found in disambiguation.")
        return None
    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found for exact title: '{name}'")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def get_text_blob(text):
    if text is None:
        raise ValueError("Cannot create TextBlob from None. Summary failed.")
    return TextBlob(text)


def get_phrases(name):
    text = summarize_wiki(name)
    if text is None or not text.strip():
        print("No text retrieved. Cannot extract phrases.")
        return []

    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
