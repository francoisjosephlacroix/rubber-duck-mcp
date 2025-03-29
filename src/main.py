import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.tools.rubber_duck import RubberDuckTool

app = FastAPI(title="Rubber Duck MCP Server")

# Initialize tools
rubber_duck = RubberDuckTool()

class RubberDuckRequest(BaseModel):
    code: str
    context: Optional[str] = None

@app.post("/tools/rubber-duck")
async def rubber_duck_endpoint(request: RubberDuckRequest):
    """
    Endpoint for the rubber duck debugging tool.
    Receives code and context, but doesn't return anything.
    """
    try:
        await rubber_duck.process(request.code, request.context)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    
    # Determine if we're in production
    is_production = os.getenv("ENVIRONMENT", "development") == "production"
    
    # Configure SSL for production
    ssl_config = {}
    if is_production:
        ssl_config = {
            "ssl_keyfile": os.getenv("SSL_KEYFILE"),
            "ssl_certfile": os.getenv("SSL_CERTFILE"),
        }
    
    # Start the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=not is_production,
        **ssl_config
    ) 