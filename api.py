from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import subprocess
import json
import os

app = FastAPI()

@app.get("/hsapi")
async def execute_command():
    command = [
        "bash", "./curl.sh"
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Command executed successfully.")
        output = result.stdout
    else:
        print("Error occurred:")
        output = result.stderr
    
    output_file_path = 'output.txt'
    with open(output_file_path, 'w') as output_file:
        output_file.write(output)

    print(f"Output saved to {output_file_path}")

    try:
        with open('input.txt', 'r') as f:
            output = f.read()
        # remove the first line
        output = output[output.find('\n') + 1:]
        output = output[output.find(':') + 1:]
        json_data = json.loads(output)
        print(json_data)

        # Write the JSON data to output.json with indentation
        with open('output.json', 'w') as f:
            json.dump(json_data, f, indent=4)

        return JSONResponse(content=json_data)

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error executing curl command: {e}")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to decode JSON from response.")
