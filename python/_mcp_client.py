import json
import os
from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import nest_asyncio
import uvicorn

os.environ["OPENAI_API_KEY"] = ""

messages = [] 

async def setup_mcp_servers(): 
    servers = []
    with open('mcp.json', 'r') as f: 
        config = json.load(f)        
    
    for server_name, server_config in config.get('mcpServers', {}).items():
        mcp_server = MCPServerStdio(
            params={
                "command": server_config.get("command"),
                "args": server_config.get("args", [])
            },
            cache_tools_list=True
        )
        await mcp_server.connect()
        servers.append(mcp_server)

    return servers

async def setup_agent(): 
    mcp_servers = await setup_mcp_servers()
    agent = Agent(
        name="Assistant",
        instructions="You are smart chatbot", 
        model="gpt-4o-mini", 
        mcp_servers=mcp_servers
    )
    return agent, mcp_servers


async def process_user_message(user_message: str)->str: 
    agent, mcp_servers = await setup_agent() 
    append_message(True, user_message) 

    result = Runner.run_sync(           
            agent, 
            input=messages
        )
    response = str(result.final_output) 
    append_message(False, response)   

    for server in mcp_servers: 
        await server.__aexit__(None,None,None) 
    
    return response


def append_message(isUser: bool, message: str): 
    if(isUser):
        messages.append({"role":"user", "content":message})
    else:
        messages.append({"role":"assistant", "content":message})





nest_asyncio.apply() 
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/chat")
async def chat_api(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    response = await process_user_message(user_message)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)