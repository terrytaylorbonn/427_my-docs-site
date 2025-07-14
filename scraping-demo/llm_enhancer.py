"""
LLM Context Enhancement using Scraped Content
Purpose: Use scraped content to provide current context to LLM prompts
"""

import json
from simple_scraper import SimpleDocsScraper

class LLMContextEnhancer:
    def __init__(self, scraped_content_file=None):
        """Initialize with optional pre-scraped content"""
        self.content_db = {}
        if scraped_content_file:
            self.load_scraped_content(scraped_content_file)
    
    def load_scraped_content(self, file_path):
        """Load previously scraped content from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.content_db = json.load(f)
            print(f"✅ Loaded {len(self.content_db)} pages from {file_path}")
        except Exception as e:
            print(f"❌ Error loading content: {e}")
    
    def search_content(self, query_keywords):
        """Simple keyword search in scraped content"""
        relevant_content = []
        query_lower = query_keywords.lower()
        
        for url, content in self.content_db.items():
            relevance_score = 0
            matched_sections = []
            
            # Check title
            if any(keyword in content['title'].lower() for keyword in query_lower.split()):
                relevance_score += 3
                matched_sections.append("title")
            
            # Check headings
            for heading in content['headings']:
                if any(keyword in heading['text'].lower() for keyword in query_lower.split()):
                    relevance_score += 2
                    matched_sections.append(f"heading: {heading['text']}")
            
            # Check main content
            if any(keyword in content['content'].lower() for keyword in query_lower.split()):
                relevance_score += 1
                matched_sections.append("content")
            
            if relevance_score > 0:
                relevant_content.append({
                    'url': url,
                    'title': content['title'],
                    'relevance_score': relevance_score,
                    'matched_sections': matched_sections,
                    'content_snippet': self._extract_snippet(content['content'], query_keywords)
                })
        
        # Sort by relevance
        relevant_content.sort(key=lambda x: x['relevance_score'], reverse=True)
        return relevant_content
    
    def _extract_snippet(self, content, query_keywords, snippet_length=200):
        """Extract relevant snippet around query keywords"""
        query_lower = query_keywords.lower()
        content_lower = content.lower()
        
        # Find first occurrence of any keyword
        for keyword in query_lower.split():
            pos = content_lower.find(keyword)
            if pos != -1:
                # Extract snippet around the keyword
                start = max(0, pos - snippet_length // 2)
                end = min(len(content), pos + snippet_length // 2)
                snippet = content[start:end]
                
                # Clean up snippet
                if start > 0:
                    snippet = "..." + snippet
                if end < len(content):
                    snippet = snippet + "..."
                
                return snippet
        
        # If no keywords found, return beginning of content
        return content[:snippet_length] + "..." if len(content) > snippet_length else content
    
    def enhance_prompt(self, user_question, max_context_items=3):
        """Enhance a user question with relevant scraped content"""
        
        # Search for relevant content
        relevant_content = self.search_content(user_question)
        
        if not relevant_content:
            return user_question, "No relevant documentation found."
        
        # Build context from top matches
        context_parts = []
        for i, item in enumerate(relevant_content[:max_context_items]):
            context_parts.append(f"""
Source {i+1}: {item['title']}
URL: {item['url']}
Content: {item['content_snippet']}
""")
        
        context = "\n".join(context_parts)
        
        # Enhanced prompt
        enhanced_prompt = f"""
CONTEXT FROM DOCUMENTATION:
{context}

USER QUESTION: {user_question}

Please answer the user's question using the provided documentation context when relevant. 
If the context doesn't contain relevant information, mention that and provide general guidance.
"""
        
        return enhanced_prompt, f"Found {len(relevant_content)} relevant sections"

def demo_context_enhancement():
    """Demo the context enhancement functionality"""
    print("🚀 Demo: LLM Context Enhancement\n")
    
    # Initialize enhancer with our scraped content
    enhancer = LLMContextEnhancer('scraped_content.json')
    
    # Test questions
    test_questions = [
        "How do I create a new document?",
        "What is Docusaurus?",
        "How do I get started with this site?",
        "Tell me about React components"  # This should find limited info
    ]
    
    for question in test_questions:
        print(f"❓ Question: {question}")
        enhanced_prompt, status = enhancer.enhance_prompt(question)
        print(f"📊 Status: {status}")
        print("🔍 Enhanced Prompt Preview:")
        print(enhanced_prompt[:300] + "..." if len(enhanced_prompt) > 300 else enhanced_prompt)
        print("-" * 80)

if __name__ == "__main__":
    demo_context_enhancement()
