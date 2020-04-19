pipeline {
   agent {
      docker {image 'davidj/django-production-py3'}
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

