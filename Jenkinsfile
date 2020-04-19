pipeline {
   agent {
      docker {image 'wildfish/django'}
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

