pipeline { 
  agent any 
  triggers {
    cron('1 0 * * *')
  }
  stages { 
    stage("Compile") { 
      steps { 
        //pip install requirements.txt 
        echo "Python compile done" 
      } 
    } 
    stage("Unit test") { 
      steps {
        sh "python Test_Case.py" 
          } 
        } 
      } 
    } 
