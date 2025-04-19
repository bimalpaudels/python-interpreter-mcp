from .server import server


def main():
    """Main entrypoint for the MCP server."""
    import asyncio

    print("Starting Python-Interpreter-MCP server")
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
