from flask import Flask, request, jsonify
import pickle

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Create a Flask app instance
app = Flask(__name__)

# AQI Classification Function
def classify_aqi(aqi):
    if aqi <= 50:
        return {
            "Quality Classification": "Minimal Impact",
            "Remarks": "Good",
            "Background Color": "#e8f5e9"  # Green
        }
    elif 51 <= aqi <= 100:
        return {
            "Quality Classification": "Minor breathing discomfort to sensitive people",
            "Remarks": "Satisfactory",
            "Background Color": "#fff9c4"  # Yellow
        }
    elif 101 <= aqi <= 200:
        return {
            "Quality Classification": "Breathing discomfort to people with lung, heart disease, children, and older adults",
            "Remarks": "Moderate",
            "Background Color": "#ffcc80"  # Orange
        }
    elif 201 <= aqi <= 300:
        return {
            "Quality Classification": "Breathing discomfort to people on prolonged exposure",
            "Remarks": "Poor",
            "Background Color": "#ffab91"  # Red
        }
    elif 301 <= aqi <= 400:
        return {
            "Quality Classification": "Respiratory illness to people on prolonged exposure",
            "Remarks": "Very Poor",
            "Background Color": "#d50032"  # Purple
        }
    else:
        return {
            "Quality Classification": "Respiratory effects even on healthy people",
            "Remarks": "Severe",
            "Background Color": "#b71c1c"  # Maroon
        }

# Create a route for root
@app.route("/", methods=["GET"])
def root():
    return """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AQI Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background-color: #f4f4f9;
        }
        .container {
            width: 90%;
            max-width: 900px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            width: 100%;
            margin-top: 30px;
            border-collapse: collapse;
        }
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .std-value {
            font-size: 0.8em;
            color: #666;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 18px;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 20px;
            color: #333;
            border-radius: 4px;
            text-align: center;
            font-size: 20px;
        }
        .result .classification {
            font-weight: bold;
        }
        .result .remarks {
	    font-weight: bold;
        }
        .tableau-container {
            display: flex;
            justify-content: center;
            margin-top: 50px;
        }
        .tableau-embed {
            width: 90%;
            max-width: 1000px;
            height: 800px;
        }
    </style>
    <script>
        async function submitForm(event) {
            event.preventDefault(); // Prevent form from submitting normally
            const form = event.target;
            const formData = new FormData(form);
            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });
            const result = await response.json();
            const prediction = result.prediction.toFixed(2);
            const classification = result.classification;
            const color = classification["Background Color"];

            const resultDiv = document.getElementById("predictionResult");
            resultDiv.innerHTML = `
                <div class="classification">Predicted Air Quality Index (AQI): ${prediction}</div>
                <div class="classification">Quality Classification: ${classification["Quality Classification"]}</div>
                <div class="remarks">Remarks: ${classification["Remarks"]}</div>
            `;
            resultDiv.style.backgroundColor = color;
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Air Quality Prediction</h1>
        <form id="predictionForm" onsubmit="submitForm(event)">
            <table>
                <thead>
                    <tr>
                        <th>Pollutant</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>SO2 <br><span class="std-value">STD VALUE: 80 µg/m³</span></td>
                        <td><input name="so2" type="number" step="0.01" required /></td>
                    </tr>
                    <tr>
                        <td>NOx <br><span class="std-value">STD VALUE: 80 µg/m³</span></td>
                        <td><input name="nox" type="number" step="0.01" required /></td>
                    </tr>
                    <tr>
                        <td>RSPM <br><span class="std-value">STD VALUE: 120 µg/m³</span></td>
                        <td><input name="rspm" type="number" step="0.01" required /></td>
                    </tr>
                    <tr>
                        <td>SPM <br><span class="std-value">STD VALUE: 360 µg/m³</span></td>
                        <td><input name="spm" type="number" step="0.01" required /></td>
                    </tr>
                </tbody>
            </table>
            <button type="submit">Predict</button>
        </form>
        <div id="predictionResult" class="result"></div>
    </div>
    <h1>AQI Analysis Visualization</h1>
    <div class="tableau-container">
        <div class='tableauPlaceholder tableau-embed' id='viz1722800786554' style='position: relative'>
            <noscript>
                <a href='#'>
                    <img alt=' ' src='https://public.tableau.com/static/images/AQ/AQIPredictionProject/YearlyAQITrendsbyCity/1_rss.png' style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='AQIPredictionProject/YearlyAQITrendsbyCity' />
                <param name='tabs' value='yes' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https://public.tableau.com/static/images/AQ/AQIPredictionProject/YearlyAQITrendsbyCity/1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1722800786554');
            var vizElement = divElement.getElementsByTagName('object')[0];
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
    </div>
</body>
</html>
"""
@app.route("/predict", methods=["POST"])
def predict():
    # Retrieve values from user input
    so2 = float(request.form.get("so2", 0))
    nox = float(request.form.get("nox", 0))
    rspm = float(request.form.get("rspm", 0))
    spm = float(request.form.get("spm", 0))

    # Predict the AQI using the model
    input_features = [[so2, nox, rspm, spm]]
    prediction = model.predict(input_features)[0]

    # Classify the AQI
    classification = classify_aqi(prediction)

    return jsonify(prediction=prediction, classification=classification)

# Start the server on port 4000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

