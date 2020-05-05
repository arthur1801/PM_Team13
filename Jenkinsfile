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
       failure  {
          emailext body: 'Team 13 pipline failure', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], to:'arthuvi@ac.sce.ac.il , arthur1801@outlook.com'  ,subject: 'Fix your code!!!!'
       }
       always {
           emailext body: 'Team 13 pipline failure', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], to:'arthuvi@ac.sce.ac.il , arthur1801@outlook.com'  ,subject: 'Fix your code!!!!'
       }
   }
}

