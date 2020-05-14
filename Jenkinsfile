pipeline {
   agent { dockerfile true }

   stages {
      stage('Test') {
         steps {
           
            sh '''
            cd Parks
            python manage.py test 
            '''
         }
      }
      
   }

      stages {
      stage('Code rating') {
         steps {
           
            sh '''
            cd Parks
            pylint --disable=W0622,W0611,F0401,R0914,W0221,W0222,W0142,F0010,W0703,R0911,C0415,C0116 -f parseable Parkapp/*
            '''
         }
      }
      
   }
      
   
   post {
       failure  {
          emailext body: 'Team 13 pipline failure', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], to:'arthuvi@ac.sce.ac.il , shako1@ac.sce.ac.il, shahaas@ac.sce.ac.il'  ,subject: 'Fix your code!!!!'
       }
   }
}

