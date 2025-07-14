import requests
from bs4 import BeautifulSoup
import json

def scrape_page(url):
    """Extract title and content from a webpage"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('title').text.strip()
    main = soup.find('main') or soup.find('article')
    content = main.get_text().strip() if main else "No content"
    
    return {'title': title, 'content': content}

def search_content(data, query):
    """Find pages matching query keywords"""
    results = []
    for url, page in data.items():
        if any(word.lower() in page['content'].lower() for word in query.split()):
            results.append({'url': url, 'title': page['title'], 
                          'snippet': page['content'][:150] + "..."})
    return results

def enhance_prompt(query, scraped_data):
    """Add scraped content to user query for LLM"""
    matches = search_content(scraped_data, query)
    if not matches:
        return f"Question: {query}\nNo relevant docs found."
    
    context = "Relevant docs:\n"
    for i, match in enumerate(matches[:2], 1):
        context += f"{i}. {match['title']}: {match['snippet']}\n"
    
    return f"{context}\nQuestion: {query}\nAnswer using the docs above."

if __name__ == "__main__":
    # Demo
    base_url = "https://four27-my-docs-site.onrender.com"
    urls = [f"{base_url}/", f"{base_url}/intro"]
    
    print("1. Scraping pages...")
    data = {}
    for url in urls:
        print(f"   - {url}")
        data[url] = scrape_page(url)
    
    print("2. Testing search...")
    query = "create document"
    matches = search_content(data, query)
    print(f"   Found {len(matches)} matches for '{query}'")
    
    print("3. Enhancing prompt...")
    enhanced = enhance_prompt(query, data)
    print(f"   Enhanced prompt length: {len(enhanced)} chars")
    
    print("4. Demo complete!")
    print("\nEnhanced prompt:")
    print(enhanced)
    
    
