import wikipediaapi

def scrape_wikipedia(actor_name):
    wiki = wikipediaapi.Wikipedia(language='en',user_agent="muhammadumer.bashir@students.mq.edu.au")
    page = wiki.page(actor_name)
    
    if page.exists():
        # Extract content and save to file
        content = page.text[:500]  # First 500 words
        with open('wikipedia.txt', 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Successfully scraped {actor_name}')
    else:
        print(f'Page not found for {actor_name}')

# Example usage
scrape_wikipedia('Tom Cruise')