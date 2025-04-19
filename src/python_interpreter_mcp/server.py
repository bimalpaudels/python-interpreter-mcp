from mcp.server.fastmcp import FastMCP
from python_interpreter_mcp.runner import execute_script


server = FastMCP("Lite-weight Python Interpreter")


@server.tool()
async def run_script(script: str) -> str:
    """Executes the given script string by passing it to execute_script function.
    :param str script: The script string to execute.
    :return: The return value of the execute_script function.
    """

    output = await execute_script(script)
    if output is None:
        return "Nothing happened. Returning None."
    return output
