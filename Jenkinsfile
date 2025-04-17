pipeline{
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Angelic203/RCB.git', branch:'main'
            }
        }

        // stage('Install Dependencies') {
        //     steps {
        //         bat '''
                
        //         call venu\\Script\\activate
        //         pip install --upgrade pip
        //         pip install -r requirement.txt
        //         '''
        stage('Install Dependencies') {
            steps {
                bat '''
                python --version
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venu\\Scripts\\activate
                pytest test.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'

                bat '''
                    call venv\\Scripts\\activate
                    python add.py
                    '''
            }
        }
    

        post {
            success {
                echo 'Pipeline succeeded!'
            }
            failure {
                echo 'Pipeline failed!'
            }
        }
    }
}

