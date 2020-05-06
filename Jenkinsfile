pipeline {
   agent {
      docker {image 'tatianno/django'}
   }

   stages {
      stage('Test') {
         steps {
           
            sh '''
            cd Parks
            python manage.py test 
            '''
         }
      }
      
       
      stage ('Deploy To Prod'){
        input{
          message "Do you want to proceed for production deployment?"
        }
          steps {
                sh 'echo "Deploy into Prod"'
          }
        }
      
   }
      
      
   
   post {
       failure  {
          emailext body: 'Team 13 pipline failure', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], to:'arthuvi@ac.sce.ac.il , shako1@ac.sce.ac.il, shahaas@ac.sce.ac.il'  ,subject: 'Fix your code!!!!'
       }
   }
}

