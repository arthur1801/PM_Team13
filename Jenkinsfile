pipeline {
   agent {
      docker {image 'django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            cd Parks
            python manage.py runserver test
            '''
         }

      }
   }


}

