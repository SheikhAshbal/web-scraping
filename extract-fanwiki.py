import fandom

# Set the wiki to the Jojo fandom wiki
fandom.set_wiki("Jojo")

def scrape_fandom(character_name):
    # Search for the character to get the exact page title
    search_results = fandom.search(character_name)
    
    if search_results:
        # Print search results to debug
        print("Search Results:")
        for result in search_results:
            # Assuming the title is the first element of the tuple
            print(f"- {result[0]}")  # Access the title using result[0]

        # Get the first search result (assuming the first is the best match)
        character = search_results[0][0]  # Access the title of the first result
        print(f"Attempting to access page for: {character}")
        
        try:
            # Fetch the character's page details
            details = fandom.page(character)
            
            # Check if content is a dict and convert it to string if necessary
            content = details.content if isinstance(details.content, str) else str(details.content)
            
            # Save the page content to a file
            with open("fanwiki.txt", "w", encoding='utf-8') as file:
                file.write(content)  # Write the content string to the file
            
            print(f"Data for {character_name} saved to fanwiki.txt")
        except Exception as e:
            print(f"Error accessing page: {e}")
    else:
        print(f"Character {character_name} not found on Jojo wiki!")


scrape_fandom('Hol Horse')
