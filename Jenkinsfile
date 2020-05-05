pipeline {
   agent {
      docker {image 'tatianno/django'}
   }

   stages {
      stage('Build') {
         steps {
           
            sh '''
            cd Parks
            python manage.py test Parkapp.tests.testing
            '''
            echo "success!!!"
         }

      }
   }
   
   post {
       always {
           emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
       }
   }
}

