pipeline {
   agent {
      docker {image 'django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            pip install django-crispy-forms
            cd Parks
            python manage.py test
            '''
         }

      }
   }


}

