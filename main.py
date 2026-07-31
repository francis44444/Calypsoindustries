<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Dashboard</title>
</head>
<body>
    <h1>Welcome to the FastAPI Dashboard</h1>
    <div id="project-management">
        <h2>Project Management</h2>
        <button onclick="createProject()">Create Project</button>
        <button onclick="deleteProject()">Delete Project</button>
    </div>
    <div id="simulation">
        <h2>Run Simulation</h2>
        <button onclick="runSimulation()">Run</button>
        <button onclick="stopSimulation()">Stop</button>
        <button onclick="submitToIBMQuantum()">Submit to IBM Quantum</button>
    </div>
    <script>
        async function createProject() {
            const response = await fetch('/api/projects', { method: 'POST' });
            console.log('Project created:', response);
        }
        async function deleteProject() {
            const response = await fetch('/api/projects', { method: 'DELETE' });
            console.log('Project deleted:', response);
        }
        async function runSimulation() {
            const response = await fetch('/api/simulate', { method: 'POST' });
            console.log('Simulation started:', response);
        }
        async function stopSimulation() {
            const response = await fetch('/api/simulate', { method: 'DELETE' });
            console.log('Simulation stopped:', response);
        }
        async function submitToIBMQuantum() {
            const response = await fetch('/api/quantum/submit', { method: 'POST' });
            console.log('Submission to IBM Quantum:', response);
        }
    </script>
</body>
</html>