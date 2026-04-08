# AI Log Analyzer

An AI-powered tool to analyze test failure logs and provide root cause analysis and suggested fixes using OpenAI's GPT models.

## Features

- Extracts failure-related lines from test logs
- Uses GPT-4o-mini to classify root causes (e.g., Assertion failure, Element not found, Timeout, API error)
- Provides detailed analysis with reasons and suggested fixes
- Command-line interface for quick analysis
- Web UI using Streamlit for interactive analysis

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/PaLiNYG96/AI-Log-Analyzer.git
   cd AI-Log-Analyzer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

### Command Line

Run the analyzer on a log file:
```
python main.py [log_file_path]
```

If no file is specified, it defaults to `fail.log` in the project root.

Example:
```
python main.py sample_logs/testcafe_fail.log
```

### Web UI

Launch the Streamlit web interface:
```
streamlit run ui/app.py
```

Paste your test log into the text area and click "Analyze" for interactive analysis.

## Project Structure

- `main.py`: Command-line entry point
- `analyze.py`: OpenAI API integration for log analysis
- `preprocess.py`: Log preprocessing to extract failure lines
- `ui/app.py`: Streamlit web application
- `requirements.txt`: Python dependencies
- `sample_logs/`: Sample log files for testing

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls

## License

This project is licensed under the MIT License.