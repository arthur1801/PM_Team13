pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            python3.8 Parks/manage.py test
            '''
         }

      }
   }


}

