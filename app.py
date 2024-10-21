import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__, template_folder='.')  # Set current folder for templates
SAVE_DIRECTORY = 'saved_files'  # Directory where files will be saved

@app.route('/')
def index():
    # List all Markdown files in the save directory
    files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith(('.md', '.txt'))]
    return render_template('index.html', files=files)  # No need to specify subfolder

@app.route('/save', methods=['POST'])
def save_file():
    filename = request.form.get('filename')
    markdown_content = request.form.get('markdown_content')
    fileformat = request.form.get('fileformat')  # Get selected file format

    if filename and markdown_content:
        # Determine the file extension based on the selected format
        if fileformat == 'md':
            extension = '.md'
        elif fileformat == 'txt':
            extension = '.txt'
        else:
            return "Invalid file format!", 400

        # Save the file with the appropriate extension
        with open(os.path.join(SAVE_DIRECTORY, f"{filename}{extension}"), 'w') as file:
            file.write(markdown_content)
        return index()  # Redirect back to the index page after saving
    else:
        return "Filename and content are required!", 400

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        file_path = os.path.join(SAVE_DIRECTORY, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return index()  # Redirect back to the index page after deletion
        else:
            return f"File {filename} not found!", 404
    except Exception as e:
        return str(e), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(SAVE_DIRECTORY, filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)  # Create the save directory if it doesn't exist
    app.run(debug=True)
