pipeline {
   agent {
      docker {image 'django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            python -m pip install --user --upgrade pip
            cd Parks
            python manage.py test
            '''
         }

      }
   }


}

