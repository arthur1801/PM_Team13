pipeline {
   agent {
      docker {image 'camandel/django-wiki'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            cd Parks
            python3.8 manage.py test
            '''
         }

      }
   }


}

