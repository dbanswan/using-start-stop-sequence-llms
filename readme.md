# Getting Valid JSON back from LLM's

## Prerequisites

- A valid Anthropic API key
- python 3.8 or higher
- pip installed

## Installation

```bash
# Create a virtual environment (optional but recommended)
python -m venv claude-env
source venv/bin/activate
# On Windows use `venv\Scripts\activate`  or `.\venv\Scripts\activate`

# Clone the repository
git clone https://github.com/dbanswan/using-start-stop-sequence-llms.git
# Install the required packages
pip install -r requirements.txt
```

## Usage

2. Create a `.env` file in the root directory of the project and add your Anthropic API key:

```
CLAUDE_API_KEY=your_api_key_here
```

3. Run following to see how the response looks without using start and stop sequences:

```bash
python not-using-start-stop-sequence.py
```

This will generate a JSON response without the start and stop sequences, also will contain few header or footer text.

4. Run following to see how the response looks with using start and stop sequences:

```bash
python using-start-stop-sequence.py
```

This will be a valid JSON response without any header or footer text, also without any markdown code block.

Feel free to modify or change the prompts in both the scripts to see how the response changes.

Credits :
Thanks Anthropic Academy✌🏼
