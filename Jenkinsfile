pipeline {
	agent any
	stages {
		stage('Sonarqube') {
                  	environment {
                       		scannerHome = tool 'sonar-scanner'
                       	}
                	steps {
                   		withSonarQubeEnv('SonarQubeChatApp') {
                       		sh "${scannerHome}/bin/sonar-scanner"
                   		}
                   		timeout(time: 5, unit: 'MINUTES') {
                       		waitForQualityGate abortPipeline: true
				}
                	}
                }
		stage('Clone Repository') {
			steps {
				sh ''' #! /bin/bash
				ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/id_rsa ubuntu@18.217.180.181 '
                                sudo rm -rf FastApi
				'
				scp -r /var/lib/jenkins/workspace/FastApi ubuntu@18.217.180.181:
				'''
			}
		}
		stage('Build Image') {
			steps {
				sh ''' #! /bin/bash
				ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/.ssh/id_rsa ubuntu@18.217.180.181 '
				cd FastApi
				docker-compose up -d --build
				'
				'''
			}
		}

	}
	
}
