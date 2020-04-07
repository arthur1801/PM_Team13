pipeline {
   agent {docker {image 'python:3-alpine'}}

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

