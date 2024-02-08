# Import necessary libraries
from openai import OpenAI
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json

# Load configuration from .env file
config = dotenv_values('.env')

# Initialize OpenAI client with API key
client = OpenAI(api_key=config["OPENAI_API_KEY"])

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

def get_colors(msg):
    """
    Generate a color palette based on the provided message.
    
    Args:
    msg (str): The message to generate the color palette from.
    
    Returns:
    list: A list of hexadecimal color codes in a consistent JSON array format.
    """
    # Prepare the prompt content for the API call
    prompt = f"""
    You are a highly consistent color palette generating assistant. Respond only in a JSON array format of hexadecimal color codes. Generate 1 color palette that fits the theme, mood, or instructions in the prompt. The palette should include exactly 5 colors, unless a specific number of colors is stated in the prompt.

    Example prompt and response:
    Prompt: Ocean sunrise
    Response: ["#FF5733", "#FFC300", "#FF5733", "#FF5733", "#C70039"]

    Text: {msg}
    """

    # Make the API call to the OpenAI service
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo",
        max_tokens=200
    )

    # Attempt to parse the response
    try:
        # Extract and return the JSON array response directly
        colors = json.loads(response.choices[0].message.content)
        # Ensure the result is a list of colors; otherwise, raise ValueError
        if not isinstance(colors, list) or not all(isinstance(color, str) and color.startswith('#') for color in colors):
            raise ValueError("Response format is incorrect")
        return colors
    except (ValueError, json.JSONDecodeError) as e:
        # Log the error or handle it as appropriate
        print(f"Error parsing the API response: {e}")
        # Return a default color palette or handle the error as needed
        return ["#FFFFFF", "#CCCCCC", "#999999"]

# Flask route handling for generating color palettes
@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    # Retrieve the user's query from the form data
    query = request.form.get("query")

    # Generate color palette based on the user's query
    colors = get_colors(query)

    # Return the generated colors as a JSON response
    return {"colors": colors}

# Flask route for the home page
@app.route("/")
def index():
    # Render and return the home page template (index.html)
    return render_template("index.html")

# Check if the script is run as the main program
if __name__ == '__main__':
    # Run the Flask app with debug mode enabled for development purposes
    app.run(debug=True)