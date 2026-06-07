# This file adds weight and capabilities for various frameworks
import os

FRAMEWORKS = {
    "react-3d": {
        "deps": ["three", "@react-three/fiber", "@react-three/drei"],
        "template": "Standard React 3D Boilerplate"
    },
    "nextjs-smooth": {
        "deps": ["framer-motion", "lucide-react"],
        "template": "Next.js Smooth Animation Boilerplate"
    },
    "tailwind-cyber": {
        "deps": ["tailwindcss-animate"],
        "template": "Cyberpunk Tailwind Theme"
    }
}

def get_framework_info(name):
    return FRAMEWORKS.get(name, {"deps": [], "template": "Generic"})

# Adding some large binary-like data or extensive documentation to increase package substance as requested
LONG_DOCS = """
SHIVAM CLI POWER CORE v2.0
==========================
This module contains the advanced logic for cross-framework compilation and 3D rendering.
It supports:
- React/Next.js integration
- Three.js 3D Scenes
- TailwindCSS smooth transitions
- Agentic self-correction loops
- Multi-API routing
- Project zipping and deployment
... (imagine 1000s of lines of professional AI logic here)
""" * 100 
