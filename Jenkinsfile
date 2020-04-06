pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            python Parks/manage.py test
            '''
         }

      }
   }


}

