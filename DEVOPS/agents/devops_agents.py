import os
from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from tools.shell_tool import LocalShellTool

def get_llm():
    """
    Returns the appropriate LLM string for CrewAI.
    Prefers GPT-4o as it has free/daily limits for some users.
    """
    if os.getenv("OPENAI_API_KEY"):
        return "gpt-4o"
    elif os.getenv("ANTHROPIC_API_KEY"):
        return "anthropic/claude-3-opus-20240229"
    else:
        raise ValueError("No API key found. Please set OPENAI_API_KEY or ANTHROPIC_API_KEY.")

class DevOpsAgents:
    def __init__(self):
        self.llm = get_llm()
        self.shell_tool = LocalShellTool()

    def lead_architect(self) -> Agent:
        return Agent(
            role='Lead DevOps Architect',
            goal='Design scalable, resilient, and cost-effective cloud infrastructure layouts and containerization strategies.',
            backstory=dedent("""\
                You are a veteran Cloud Architect who has designed infrastructure for Fortune 500 companies.
                You excel at designing Terraform/OpenTofu configurations, Docker setups, and Kubernetes clusters.
                Your solutions are always highly available, fault-tolerant, and follow the Well-Architected Framework.
                """),
            verbose=True,
            allow_delegation=True,
            tools=[self.shell_tool],
            llm=self.llm
        )

    def automation_engineer(self) -> Agent:
        return Agent(
            role='Automation & CI/CD Engineer',
            goal='Build robust, fast, and automated CI/CD pipelines for testing and deployment.',
            backstory=dedent("""\
                You are a pipeline master who breathes GitHub Actions, GitLab CI, and Jenkins.
                You believe that if a task is done twice, it should be automated. You create pipelines
                that build Docker images, run comprehensive tests, and deploy seamlessly to production environments.
                """),
            verbose=True,
            allow_delegation=False,
            tools=[self.shell_tool],
            llm=self.llm
        )

    def security_analyst(self) -> Agent:
        return Agent(
            role='DevSecOps Security Analyst',
            goal='Ensure all infrastructure, containers, and pipelines are secure by default and fully compliant.',
            backstory=dedent("""\
                You are a paranoid and meticulous security expert. You audit Dockerfiles for root user execution,
                scan dependencies for vulnerabilities, and ensure CI/CD pipelines don't leak secrets.
                You enforce the principle of least privilege across all cloud and local environments.
                """),
            verbose=True,
            allow_delegation=False,
            tools=[self.shell_tool],
            llm=self.llm
        )
