"""
Runtime Integration Demo
Purpose: Show how to integrate runtime scraping with LLM calls
"""

from llm_enhancer import LLMContextEnhancer
from simple_scraper import SimpleDocsScraper
import json
import time

class RuntimeScrapingLLM:
    def __init__(self, base_url, content_cache_file='scraped_content.json'):
        """Initialize with scraper and content enhancer"""
        self.base_url = base_url
        self.scraper = SimpleDocsScraper(base_url)
        self.enhancer = LLMContextEnhancer(content_cache_file)
        self.cache_file = content_cache_file
    
    def scrape_fresh_content(self, url):
        """Scrape fresh content from a specific URL"""
        print(f"🔄 Scraping fresh content from: {url}")
        content = self.scraper.scrape_page(url)
        
        if content:
            # Update our content database
            self.enhancer.content_db[url] = content
            
            # Save updated content to cache
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.enhancer.content_db, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Fresh content added for: {content['title']}")
            return True
        return False
    
    def answer_with_context(self, user_question, check_fresh_content=False):
        """Answer user question with enhanced context"""
        print(f"\n❓ User Question: {user_question}")
        print("=" * 60)
        
        # Optional: Scrape fresh content if needed
        if check_fresh_content:
            print("🔄 Checking for fresh content...")
            # In a real implementation, you'd determine which URLs to refresh
            # For demo, we'll just note this capability
            print("ℹ️  (In production: would check specific URLs for updates)")
        
        # Get enhanced prompt with current content
        enhanced_prompt, status = self.enhancer.enhance_prompt(user_question)
        print(f"📊 Context Status: {status}")
        
        # Simulate LLM call (in reality you'd call OpenAI, Claude, etc.)
        simulated_answer = self._simulate_llm_call(enhanced_prompt)
        
        print(f"\n🤖 LLM Response:")
        print(simulated_answer)
        print("=" * 60)
        
        return simulated_answer
    
    def _simulate_llm_call(self, enhanced_prompt):
        """Simulate what an LLM would respond with the enhanced prompt"""
        
        # Extract user question from enhanced prompt
        user_question = ""
        if "USER QUESTION:" in enhanced_prompt:
            user_question = enhanced_prompt.split("USER QUESTION:")[1].strip().lower()
        
        print(f"🔍 Analyzing question: '{user_question[:50]}...'")
        
        if "create" in user_question and "document" in user_question:
            return """Based on the documentation provided, here's how to create a document:

1. **Create a Markdown file**: Create a new .md file in the `docs/` directory
2. **Add content**: Write your content using Markdown syntax
3. **Configure sidebar**: Add metadata to customize the sidebar label and position
4. **Automatic integration**: Docusaurus automatically creates a sidebar from the docs folder

Example from your documentation:
```markdown
docs/hello.md
---
sidebar_label: 'Hi!'
sidebar_position: 3
---
# Hello
This is my **first Docusaurus document**!
```

The document will be automatically available in your site navigation."""

        elif "docusaurus" in user_question or "what is" in user_question:
            return """Based on your site documentation, Docusaurus is a modern static site generator that:

• **Easy to Use**: Designed to be easily installed and used to get websites running quickly
• **Focus on Content**: Lets you focus on your docs while handling the technical aspects
• **React-Powered**: Built with React, allowing you to extend or customize your website layout
• **Documentation-Focused**: Specifically designed for creating documentation sites

From your intro page, you can get started by creating a new site and it takes less than 5 minutes to discover Docusaurus basics."""

        elif "get started" in user_question or "new here" in user_question:
            return """Based on your documentation, here's how to get started:

**Prerequisites:**
• Node.js version 18.0 or above

**Quick Start:**
1. Generate a new site: `npm init docusaurus@latest my-website classic`
2. Navigate to your site: `cd my-website`
3. Start development server: `npm run start`
4. Open http://localhost:3000/ to view your site

The documentation mentions you can also try Docusaurus immediately with docusaurus.new for a quick preview."""

        else:
            return """I can help answer questions about your Docusaurus site. Based on the current documentation I have access to, I can provide information about:

• Creating documents and pages
• Getting started with Docusaurus
• Site configuration and setup
• Documentation best practices

Please ask a more specific question about any of these topics."""

def demo_runtime_integration():
    """Demo the complete runtime integration"""
    print("🚀 Runtime Scraping + LLM Integration Demo")
    print("=" * 60)
    
    # Initialize runtime system
    runtime_llm = RuntimeScrapingLLM("https://four27-my-docs-site.onrender.com")
    
    # Demo questions that would benefit from current content
    demo_questions = [
        "How do I create a new document in this system?",
        "What is Docusaurus and why should I use it?", 
        "I'm new here, how do I get started?",
        "How do I customize the sidebar?"
    ]
    
    for question in demo_questions:
        runtime_llm.answer_with_context(question)
        time.sleep(1)  # Pause between questions for readability
    
    print("\n✨ Demo Complete!")
    print("\n💡 Key Benefits Demonstrated:")
    print("   • Real-time content enhancement")
    print("   • Context-aware responses")
    print("   • Current documentation integration")
    print("   • Scalable to any number of sources")

if __name__ == "__main__":
    demo_runtime_integration()
