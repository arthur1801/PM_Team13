pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            sudo apt install python3-pip
            pip3 install Django
            python3 Parks/manage.py test
            '''
         }

      }
   }


}

