# AI Data Analyst

A Streamlit-based web application that leverages AI to analyze and visualize data through natural language queries. Upload your dataset and get instant insights through conversational interactions.

<p align="center">
  <img src="https://github.com/user-attachments/assets/186e287b-92b5-4c05-9740-2bf334479d05" alt="App Screenshot" width="800"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/3ac0eaf0-6133-478f-b2bb-6dc319c58f60" alt="App Screenshot" width="800"/>
</p>

## Features

- **Easy Data Upload**: Supports CSV and Excel file formats
- **Natural Language Queries**: Ask questions about your data in plain English
- **Interactive Visualizations**: Generates relevant charts and graphs
- **Conversation History**: Maintains context of your analysis session
- **Responsive Design**: Works on both desktop and mobile devices

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- An OpenAI API key (or other supported LLM provider)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/muhammadhamzaazhar/Data-Analysis.git
   cd Data-Analysis
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add your API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   LLM_MODEL=openrouter/deepseek/deepseek-chat-v3.1:free
   LLM_TEMPERATURE=0.5
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```
   
2. Upload your dataset using the sidebar

3. Start asking questions about your data in natural language
   

## Example Queries

- "Show me the distribution of sales by region"
- "What are the top 5 products by revenue?"
- "Create a scatter plot of price vs. sales"
- "What's the average order value?"
- "Show me trends in customer purchases over time"

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [PandasAI](https://github.com/Sinaptik-AI/pandas-ai)
