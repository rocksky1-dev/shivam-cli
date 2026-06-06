# 🤖 SHIVAM CLI - ULTRA INSTINCT MODE

SHIVAM CLI is a powerful, autonomous AI agent designed to build anything from 3D websites to complex applications directly from your terminal. Inspired by high-performance agents like Claude Code and Antigravity, it features a stunning cyberpunk UI and leverages OpenRouter for state-of-the-art LLM capabilities.

## 🚀 Features

- **Cyberpunk Terminal UI**: Beautifully designed interface using the `Rich` library.
- **Autonomous Building**: Use `/goal <idea>` to let Shivam CLI plan, write, and verify your projects.
- **OpenRouter Integration**: Connect to any model (Claude 3.5 Sonnet, GPT-4o, etc.) via OpenRouter.
- **Full-Stack Capability**: Builds 3D websites, apps, and more in any framework.
- **Project Packaging**: Automatically zips your projects for easy sharing.
- **Task Verification**: Self-correcting logic to ensure code quality.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rocksky1-dev/shivam-cli.git
   cd shivam-cli
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

3. Set up your environment:
   Create a `.env` file or export your API key:
   ```bash
   export OPENROUTER_API_KEY='your_api_key_here'
   export MODEL_ID='anthropic/claude-3.5-sonnet'
   ```

## 🎮 Usage

Run the CLI:
```bash
shivam
```

### Commands:
- `/goal <idea>`: Start an autonomous build process.
- `/chat`: Chat with the AI.
- `/status`: View system status and UI.
- `/memory`: Check the agent's memory.
- `/exit`: Close the CLI.

## 🌈 UI Preview

The CLI features a matrix-style execution view, real-time system status, and a dedicated command center.

---
Built with ❤️ by Shivam
