# LocaLLM

A simple Python package that lets you interact with a large language model (LLM) locally, based on [Ollama](https://ollama.com).

## Dependencies

- Python 3.11 or higher
- Ollama
- Requests library

## Installation

1. [Download](https://ollama.com/download) and Install Ollama

2. Clone the repository

   ```bash
    git clone https://github.com/glaciapag/locallm.git
   ```

3. Navigate to the project directory

   ```bash
    cd locallm
   ```

4. Create and activate a virtual environment

   ```bash
    python -m venv venv
    source venv/bin/activate # On windows use `venv\Scripts\activate`
   ```

5. Install [poetry](https://python-poetry.org)

   ```bash
    pip install poetry
   ```

6. Install the project and dependencies

   ```bash
    poetry install
   ```

## Usage

### Initial Setup

Before using the package, make sure Ollama is properly configured and running locally.

#### Running the Ollama server

```bash
ollama serve
```

#### Downloading models

```bash
ollama run llama3
```

More information can be found in the Ollama [documentation](https://github.com/ollama/ollama).

### Sample Code

```python
from locallm import AIChatbot

ai = AIChatbot()
answer = ai.ask("What is the capital of the Philippines")
print(answer)
```

### Sample Output

```bash
{'model': 'llama3', 'created_at': '2024-07-22T10:49:11.274119Z', 'response': 'The capital of the Philippines is Manila.', 'done': True, 'done_reason': 'stop', 'context': [128006, 882, 128007, 271, 3923, 374, 279, 6864, 315, 26363, 128009, 128006, 78191, 128007, 271, 791, 6864, 315, 279, 26363, 374, 57664, 13], 'total_duration': 9569433512, 'load_duration': 7126954944, 'prompt_eval_count': 16, 'prompt_eval_duration': 1128135000, 'eval_count': 9, 'eval_duration': 1312084000}
```

### Changing the runtime model

```python
from locallm import AIChatbot
from locallm.config import DefaultConfig

# Changing the model from llama3 (default) to llama2
class Llama2Config(DefaultConfig):
    model = "llama2"

ai = AIChatbot(Llama2Config)
answer = ai.ask("What is the capital of the Philippines")
print(answer)
```

```bash
{'model': 'llama2', 'created_at': '2024-07-22T10:53:49.189766Z', 'response': 'The capital of Philippines is Manila.', 'done': True, 'done_reason': 'stop', 'context': [518, 25580, 29962, 3532, 14816, 29903, 29958, 5299, 829, 14816, 29903, 6778, 13, 13, 5618, 338, 278, 7483, 310, 26260, 518, 29914, 25580, 29962, 13, 1576, 7483, 310, 26260, 338, 2315, 4233, 29889], 'total_duration': 12565333601, 'load_duration': 8434900459, 'prompt_eval_count': 26, 'prompt_eval_duration': 2611097000, 'eval_count': 9, 'eval_duration': 1518017000}
```

## Contributing

1. Fork the repository.
2. Create a new branch: git checkout -b my-feature-branch.
3. Make your changes and commit them: git commit -m 'Add some feature'.
4. Push to the branch: git push origin my-feature-branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact <glenn.laciapag@gmail.com>.
