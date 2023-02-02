from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def principal():
    mislenguages=("hola", "como", "va", "putos")
    return render_template('index.html', lenguajes=mislenguages)
   


if __name__== '__main__':
    app.run(debug=True, port=5000)



