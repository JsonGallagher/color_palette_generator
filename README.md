# Color Palette Generator

## Overview

This project is an interactive color palette generator that uses a web-based form to accept text prompts for creating primary color palettes. It's designed to generate color palettes that align with specific themes, moods, or instructions provided by the user. Once generated, the colors are displayed on the website, allowing for quick and easy copying of HEX values.

## App Preview

Here's a look at the app in action:

## Desktop Web Preview

![Desktop Web preview](images/app-image-desktop.png)

## Mobile Web Preview

<img src="images/app-image-mobile.png" style="width: 50%;" alt="Mobile Web preview">

## Features

- **Interactive Web Form**: Input your color palette prompt through a simple web form interface.
- **Generate Color Palettes**: Create sets of colors that match your specified themes, moods, or instructions.
- **Browser Display**: View the generated color palette directly on the website.
- **Copy HEX Values**: Conveniently copy the HEX values of the generated colors for use in your design projects.

## How to Use

1. **Enter a Prompt**: Navigate to the website and type your color palette prompt into the provided form.
2. **Generate Palette**: Submit the form to generate a color palette based on your prompt.
3. **View and Copy Colors**: The generated colors will be displayed on the website. You can easily copy the HEX values of these colors by clicking or tapping on them.

## Installation

To set up this project for development or local use, follow these steps:

1. Clone the repository and navigate to the directory:
   - `git clone [your-repo-url]`
   - `cd [your-repo-directory]`

2. Create a `.env` file in the root directory of the project:
   - OPENAI_API_KEY='YOUR KEY GOES HERE'
3. Replace 'YOUR KEY GOES HERE' with your actual OpenAI API key.
4. Navigate to the root directory in your terminal
    - Run `source env/bin/activate`
5. Start flask server
    - `flask run` (--debug optional)

## Contributing

Contributions to this project are welcome!

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Acknowledgements

This project is based off a tutorial offered by Colt Steele on Udemy called Mastering OpenAI Python APIs: Unleash ChatGPT and GPT4
<https://www.udemy.com/course/mastering-openai/>
