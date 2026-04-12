import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://user:password@cluster0.example.mongodb.net/?retryWrites=true&w=majority")
MONGODB_DB = os.getenv("MONGODB_DB", "calypso_simulations")

# IBM Quantum Configuration
IBM_QUANTUM_TOKEN = os.getenv("IBM_QUANTUM_TOKEN", "")
IBM_QUANTUM_CHANNEL = os.getenv("IBM_QUANTUM_CHANNEL", "ibm_quantum")

# Project Configuration
PROJECT_BASE = os.path.expanduser("~/Calypsoindustries")

# FastAPI Configuration
API_HOST = "127.0.0.1"
API_PORT = 8000
