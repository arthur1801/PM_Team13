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
            venv/bin/pip3.8 install django
            cd Parks
            python3.8 manage.py runserver test
            '''
         }

      }
   }


}

