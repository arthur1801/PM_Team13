pipeline {
   agent {
      docker {image 'python:3-alpine'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            virtualenv -p python3 myenv
            source myenv/bin/activate
            pip3 install -r requirements.txt
            '''
         }

      }
   }


}

