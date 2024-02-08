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
    # Prepare the prompt content for the API call
    prompt = f"""
    You are a highly consistent color palette generating assistant. Respond only in a JSON array format of hexadecimal color codes. Generate 1 color palette that fits the theme, mood, or instructions in the prompt. If a specific number of colors is requested in the prompt, return that number of colors, otherwise return exactly 8 colors in the palette.

    Example prompt and response:
    Prompt: Ocean sunrise
    Response: ["#FF5733", "#FFC300", "#FF5733", "#FF5733", "#C70039"]

    Text: {msg}
    """

    # Make the API call to the OpenAI service
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo-1106",
        max_tokens=200
    )
    raw_response = response.choices[0].message.content
    print(f"Raw API response: {raw_response}")  # Solution 2: Debugging the actual content

    # Solution 1: Clean up the response content
    clean_response = raw_response.replace("Response: ", "").strip()

    # Attempt to parse the cleaned response
    try:
        colors = json.loads(clean_response)
        if not isinstance(colors, list) or not all(isinstance(color, str) and color.startswith('#') for color in colors):
            raise ValueError("Response format is incorrect")
        return colors
    except (ValueError, json.JSONDecodeError) as e:
        app.logger.error(f"Error parsing the API response: {e}")
        print(f"Error parsing the API response: {e}")
        return ["#FFFFFF", "#CCCCCC", "#999999"]


# Flask route handling for generating color palettes
@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    # Retrieve the user's query from the JSON body of the request
    data = request.get_json()  # This method parses the JSON request body
    query = data.get("query")  # Access the 'query' attribute from the parsed JSON

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