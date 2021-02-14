# Fall-Detection-System
A fall detection system to assist elderly people when they suffer accidental falls using fog computing architecture and machine learning based approach

# Steps to execute
1. Execute Data_Cleaning.py. The .txt files from Sisfall_Dataset will be modified for 1 accelerometer and gyroscope reading along with magnitude(euclidean norm) computed and timestamp attached for each sample. The output will be stored in csv format in the folder created in step 1.
```
python Data-Cleaning.py
```
2. Run Features.py in order to extract the features for each activity using partially overlapping sliding window technique. The window size and overlap can be adjusted using slot function. The output will be stored in Extracted_Features.csv. The first column is the label for target variable, i.e. 0-Daily Activity and 1-Fall.
```
python Feature\ Extraction/Features.py
```
3. Run the classfication algorithm after tuning the hyperparameters and observe the results.
```
python Classification\ Algorithms/Randomforest.py
```
```
python Classification\ Algorithms/Support\ Vector\ Machine\ \(SVM\).py
```
Note - The paths mentioned are relative to your working folder
