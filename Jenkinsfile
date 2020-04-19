pipeline {
   agent {
      docker {image 'python:3-alpine'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            sudo python -m pip install Django
            '''
         }

      }
   }


}

