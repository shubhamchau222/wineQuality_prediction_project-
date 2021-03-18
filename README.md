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
first commit
''' bash
 git commit -m "first commit"
 '''

update Readme.md
''' bash
git add . && git commit -m "update Readme.md"
'''

create new  fresh repository on github 
and then 
…or push an existing repository from the command line
''' bash
git remote add origin https://github.com/shubhamchau222/ wineQuality_prediction_project-.git
'''

call the main branch 
''' bash
git branch -M main
'''

push entire code to the origin / main branch
'''bash 
git push -u origin main
'''






