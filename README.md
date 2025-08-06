GEMMA Textbook Generator — Technical Writeup
============================================
### Public Demo Note

Due to platform limitations, the public version of this project uses a **mocked chapter generator** instead of the actual Ollama-based Gemma model. This allows the demo to run on environments like Streamlit Cloud or Kaggle, which do not support local model runners or custom servers.

In the real pipeline, chapter generation is handled by **Ollama running locally**, using the Gemma 2B model. The mock function simply returns placeholder text for each topic to demonstrate the structure and flow of the system.

Here’s the mock function used in the public version:

```python
def generate_chapter(topic):
    return f"### Chapter: {topic}\n\nThis is a placeholder summary for demo purposes."
Overview
--------
This project generates an entire textbook from the topics listed in a syllabus. 
It matters because in many places, students struggle to access textbooks — not because 
they don’t want to learn, but because the books simply don’t exist. There are no writers 
for certain niche or local subjects, and students are forced to pass the semester somehow, 
often with poor results.

I’m one of those students. I’ve had to go through semesters without proper textbooks, 
relying on scattered notes and incomplete materials. This project is my way of solving 
that problem using AI.

Architecture
------------
Folder Structure:
GEMMA_TEXTBOOK_GENERATOR/
├── core/
│   ├── gemma_prompting.py
│   ├── generate_textbook.py
│   ├── generator.py
│   └── ingest.py
├── utils/
│   ├── io.py
│   └── syllabus_loader.py
├── data/
│   ├── syllabus.txt
│   └── cache/
├── models/
├── cache/
└── server.py

Pipeline Flow:
1. Load syllabus from `syllabus.txt`
2. Parse topics and validate them
3. Generate chapters using Gemma via Ollama
4. Save chapters individually
5. Compile final textbook into a single `.txt` file

Key Modules:
- `core/generator.py`: Handles chapter generation
- `core/gemma_prompting.py`: Builds structured prompts
- `utils/io.py`: Manages file I/O and sanitization
- `generate_textbook.py`: Orchestrates the full pipeline

Gemma Usage
-----------
Although the competition requires using Gemma E2B, I wasn’t able to run it on my device 
due to hardware limitations. Given the right resources, I could enhance this project 
with web search, a RAG pipeline, and more advanced prompting for even better results.

For showcase purposes, I used Ollama’s Gemma 2B model locally. It still demonstrates 
the core idea and structure of the system.

Challenges
----------
- Filename Sanitization: Windows rejects filenames with characters like `:` or `*`, so 
  I implemented a sanitization function to clean topic names before saving.
- Fallback Handling: If chapter generation fails, the system logs the error and inserts 
  a fallback message in the final textbook to maintain structure.

Design Choices
--------------
- Modular Structure: Each component (prompting, generation, I/O) is isolated for clarity 
  and reusability.
- Prompt Layering: Prompts are built in a structured way to guide the LLM effectively.
- Scalable Pipeline: The system can easily be extended to support other models, 
  web-based interfaces, or PDF export.
- Clean Output: Chapters are saved with readable formatting and compiled into a 
  professional-looking `.txt` textbook.

Code Snippet — Filename Sanitization
------------------------------------
```python
def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip().rstrip('.')
    return name.replace(' ', '_')
