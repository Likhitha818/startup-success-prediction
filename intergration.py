from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data and convert to appropriate types
        relationships = float(request.form['relationships'])
        funding_rounds = float(request.form['funding_rounds'])
        funding_total_usd = float(request.form['funding_total_usd'])
        milestones = float(request.form['milestones'])
        avg_participants = float(request.form['avg_participants'])

        # Prepare the data for prediction
        data = [[relationships, funding_rounds, funding_total_usd, milestones, avg_participants]]

        # Load the model and make predictions
        model = pickle.load(open('prediction.pkl', 'rb'))
        prediction = model.predict(data)[0]

        # Check for invalid data
        if relationships <= 0 or funding_rounds <= 0 or funding_total_usd <= 0 or milestones <= 0 or avg_participants <= 0:
            prediction = 'PLEASE GIVE VALID DATA'
        elif milestones < 4:
            prediction = 'Our Prediction says that your startup might fail, as milestones are too few. Please try to increase them, and you may succeed.'
        elif relationships < 4:
            prediction = 'Our Prediction says that your startup might fail, as relationships are insufficient. Start building more relationships to improve your chances.'
        elif funding_rounds < 4:
            prediction = 'Our Prediction says that your startup might fail due to fewer funding rounds. Increase the number of funding rounds for better success.'
        elif funding_total_usd < 50000:
            prediction = 'Our Prediction says that your startup might fail due to insufficient funding. Try to secure more rounds to increase the total amount.'
        else:
            prediction = 'Our Prediction says that your startup is likely to be a success.'

        # Render the result back to the form
        return render_template('index.html', 
                               prediction=prediction, 
                               relationships=relationships, 
                               funding_rounds=funding_rounds, 
                               funding_total_usd=funding_total_usd, 
                               milestones=milestones, 
                               avg_participants=avg_participants)

if __name__ == '__main__':
    app.run(debug=True)
