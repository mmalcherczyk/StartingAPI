pipeline {
    environment {
        imagename = "sl1god/fastapi"
        registryCredential = "sl1god"
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
                    dockerImage = docker.build imagename
                }
            }
        }
        stage("Deploy Docker Image") { 
            steps {
                script {
                    docker.withRegistry( ' ', registryCredential ) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
}
