pipeline {
   agent {
      docker {image 'python:3-alpine'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            source venv/bin/activate
            venv/bin/pip install django
            cd Parks
            python3.8 manage.py runserver test
            '''
         }

      }
   }


}

