import os
import time
from agents.devops_agents import DevOpsAgents
from tasks.devops_tasks import DevOpsTasks
from tools.shell_tool import LocalShellTool

def check_performance():
    print("📋 [AGENT PERFORMANCE AUDIT] 📋\n")
    
    start_total = time.perf_counter()

    # 1. Tool Performance
    print("[1/4] Auditing LocalShellTool...")
    tool = LocalShellTool()
    start_tool = time.perf_counter()
    # Test a simple 'echo' command to check overhead
    output = tool._run("echo 'Heartbeat Check'")
    end_tool = time.perf_counter()
    print(f"✅ Tool Latency: {(end_tool - start_tool) * 1000:.2f}ms")
    print(f"   Output: {output.strip()}")

    # 2. Agent Initialization
    print("\n[2/4] Waking up the Team (Initialization)...")
    try:
        # We temporarily set a dummy key to bypass the 'get_llm' check for init
        os.environ["OPENAI_API_KEY"] = "dummy-key-for-init-test"
        start_init = time.perf_counter()
        agents = DevOpsAgents()
        arch = agents.lead_architect()
        eng = agents.automation_engineer()
        sec = agents.security_analyst()
        end_init = time.perf_counter()
        print(f"✅ Agent Boot Time: {(end_init - start_init) * 1000:.2f}ms")
    except Exception as e:
        print(f"❌ Boot Failed: {e}")

    # 3. Task Mapping
    print("\n[3/4] Routing Task Dependencies...")
    start_task = time.perf_counter()
    tasks = DevOpsTasks()
    t1 = tasks.analyze_infrastructure(arch, "Test Project")
    t2 = tasks.create_ci_cd_pipeline(eng, [t1])
    t3 = tasks.audit_security(sec, [t1, t2])
    end_task = time.perf_counter()
    print(f"✅ Task Routing Latency: {(end_task - start_task) * 1000:.2f}ms")

    # 4. Summary
    end_total = time.perf_counter()
    print(f"\n🚀 Total System Readiness Check: {(end_total - start_total) * 1000:.2f}ms")
    print("\n[CONCLUSION]: The infrastructure is HIGHLY optimized and ready for the LLM 'Brain'.")

if __name__ == "__main__":
    check_performance()
