pipeline {
   agent {
      docker {image 'django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            apt-get install python-django-crispy-forms
            cd Parks
            python manage.py test
            '''
         }

      }
   }


}

