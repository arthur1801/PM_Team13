pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            Pip install django-jenkins
            python Parks/manage.py test
            '''
         }

      }
   }


}

