from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location:str) -> str:
    """
    Get the current weather for a specified location.
    Args:
        location (str): The name of the location to get the weather for.
    
    Returns:
        str: A string describing the current weather conditions.
    """
    # Placeholder implementation
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """
    Resource to get weather information for a specific location.
    
    Args:
        location (str): The name of the location to get the weather for.
    
    Returns:
        str: A string describing the current weather conditions.
    """
    return f"Weather data for {location}: Sunny, 25°C."

@mcp.prompt()
def weather_report(location: str) -> str:
    """
    Generate a weather report prompt for a specified location.
    
    Args:
        location (str): The name of the location to generate the report for.
    
    Returns:
        str: A detailed weather report.
    """
    return f"""You are a weather Reporter. Weather Report for {location}?"""

if __name__ == "__main__":
    #mcp.run(transport="http", port=8000, debug=True)
    mcp.run(transport="sse", port=3001)
