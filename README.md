create env
'''bash
 conda create -n wineq python=3.7 -y
 '''

 activate env
 ''' bash 
 conda activate wineq
 '''

 created requirements 

  created requirements 
  '''bash 
  pip install -r requirements.txt
  '''
  create template.py file wich consist all project structure
  create necessary dirs and files 

  download the data from 
  https://drive.google.com/drive/u/2/folders/112a_LzvZk5WlLeBU9oPbqHrtEHIKF5TN

''' bash 
  git init 
  '''
'''bash 
  dvc init 
  '''

tracking our given data 
  ''' bash 
  dvc add  data_given\winequality.csv
  ''' 

''' bash
 git add .
 '''
''' bash
 git commit -m "first commit"
 '''
 




