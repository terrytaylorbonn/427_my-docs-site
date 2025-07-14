import requests
from bs4 import BeautifulSoup
import openai
import os

def scrape_paragraphs(url):
    """Extract paragraph text from a webpage"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    paragraphs = []
    for p in soup.find_all('p'):
        text = p.get_text().strip()
        if text:
            paragraphs.append(text)
    
    return paragraphs

def find_froquetism_text(paragraphs):
    """Find paragraphs containing 'froquetism'"""
    froquetism_text = []
    for p in paragraphs:
        if 'froquetism' in p.lower():
            froquetism_text.append(p)
    return froquetism_text

def ask_openai_about_froquetism(text_list, source_urls):
    """Send froquetism text to OpenAI for summary"""
    if not text_list:
        return "No froquetism text found."
    
    # Combine all froquetism text
    combined_text = " ".join(text_list)
    
    # Combine URLs for prompt
    urls_text = ", ".join(source_urls)
    
    # Create prompt with source URLs
    prompt = f'Create a 1-sentence summary of what a "froquetism" is based on the following text from {urls_text}: \n\n{combined_text}'
    
    # Call OpenAI
    client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    
    return response.choices[0].message.content

def main():
    """Demo: Find froquetism text and get OpenAI summary"""
    print("=== Froquetism Finder Demo ===")
    
    # Step 1: Scrape paragraphs
    print("1. Scraping paragraphs...")
    base_url = "https://four27-my-docs-site.onrender.com"
    urls = [f"{base_url}/intro", f"{base_url}/tutorial-basics/create-a-document"]
    
    all_paragraphs = []
    for url in urls:
        print(f"   - {url}")
        paragraphs = scrape_paragraphs(url)
        all_paragraphs.extend(paragraphs)
    
    print(f"   Found {len(all_paragraphs)} total paragraphs")
    
    # Step 2: Find froquetism text
    print("2. Searching for 'froquetism'...")
    froquetism_text = find_froquetism_text(all_paragraphs)
    print(f"   Found {len(froquetism_text)} paragraphs with 'froquetism'")
    
    if froquetism_text:
        print("   Froquetism text found:")
        for i, text in enumerate(froquetism_text, 1):
#            print(f"   {i}. {text[:100]}...")  # TT MOD
            print(f"   {i}. {text}") ## TT MOD
    
    # Step 3: Ask OpenAI
    print("3. Asking OpenAI for summary...")
    if not os.getenv('OPENAI_API_KEY'):
        print("   ❌ OPENAI_API_KEY not found in environment")
        return
    
    try:
        summary = ask_openai_about_froquetism(froquetism_text, urls)
        print(f"   ✅ OpenAI Summary: {summary}")
    except Exception as e:
        print(f"   ❌ OpenAI error: {e}")
    
    print("4. Demo complete!")

if __name__ == "__main__":
    main()
