SMS Spam Detection Project
Project Overview
This project is an SMS Spam Detection application. It uses natural language processing (NLP) techniques and machine learning models to classify SMS messages as either Spam or Ham (not spam). The web application is built with Streamlit, providing a simple and interactive interface where users can input a message to check if it's spam or not.

Project Features
Input Text Box: Enter an SMS message to check whether it's spam or ham.
Spam Detection: The model processes the input message and outputs whether it is spam or not.
Machine Learning Models: Utilizes Multinomial Naive Bayes as the classifier, trained on a dataset of SMS messages.
Interactive Visualization: Displays statistics about the dataset and visualizes frequently used words in spam and ham messages.
Demo
If you want to try the project locally, follow the instructions below to set up and run it on your machine.

Setup Instructions
Prerequisites
Ensure you have the following installed on your local machine:

Python 3.7+
Streamlit (for building the web interface)
Scikit-learn (for the machine learning models)
Numpy and Pandas (for data manipulation)
Matplotlib and Seaborn (for data visualization)
NLTK (for natural language processing)
You can install the required libraries by running:


pip install -r requirements.txt
Installation
Clone the repository:


git clone https://github.com/yourusername/sms_spam_detection.git
cd sms_spam_detection
Download NLTK data (required for tokenizing words and removing stopwords):


python -m nltk.downloader punkt stopwords
Run the Streamlit application:

To run the app locally, use the command:


streamlit run app.py
This will open a browser window where you can interact with the SMS Spam Detection model.

File Descriptions
app.py: The main script that runs the Streamlit web application.
spam.csv: The dataset used for training the model.
model.pkl: The pre-trained model file (Multinomial Naive Bayes).
vectorizer.pkl: The saved TfidfVectorizer used to transform input text.
requirements.txt: Contains the list of dependencies required to run the project.
Project Structure
kotlin
Copy code
📦sms_spam_detection
 ┣ 📂data
 ┃ ┗ spam.csv
 ┣ 📂models
 ┃ ┣ model.pkl
 ┃ ┗ vectorizer.pkl
 ┣ 📜app.py
 ┣ 📜README.md
 ┣ 📜requirements.txt
Usage
Enter an SMS message in the text box.
Click on the "Check" button.
The app will display whether the message is Spam or Ham.
Example
Input:


Congratulations! You've won a $1,000 Walmart gift card. Go to http://bit.ly/abc123 to claim now.
Output:
Spam

Model Details
Text Preprocessing:
Lowercasing, removing non-alphanumeric characters, stopword removal, and stemming.
Feature Extraction:
Text data is converted into numeric features using TfidfVectorizer.
Classification Model:
The Multinomial Naive Bayes algorithm is used to classify messages.
Visualizations
The app also provides visualizations to show:

The distribution of Spam and Ham messages.
Word frequency counts for Spam and Ham.
Future Improvements
Deployment: Deploy the project to a cloud platform like Heroku or Streamlit sharing for public access.
Additional Models: Incorporate other machine learning algorithms like Random Forest or SVM to improve performance.
License
This project is licensed under the MIT License - see the LICENSE file for details.
