import os
import subprocess
import zipfile
from typing import List

class ToolExecutor:
    @staticmethod
    def create_file(path: str, content: str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)
        return f"File created: {path}"

    @staticmethod
    def run_command(command: str):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return f"Success: {result.stdout}"
            else:
                return f"Error: {result.stderr}"
        except Exception as e:
            return f"Execution failed: {str(e)}"

    @staticmethod
    def create_zip(folder_path: str, zip_name: str):
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    zipf.write(os.path.join(root, file), 
                               os.path.relpath(os.path.join(root, file), 
                               os.path.join(folder_path, '..')))
        return f"Project zipped as: {zip_name}"

    @staticmethod
    def get_3d_template():
        return """
<!DOCTYPE html>
<html>
<head>
    <title>3D Shivam Experience</title>
    <style>
        body { margin: 0; overflow: hidden; background: #000; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        const geometry = new THREE.TorusKnotGeometry(10, 3, 100, 16);
        const material = new THREE.MeshNormalMaterial({ wireframe: true });
        const torusKnot = new THREE.Mesh(geometry, material);
        scene.add(torusKnot);

        camera.position.z = 30;

        function animate() {
            requestAnimationFrame(animate);
            torusKnot.rotation.x += 0.01;
            torusKnot.rotation.y += 0.01;
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
"""
