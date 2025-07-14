from mini_scraper import enhance_prompt, scrape_page

def simulate_llm_call(enhanced_prompt):
    """Simulate LLM response to enhanced prompt"""
    if "create document" in enhanced_prompt.lower():
        return "Based on the docs: Create a .md file in docs/ folder, add content, configure sidebar."
    elif "docusaurus" in enhanced_prompt.lower():
        return "Based on the docs: Docusaurus is easy to use, focuses on content, powered by React."
    else:
        return "I can help with documentation questions. Please be more specific."

def demo_llm_integration():
    """Demo complete scraping + LLM workflow"""
    print("=== Runtime Scraping + LLM Demo ===")
    
    # Step 1: Scrape content
    print("1. Scraping documentation...")
    base_url = "https://four27-my-docs-site.onrender.com"
    data = {
        f"{base_url}/": scrape_page(f"{base_url}/"),
        f"{base_url}/intro": scrape_page(f"{base_url}/intro")
    }
    print(f"   Scraped {len(data)} pages")
    
    # Step 2: Test queries
    queries = ["How to create document?", "What is Docusaurus?"]
    
    for i, query in enumerate(queries, 3):
        print(f"{i-1}. Processing: '{query}'")
        
        # Step 3: Enhance with context
        enhanced = enhance_prompt(query, data)
        print(f"   Enhanced prompt: {len(enhanced)} chars")
        
        # Step 4: Simulate LLM
        answer = simulate_llm_call(enhanced)
        print(f"   LLM Response: {answer}")
        print()
    
    print("4. Demo complete!")

if __name__ == "__main__":
    demo_llm_integration()
