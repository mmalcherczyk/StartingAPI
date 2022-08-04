pipeline {
    environment {
        registry = "sl1god/fastapi"
        registryCredential = "dockerhub_id"
        dockerImage = ''
    }
    agent any

    stages {

        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'docker --version'
                sh 'pip3 --version'
     
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            }
        }
        stage("Deploy Docker Image") { 
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage("Cleaning up") {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
