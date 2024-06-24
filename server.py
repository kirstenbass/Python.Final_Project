"""
This module will enable customers to access this application on the web.
"""

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection import emotion_detection

# Instantiate the app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    This function will take a text input from a user interface and
    pass back the emotion score of that text input.
    """
    # Pass in textToAnalyze
    text_to_analyze = request.args.get('textToAnalyze')
    # Use emotion_detector() function to output the highest detected emotion
    dominant_emotion = emotion_detection.emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    anger = dominant_emotion['anger']
    disgust = dominant_emotion['disgust']
    fear = dominant_emotion['fear']
    joy = dominant_emotion['joy']
    sad = dominant_emotion['sadness']
    max_emotion = dominant_emotion['max_emotion']
    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
            f"'sadness': {sad}. "
            f"The dominant emotion is {max_emotion}")

@app.route("/")
def render_index_page():
    """
    This function will render the user interface
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
