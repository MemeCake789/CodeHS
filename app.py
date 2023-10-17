from flask import Flask, render_template
import tkinter as tk
import tempfile
import webbrowser

app = Flask(__name__)

@app.route('/')
def hello():
		# Create and display the Tkinter window
		window = tk.Tk()
		canvas = tk.Canvas(window, width=400, height=400)
		canvas.pack()

		rectangle = canvas.create_rectangle(50, 50, 200, 150, fill="red")
		oval = canvas.create_oval(250, 50, 350, 150, fill="blue")
		line = canvas.create_line(50, 250, 350, 250)

		# Save the image as a temporary file
		temp_file = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
		canvas.postscript(file=temp_file.name, colormode="color")

		# Close the Tkinter window
		window.destroy()

		# Render the temporary HTML file
		return render_template('index.html', image_path=temp_file.name)

if __name__ == '__main__':
		app.run(debug=True)
