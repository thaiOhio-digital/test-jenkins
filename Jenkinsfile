pipeline {
    agent any
    stages {
        stage('Clone') {
            steps (
                git branch: 'main', url: 'https://github.com/thaiOhio-digital/test-jenkins.git'
            )
        }
    }
}