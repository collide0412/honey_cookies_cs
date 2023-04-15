from flask import Flask, request, render_template
from sklearn import feature_extraction, model_selection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the submitted URL from the form
        url = request.form['url']

        # Extract the features from the URL using your FeatureExtraction class
        features = feature_extraction(url).features

        # Make a prediction using the trained model
        prediction = model_selection.predict([features])[0]

        # Return the prediction to the user
        if prediction == 0:
            return render_template('index.html', result='The URL is legitimate')
        else:
            return render_template('index.html', result='The URL is phishing')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()