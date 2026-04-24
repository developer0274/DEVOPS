# 🚀 Professional AI DevOps Agent Team

A highly productive, multi-agent AI system designed to automate and standardize DevOps workflows. Powered by **CrewAI**, this team operates with the speed and proficiency of senior cloud engineers. 

You can easily switch the underlying LLM to **Claude 3 (Anthropic)** or **GPT-4o (OpenAI)** for industry-leading reasoning.

## 🤖 The Team
1. **Lead DevOps Architect:** Designs scalable infrastructure, Dockerizes applications, and writes Terraform/OpenTofu configurations.
2. **Automation Engineer:** Crafts robust CI/CD pipelines (GitHub Actions, GitLab CI) based on the architect's designs.
3. **DevSecOps Analyst:** Audits all generated code for security vulnerabilities and enforces least privilege.

## 🛠️ Features
- **Local Tooling:** Agents can execute local shell commands to validate Dockerfiles, run linting, or deploy infrastructure.
- **Fast & Modular:** Built on a clean Python package structure, ready for enterprise integration.
- **Claude / GPT Ready:** Designed to work flawlessly with top-tier LLMs for advanced logical reasoning.

## 📦 Setup & Usage
1. **Install Dependencies:**
   ```bash
   pip install -e .
   ```

2. **Configure API Keys:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=sk-...
   # Or for Claude:
   # ANTHROPIC_API_KEY=sk-ant-...
   ```

3. **Run the Team:**
   ```bash
   devops
   # or
   python main.py
   ```
