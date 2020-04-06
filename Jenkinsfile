pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            source venv/bin/activate
            pip install Django
            python3 Parks/manage.py test
            '''
         }

      }
   }


}

