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
           step{[$class: 'Mailer', notifyEveryUnstableBuild: true, recipients: 'arthur1801@outlook.com', sendToIndividuals: true]}

        }
    }
}

