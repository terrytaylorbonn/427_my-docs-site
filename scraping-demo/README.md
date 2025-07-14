# Simple Runtime Scraping for LLM Enhancement

## 🎯 Purpose
This demo shows how to scrape content at runtime to enhance LLM prompts with current information, rather than relying on potentially outdated training data.

## 📁 Files Created

### 1. `simple_scraper.py`
**Basic web scraper for Docusaurus sites**
- Extracts title, headings, content, metadata
- Respects rate limits with delays
- Saves results to JSON for reuse

### 2. `llm_enhancer.py` 
**Context enhancement engine**
- Searches scraped content by keywords
- Ranks results by relevance
- Builds enhanced prompts with context

### 3. `runtime_demo.py`
**Complete integration demo**
- Shows real-time scraping + LLM workflow
- Simulates how you'd use this with actual LLM APIs
- Demonstrates different responses based on context

### 4. `requirements.txt`
**Dependencies needed**
```
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
```

## 🚀 How It Works

### Step 1: Scrape Current Content
```python
scraper = SimpleDocsScraper("https://your-site.com")
content = scraper.scrape_page(url)
```

### Step 2: Enhance User Questions
```python
enhancer = LLMContextEnhancer('scraped_content.json')
enhanced_prompt, status = enhancer.enhance_prompt(user_question)
```

### Step 3: Send to LLM
```python
# Send enhanced_prompt to OpenAI, Claude, etc.
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": enhanced_prompt}]
)
```

## 📊 Results Demonstrated

✅ **Context-Aware Responses**: Different answers based on scraped content
✅ **Current Information**: Uses live site content, not stale training data  
✅ **Scalable**: Can easily add more sources
✅ **Efficient**: Caches content to avoid repeated scraping

## 🔄 Next Steps to Expand

### Add More Sources
```python
# Scrape external documentation
external_sources = [
    "https://docusaurus.io/docs",
    "https://react.dev/learn", 
    "https://nodejs.org/docs"
]
```

### Real LLM Integration
```python
import openai

def call_real_llm(enhanced_prompt):
    return openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": enhanced_prompt}]
    )
```

### Advanced Features
- **Vector embeddings** for better content matching
- **Automatic content refresh** on schedules
- **Multi-language support** for international sites
- **Content versioning** to track changes

## 💡 Key Benefits Over Static Training Data

1. **Always Current**: Content reflects latest site updates
2. **Source Attribution**: Know exactly where info comes from  
3. **Controlled Quality**: Curate exactly what content to include
4. **Cost Effective**: No model retraining needed
5. **Privacy Friendly**: Keep sensitive docs on your own servers

## 🎯 Perfect For

- **Documentation sites** (like yours!)
- **Product information** that changes frequently
- **News/blog content** for current events
- **API documentation** with version updates
- **Company knowledge bases** with proprietary info

This approach gives you the best of both worlds: the reasoning power of LLMs with the accuracy of current, authoritative content!
