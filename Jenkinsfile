pipeline {
   agent {
      docker {image 'django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            pip3 install --user django-crispy-forms
            cd Parks
            python manage.py test
            '''
         }

      }
   }


}

