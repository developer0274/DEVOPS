import os
import sys
from dotenv import load_dotenv
from crewai import Crew, Process
from agents.devops_agents import DevOpsAgents
from tasks.devops_tasks import DevOpsTasks

# Load environment variables (API Keys)
load_dotenv()

def run():
    print("==================================================")
    print("🚀 INITIALIZING PROFESSIONAL AI DEVOPS TEAM...")
    print("==================================================")
    
    # Ensure at least one API key is set
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ Error: Please set OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file.")
        sys.exit(1)

    # Initialize agents
    print("[+] Waking up agents: Architect, Automation Engineer, Security Analyst...")
    agents = DevOpsAgents()
    architect = agents.lead_architect()
    automation_engineer = agents.automation_engineer()
    security_analyst = agents.security_analyst()

    # Initialize tasks
    print("[+] Defining DevOps pipeline tasks...")
    tasks = DevOpsTasks()
    
    # The default prompt for our demo
    project_desc = "A Python web application using FastAPI that needs to be dockerized, deployed to AWS Elastic Container Service (ECS), and requires a robust GitHub Actions CI/CD pipeline."
    
    repo_analysis = tasks.analyze_infrastructure(architect, project_desc)
    pipeline_creation = tasks.create_ci_cd_pipeline(automation_engineer, [repo_analysis])
    security_audit = tasks.audit_security(security_analyst, [repo_analysis, pipeline_creation])

    # Form the crew
    devops_crew = Crew(
        agents=[architect, automation_engineer, security_analyst],
        tasks=[repo_analysis, pipeline_creation, security_audit],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    print(f"\n[EXECUTION] 🧠 The AI Team is analyzing the requirements: '{project_desc}'\n")
    result = devops_crew.kickoff()

    print("\n==================================================")
    print("✅ DEVOPS TEAM EXECUTION COMPLETE")
    print("==================================================")
    print("Final Output:\n")
    print(result)

if __name__ == "__main__":
    run()
