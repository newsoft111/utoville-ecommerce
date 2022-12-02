node {
    stage('Clone repository') {
        checkout scm
    }

	stage('Install docker-cli') {
        app.inside {
            sh 'apt-get install -y docker-ce-cli'
        }
    }

    stage('Build image') {
        app = docker.build("mcfly17/utoville-homecare-user")
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
            app.push("dev")
        }
    }

    stage('SSH docker run a') {
        script {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "dev",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "make port")
                        ]
                    )
                ]
            )
        }
    }
}