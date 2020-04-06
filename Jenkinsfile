pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            . $VENV/bin/activate
            python3 Parks/manage.py test
            '''
         }

      }
   }


}

