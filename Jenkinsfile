pipeline {
   agent {
      docker {image 'python:3-alpine'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            source venv/bin/activate
            pyrhon3.8 --version
            '''
         }

      }
   }


}

