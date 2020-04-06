pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            . venv/bin/activate
            python3 Parks/manage.py test
            '''
         }

      }
   }


}

