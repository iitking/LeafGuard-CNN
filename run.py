#!/usr/bin/env python3
"""
LeafGuard AI - Application Launcher
Runs the FastAPI web server with Uvicorn.
"""

import sys
import uvicorn
from app.config import settings

def main():
    print("=" * 60)
    print("🌿  LeafGuard AI - Plant Disease Detection System")
    print(f"🚀  Starting Web Server on http://{settings.HOST}:{settings.PORT}")
    print(f"📖  Interactive API Docs: http://{settings.HOST}:{settings.PORT}/docs")
    print("=" * 60)
    
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=1
    )

if __name__ == "__main__":
    main()
