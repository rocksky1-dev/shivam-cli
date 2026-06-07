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
    def get_3d_template(title="SHIVAM 3D EXPERIENCE"):
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ margin: 0; overflow: hidden; background: radial-gradient(circle at center, #1a1a2e 0%, #16213e 50%, #0f3460 100%); }}
        #ui {{ position: absolute; top: 20px; left: 20px; color: #00f2fe; font-family: 'Courier New', Courier, monospace; pointer-events: none; }}
        canvas {{ display: block; }}
    </style>
</head>
<body>
    <div id="ui">
        <h1 class="text-3xl font-bold tracking-widest">SHIVAM CLI v2.0</h1>
        <p class="text-sm opacity-70">ULTRA INSTINCT GENERATED SCENE</p>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        document.body.appendChild(renderer.domElement);

        const geometry = new THREE.IcosahedronGeometry(10, 1);
        const material = new THREE.MeshPhongMaterial({{ 
            color: 0x00f2fe, 
            wireframe: true,
            emissive: 0x00f2fe,
            emissiveIntensity: 0.5
        }});
        const mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);

        const light = new THREE.PointLight(0xffffff, 1, 100);
        light.position.set(10, 10, 10);
        scene.add(light);
        scene.add(new THREE.AmbientLight(0x404040));

        camera.position.z = 25;
        const controls = new THREE.OrbitControls ? new THREE.OrbitControls(camera, renderer.domElement) : null;

        function animate() {{
            requestAnimationFrame(animate);
            mesh.rotation.x += 0.005;
            mesh.rotation.y += 0.01;
            if (controls) controls.update();
            renderer.render(scene, camera);
        }}
        animate();

        window.addEventListener('resize', () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});
    </script>
</body>
</html>
"""

    @staticmethod
    def generate_project_structure(framework, name):
        # Professional scaffolding logic
        structure = {
            "src": ["components", "assets", "utils"],
            "public": ["images", "fonts"],
            "tests": []
        }
        # In a real tool, this would create directories
        return f"Scaffolded {framework} project: {name}"
