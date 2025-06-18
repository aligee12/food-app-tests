pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "food-app-selenium-tests"
        TEST_URL = "http://16.171.54.54:3000"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aligee12/food-app-tests.git', branch: 'main'
            }
        }

        stage('Clean Previous Docker Image') {
            steps {
                script {
                    // Remove existing image (if it exists) before building a new one
                    sh '''
                        if docker image inspect ${DOCKER_IMAGE} > /dev/null 2>&1; then
                            docker rmi -f ${DOCKER_IMAGE}
                        fi
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker run --rm -e TEST_URL=${TEST_URL} ${DOCKER_IMAGE}'
                }
            }
        }
    }
    post {
        always {
            emailext (
                subject: "Jenkins Pipeline Test Results",
                body: "Test stage completed. Check Jenkins for details.",
                to: "${env.GIT_COMMITTER_EMAIL}",
                attachLog: true
            )
        }
    }
}
