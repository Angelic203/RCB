pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Angelic203/RCB.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                  call venv\\Scripts\\activate
                  pytest test.py
              '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'

                bat '''
                    call venv\\Scripts\\activate
                    C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe add.py
                '''
            }
        }
    }

   
