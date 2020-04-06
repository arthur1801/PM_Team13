pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            python -m pip install django
            python Parks/manage.py test
            '''
         }

      }
   }


}

