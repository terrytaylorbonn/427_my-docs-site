"""
Simple Docusaurus Site Scraper
Purpose: Extract content to enhance LLM prompts at runtime
"""

import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import time

class SimpleDocsScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.scraped_content = {}
    
    def scrape_page(self, url):
        """Scrape a single page and extract key content"""
        try:
            print(f"Scraping: {url}")
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract key content from Docusaurus page
            content = {
                'url': url,
                'title': self._extract_title(soup),
                'headings': self._extract_headings(soup),
                'content': self._extract_main_content(soup),
                'metadata': self._extract_metadata(soup)
            }
            
            return content
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None
    
    def _extract_title(self, soup):
        """Extract page title"""
        title_tag = soup.find('title')
        return title_tag.text.strip() if title_tag else "No title"
    
    def _extract_headings(self, soup):
        """Extract all headings (h1-h6)"""
        headings = []
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            headings.append({
                'level': heading.name,
                'text': heading.get_text().strip()
            })
        return headings
    
    def _extract_main_content(self, soup):
        """Extract main content text"""
        # Docusaurus typically puts content in main tag or article
        main_content = soup.find('main') or soup.find('article')
        if main_content:
            # Remove navigation and other noise
            for nav in main_content.find_all(['nav', 'aside', 'footer']):
                nav.decompose()
            return main_content.get_text().strip()
        return "No main content found"
    
    def _extract_metadata(self, soup):
        """Extract useful metadata"""
        metadata = {}
        
        # Description
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag:
            metadata['description'] = desc_tag.get('content', '')
        
        # Keywords
        keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
        if keywords_tag:
            metadata['keywords'] = keywords_tag.get('content', '')
        
        return metadata

def test_simple_scraping():
    """Test scraping your Docusaurus site"""
    base_url = "https://four27-my-docs-site.onrender.com"
    scraper = SimpleDocsScraper(base_url)
    
    # Test pages to scrape
    test_pages = [
        f"{base_url}/",  # Homepage
        f"{base_url}/intro",  # Introduction
        f"{base_url}/tutorial-basics/create-a-document"  # Tutorial page
    ]
    
    results = {}
    
    for url in test_pages:
        content = scraper.scrape_page(url)
        if content:
            results[url] = content
            print(f"✅ Successfully scraped: {content['title']}")
        else:
            print(f"❌ Failed to scrape: {url}")
        
        # Be polite - don't hammer the server
        time.sleep(1)
    
    # Save results for inspection
    with open('scraped_content.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n🎉 Scraped {len(results)} pages")
    print("📄 Content saved to 'scraped_content.json'")
    return results

if __name__ == "__main__":
    # Run the test
    scraped_data = test_simple_scraping()
    
    # Show a sample of what we extracted
    if scraped_data:
        first_page = list(scraped_data.values())[0]
        print("\n📋 Sample extracted content:")
        print(f"Title: {first_page['title']}")
        print(f"Headings: {len(first_page['headings'])} found")
        print(f"Content length: {len(first_page['content'])} characters")
