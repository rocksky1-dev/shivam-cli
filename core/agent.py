import os
import json
import requests
from typing import List, Dict, Any

class ShivamAgent:
    def __init__(self, api_key: str, model_id: str):
        self.api_key = api_key
        self.model_id = model_id
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.memory_file = "shivam_memory.json"
        self.history = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def _save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def chat(self, message: str):
        self.history.append({"role": "user", "content": message})
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/rocksky1-dev/shivam-cli", # Optional
            "X-Title": "SHIVAM CLI", # Optional
        }
        
        payload = {
            "model": self.model_id,
            "messages": [
                {"role": "system", "content": "You are SHIVAM CLI, an Ultra Instinct AI Agent. You are highly autonomous, capable of planning, verifying, and executing complex tasks like building 3D websites, apps, and full-stack projects. You output high-quality code and can package them into .zip files."},
                *self.history
            ]
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            data = response.json()
            
            ai_message = data['choices'][0]['message']['content']
            self.history.append({"role": "assistant", "content": ai_message})
            self._save_memory()
            return ai_message
        except Exception as e:
            return f"Error: {str(e)}"

    def plan_task(self, goal: str):
        prompt = f"""Plan the execution for the following goal: {goal}. 
        Break it down into specific steps.
        Return ONLY a JSON list of tasks like this:
        [
            {{"type": "FILE", "target": "filename.js", "desc": "Create main file"}},
            {{"type": "COMMAND", "target": "npm install", "desc": "Install deps"}}
        ]
        """
        response = self.chat(prompt)
        try:
            # Extract JSON from response
            import re
            json_match = re.search(r'\[.*\]', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))
        except:
            return [{"type": "ERROR", "target": "Planning", "desc": "Failed to parse plan"}]
        return []

    def execute_step(self, task: Dict[str, str]):
        # This will be connected to the ToolExecutor
        pass
