pipeline {
   agent {
      docker {image 'tatianno/django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            cd Parks
            python manage.py test Parks.tests.testing
            '''
         }

      }
   }


}

