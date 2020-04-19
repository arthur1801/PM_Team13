pipeline {
   agent {
      docker {image 'python:3-alpine'}
   }

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            python -c "import django; print(django.get_version())"
            '''
         }

      }
   }


}

