from openai import OpenAI
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json

config = dotenv_values('.env')
client = OpenAI(api_key=config["OPENAI_API_KEY"])

app = Flask(__name__,
            template_folder = 'templates'
            )
def get_colors(msg):
    # Prepare the prompt content for the API call
    content = f"""
    You are a color palette generating assistant that responds to text prompts to make primary color palettes.
    Generate color palettes that fit the theme, mood, or instructions in the prompt.

    Format: JSON array of hexadecimal color codes

    Text: {msg}
    """
    # Make the API call to the OpenAI service
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": content}
        ],
        model="gpt-3.5-turbo-1106",
        max_tokens=200
    )
    # Parse the JSON array API response to a Python list.
    palette = json.loads(response.choices[0].message.content)
    return palette

# Home page route
@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    # RETURN LIST OF COLORS as JS object
    return {"colors": colors}


# Home page route
@app.route("/")
def index():
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)