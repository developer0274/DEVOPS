from crewai import Task
from textwrap import dedent
from typing import List

class DevOpsTasks:
    def analyze_infrastructure(self, agent, project_description: str) -> Task:
        return Task(
            description=dedent(f"""\
                Analyze the following project requirements: 
                "{project_description}"
                
                Your Task:
                1. Design the necessary infrastructure to support this project.
                2. Write out a concrete plan detailing the Dockerfile setup and the required Cloud infrastructure (e.g., AWS ECS, Terraform modules).
                3. Create the actual text content for a `Dockerfile` and a `docker-compose.yml` (or `main.tf`) that fits these requirements.
                
                Ensure the architecture is scalable and follows modern best practices.
                """),
            expected_output="A detailed architecture document including the full source code for a Dockerfile and infrastructure configuration (e.g., Terraform/Docker-compose).",
            agent=agent
        )

    def create_ci_cd_pipeline(self, agent, context: List[Task]) -> Task:
        return Task(
            description=dedent("""\
                Based on the Architect's design and generated files, create a complete CI/CD pipeline.
                
                Your Task:
                1. Create a fully functional GitHub Actions YAML file (`.github/workflows/deploy.yml`).
                2. The pipeline MUST include steps for:
                   - Code checkout.
                   - Setup of Python/Node/etc. depending on the project.
                   - Linting and unit testing.
                   - Building and pushing the Docker image to a registry (e.g., AWS ECR or Docker Hub).
                   - Deploying the container to the infrastructure defined by the Architect.
                """),
            expected_output="A complete, valid GitHub Actions YAML configuration file that fulfills all CI/CD requirements.",
            context=context,
            agent=agent
        )

    def audit_security(self, agent, context: List[Task]) -> Task:
        return Task(
            description=dedent("""\
                Review the Architect's Dockerfile/IaC and the Automation Engineer's CI/CD pipeline.
                
                Your Task:
                1. Identify any security vulnerabilities in the Dockerfile (e.g., running as root, missing multi-stage builds, exposing unnecessary ports).
                2. Audit the CI/CD pipeline for security risks (e.g., hardcoded secrets, lack of dependency scanning steps).
                3. Provide a comprehensive security report detailing what was fixed.
                4. Output the FINAL, hardened, and secure versions of the Dockerfile, IaC configs, and the CI/CD YAML file.
                """),
            expected_output="A security audit report followed by the finalized, secure source code for the Dockerfile, IaC configuration, and CI/CD pipeline.",
            context=context,
            agent=agent
        )
