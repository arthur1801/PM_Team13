pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
           echo "Hello !!!"
            sh '''
            virtualenv myenv
            source myenv/bin/activate
            pip install Django
            python3 Parks/manage.py test
            '''
         }

      }
   }


}

