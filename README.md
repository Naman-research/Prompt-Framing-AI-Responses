# Prompt Framing and AI Response Bias

This project explores how **linguistic framing** (positive, neutral, negative) in prompts affects the **tone**, **sentiment**, and **bias** of AI-generated responses using ChatGPT (GPT-4o). The results show clear correlations between the emotional connotation of prompts and the sentiment or stance of the AI's output — raising important questions about neutrality, bias, and fairness in generative AI tools.

## 🧪 Overview of Methodology

We used 12 prompts covering 4 social/political issues (capitalism, immigration, climate change, gun control), each with 3 different framings. Responses were analyzed based on:

- **Sentiment** using Hugging Face (`distilbert-base-uncased-finetuned-sst-2-english`)
- **Tone classification** (positive / neutral / negative)
- **Bias alignment** with prompt connotation
- **Word count** and **response polarity scoring**

## 📁 Project Structure

Prompt-Framing-AI-Responses/
├── data/
│ ├── #001.txt, #002.txt, ... # Raw AI-generated responses
│ └── .gitkeep # Keeps folder tracked
├── analysis/
│ ├── sentiment_analysis.py # Python script for sentiment scoring
│ └── .gitkeep # Placeholder file
├── figures/ (optional)
│ └── graphs or charts # Visuals (if added)
├── README.md # This file

## Folder Structure

- `data/`: Contains AI-generated responses in `.txt` format. Each file (e.g., `001.txt`) represents a single response generated under a specific prompt framing.


## 🛠️ Tools and Libraries

- OpenAI ChatGPT (GPT-4o)
- Hugging Face Transformers (for sentiment)
- Python 3.x
- Matplotlib / Pandas (for analysis)

## 🔍 How to Use

1. Clone or download the repo.
2. Place AI responses in the `data/` folder (already includes sample `.txt` files).
3. Run the analysis script (e.g., `sentiment_analysis.py`) to calculate sentiment scores.
4. View results and visualizations (if included).

### Example (Command Line):

```bash
python analysis/sentiment_analysis.py

✅ Notes
Connotation scores: +1 (positive), 0 (neutral), -1 (negative)

Sentiment mapping: Positive → 1, Negative → -1, Neutral → 0

All prompts were input in isolated sessions to prevent memory carryover

📌 Limitations
Small sample size (12 prompts)

Only one AI model tested (GPT-4o)

Sentiment model may not capture nuance or sarcasm

✍️ Author
[Naman Tripathi] – AI researcher and student

GitHub: [Naman-research](https://github.com/your-username/Naman-research)

📄 License
This project is released under the MIT License. Feel free to use, adapt, and share with attribution.

If you use or build upon this project, consider citing or referencing it!

---

### ✅ What to do next:

1. Go to your GitHub repo homepage.
2. Click **Add File > Create New File** → name it `README.md`.
3. Paste the above content.
4. Hit **Commit**.
