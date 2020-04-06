pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            virtualenv 
            python3 Parks/manage.py test
            '''
         }

      }
   }


}

