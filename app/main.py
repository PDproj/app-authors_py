import uvicorn
import os

# cast to int
SERVER_PORT = int(os.environ.get('SERVER_PORT', 8000))

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0",
                port=SERVER_PORT, reload=True)
