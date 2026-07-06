# GK_HI

A Python library containing 200+ General Knowledge questions in Hindi.

# Installation
```bash
pip install GK-HI
```

# How to Use

```python
import gk_hi

# Get all questions
all_questions = gk_hi.get_all()
print(f"Total questions: {len(all_questions)}")

# Get 5 random questions
random_questions = gk_hi.get_random(5)
for q in random_questions:
    print(q)

# Search for questions containing "भारत"
search_results = gk_hi.search("भारत")
print(f"Found {len(search_results)} questions with 'भारत'")
```

# Structure
The library has the following structure:
```
gkhindi/
├── __init__.py
├── main.py
└── questions.py
```
