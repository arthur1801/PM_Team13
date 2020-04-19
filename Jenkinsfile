pipeline {
   agent {
      docker {image 'python:3-alpine'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            cd venv
            source bin/activate
            bin/pip install -r requirements.txt
            '''
         }

      }
   }


}

