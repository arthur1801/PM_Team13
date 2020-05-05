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
          emailext body: 'Team 13 pipline failure', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], to:'arthuvi@ac.sce.ac.il , shako1@ac.sce.ac.il, shahaas@ac.sce.ac.il'  ,subject: 'Fix your code!!!!'
       }
   }
}

