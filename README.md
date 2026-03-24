# Students-performance-predictor

### What the project does :-  
The student performance predictor predicts how well a student will perform based on factors like attendance, previous grades, study hours, and class participation. It predicts the student's marks and then classifies the result as a Pass or Fail , using a Linear Regression model. The passing marks for a student is set at 40 marks. This project shows how machine learning works by preparing the data, training the model, making predictions, and deciding if students pass or fail based on those predictions.

### Features :-  
Predicts students' marks based on their attendance, previous grades, study hours, and participation.  
Classifies students as Pass or Fail based on predicted marks with a threshold of 40 marks.  
Uses Linear Regression to model the relationship between the features and the target (marks).  
Scales features using StandardScaler for better model performance.  
### Technologies Used :-  
Python 3.X  
pandas: For data manipulation and analysis.  
numpy: For numerical computations.  
scikit-learn: For machine learning algorithms and preprocessing.  
matplotlib (Optional): For visualization (if added later).  

### How to set up the project :-  
To get this project up and running on your local machine, follow these steps:  
Clone the Repository  
1) First, clone the project to your local machine:  
   git clone https://github.com/your-username/student-performance-prediction.git

2) Navigate to the Project Folder  
   Go into the project directory:  
   cd student-performance-prediction  

3) Create a Virtual Environment (Optional but recommended)  
   It’s a good practice to create a virtual environment to manage dependencies:
   python -m venv venv

4) Activate the Virtual Environment  

   On Windows:  
   .\venv\Scripts\activate

   On macOS/Linux:  
   source venv/bin/activate

5) Install the Dependencies  
   Install all the required libraries:  
   pip install -r requirements.txt  

6) Run the Script  
   Once everything is set up, run the main Python script:  
   python student_performance_prediction.py  

This will start the model, make predictions, and classify students as "Pass" or "Fail" based on the predicted marks.

### How to Run the Project :-  
Ensure that the dependencies are installed.  

In the project folder, run the Python script:  

python student_performance_prediction.py  
1) The script will:  
2) Load the dataset.  
3) Train a Linear Regression model to predict students' marks.  
4) Use a threshold of 40 to classify students as Pass or Fail.  
5) Print the predicted marks and the classification for each student.  
