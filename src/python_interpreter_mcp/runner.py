import os
import subprocess


async def execute_script(code: str) -> str:
    """
    Takes in a block of Python code and runs it in a subprocess using uv.
    :param code: Chunk of code to be executed.
    :return: Output of the execution.
    """
    sandbox_dir = os.path.join(os.getcwd(), ".my_tool_sandbox")
    os.makedirs(sandbox_dir, exist_ok=True)

    script_file_path = os.path.join(sandbox_dir, "script.py")
    with open(script_file_path, "w") as f:
        f.write(code)

    print(f"\nRunning script: uv run {script_file_path}")
    try:
        result = subprocess.run(
            ['uv', 'run', script_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=5,
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Error: Subprocess timed out."
    except Exception as e:
        return f"Exception: {e}"
