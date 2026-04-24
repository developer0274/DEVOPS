import subprocess
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class LocalShellToolSchema(BaseModel):
    """Input schema for the LocalShellTool."""
    command: str = Field(..., description="The shell command to execute on the local machine.")

class LocalShellTool(BaseTool):
    name: str = "Local Shell Command Executor"
    description: str = (
        "Executes a shell command on the local machine and returns the output. "
        "Useful for running 'docker build', 'terraform validate', or linting commands to verify code."
    )
    args_schema: type[BaseModel] = LocalShellToolSchema

    def _run(self, command: str) -> str:
        """Execute the command."""
        try:
            print(f"\n[TOOL EXECUTION] Running shell command: {command}")
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Command Failed with Exit Code {e.returncode}.\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}"
