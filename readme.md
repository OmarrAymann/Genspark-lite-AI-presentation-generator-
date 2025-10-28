# Genspark lite

PowerPoint presentation generator with modern design and intelligent content creation.

## Architecture Overview

### How It Works

#### Streamlit Frontend
- Collects topic, slide count, and theme  
- Sends data to Flask backend via HTTP POST  

#### Flask Backend (`server.py`)
- Handles `/generate` endpoint  
- Calls Gemini API through `prompt.py` to generate text content  
- Passes generated text to `ppt_generator.py` to create PowerPoint slides  

#### LLM Layer (`prompt.py`)
- Uses **Gemini 2.5 Flash** for natural language generation  
- Generates:  
  - Slide titles  
  - Bullet points (2–5 per slide)  
  - Summaries and subtitles  

#### PowerPoint Generator (`ppt_generator.py`)
- Uses **python-pptx** for slide creation and styling  
- Applies selected color theme and typography  
- Adds accent bars, spacing, and consistent formatting  

## Features

**Design**

- 4 professional color themes
- Clean typography using different modern fonts
- Genspark-inspired layout

**Slide Templates**

- Title slide with subtitle
- aries number of bullet points dynamically per slide (2–5 points)
- Content slides with section titles
- Questions & Thank you slides

## Installation

### 1. Clone or Download Files

Create a project directory with these files:
Genspark lite/
├── server.py
├── ppt_generator.py
├── prompt.py
├── requirements.txt
└── README.md


### 2. Install Dependencies

pip install -r requirements.txt

### 3. Configure API Key

- Open `prompt.py` and replace the API key with your own Google Gemini API key:

**Get your API key:** https://makersuite.google.com/app/apikey

## Key Technologies
###  Component	                 Purpose

- Flask	                   REST API backend
- python-pptx	           PowerPoint slide creation
- Gemini API               LLM for text generation
- requests	               API communication between frontend and backend
- Streamlit	               Web-based user interface

## Usage

### Start the Server

python app.py

The server will start on `http://localhost:5000`

### Generate a Presentation

#### Using cURL:

curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "Artificial Intelligence in Healthcare", "slides": 14}' \
  --output presentation.pptx


#### Using Python:

import requests

response = requests.post('http://localhost:5000/generate',
    json={
        "topic": "Artificial Intelligence in Healthcare",
        "slides": 14
    }
)
with open('presentation.pptx', 'wb') as f:
    f.write(response.content)

### API Endpoints

#### POST /generate

Generate a presentation

**Request Body:**

{
    "topic": "Your Topic Here",
    "slides": 14
}

**Parameters:**
- `topic` (string, required): Presentation topic
- `slides` (integer, optional): Number of slides (5-50, default: 14)

**Response:** PowerPoint file (.pptx)

## Presentation Structure

For a 14-slide presentation:

1. **Title Slide** - Main topic + AI-generated subtitle

2-12. **Content Slides** - Structured sections:
   - Introduction & Overview
   - Key Concepts & Fundamentals
   - Current Applications & Use Cases
   - Benefits & Advantages
   - Challenges & Considerations
   - Future Trends & Opportunities
   - Implementation Strategies
   - Best Practices & Recommendations
   - Case Studies & Real-World Examples
   - Impact & Results
   - Strategic Insights
13. **Key Takeaways** - Summary slide with 5 main points
14. **Questions** - Interactive discussion prompt
15. **Thank You** - Professional closing

## Customization

### Modify Content Generation

Edit `prompt.py` to adjust:

- Tone and style guidelines
- Bullet point length
- Number of points per slide
- Section titles

## Requirements

- Python 3.10+
- Internet connection (for AI content generation)
- Google Gemini API key (free tier available)

## License

This project uses:
- Flask (BSD License)
- python-pptx (MIT License)
- Google Generative AI (Google Terms)
