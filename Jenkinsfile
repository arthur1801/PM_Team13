pipeline {
   agent {
      docker {image 'jandigarte/django'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            cd Parks
            python manage.py test
            '''
         }

      }
   }


}

