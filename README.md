# Students-performance-predictor

### What the project does :-  
The student performance predictor is a tool that tells us how well a student will do in their studies,it takes into consideration factors like attendance,previous marks,studyhours etc,the student performance predictor then guesses what marks the student will get and says if they pass or fail. It uses Linear Regression to guess wheter student is pass or fail,to pass a student needs to get least 40 marks,and it uses the concept of machine learning.

### Features :-  
This model using features like attendance,previous marks,studyhours etc predicts students marks.  
Then using predicted marks students are classified as pass or fail bu sing 40 marks criteria.  
This model uses linear regression to make relationship between the features and the target (marks).  
For better model performance it uses stabdarscaler to scale features.  
### Technologies Used :-  
Python 3.X  
pandas: For data manipulation and analysis.  
numpy: For numerical computations.  
scikit-learn: For machine learning algorithms and preprocessing.  
matplotlib (Optional): For visualization (if added later).  

### How to set up the project :-  
To set up the up this project on your local computer follow the given steps :  
First Clone the Repository  
1) Clone the project on your local computer first by writing the following command on your computer :  
   git clone https://github.com/your-username/student-performance-prediction.git

2) Then navigate to the Project Folder  
   By Going into the project directory:  
   cd student-performance-prediction  

3) Create a Virtual Environment (Optional but recommended)  
   To manage dependencies it is beter to create virtual enviroment on your computer:
   python -m venv venv

4) On your computer activate the virtual Environment:    

   On Windows type this command:  
   .\venv\Scripts\activate

   On macOS/Linux type this command:  
   source venv/bin/activate

5) Install the Dependencies  
   Install all the required libraries:  
   pip install -r requirements.txt  

6) Run the Script  
   Now run the main python script , once everything is done:    
   python student_performance_prediction.py  

After these steps model will be started , it will make predictions on students marks and classify them as pass or fail

### How to Run the Project :-  
First ensure that all the dependencies which are mentioned above are installed in your computer  

Then in your project folder, run the given Python script:  

python student_performance_prediction.py  
1) Then this script will:    
2) First load the dataset.    
3) Then to predict student's marks it will train a linear regression model.    
4) Then it will classify students as pass or fail by using the criteria of 40.
5) It will then print for each student  the predicted marks and the pass and fail classification.
### Developed By:-  
Name: Atharav Balaji Khonde  
Registration no:- 25BAI10734
