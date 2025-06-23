pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mik0war/devOps.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m pytest tests/ -v'
            }
        }
        stage('Run Flask Server') {
            steps {
                sh 'python app.py &'  # Запуск в фоне (для теста)
                sleep(time: 5, unit: 'SECONDS')  # Ждем запуска сервера
                sh 'curl http://localhost:5000'   # Проверяем ответ
            }
        }
    }
    post {
        always {
            sh 'pkill -f "python app.py"'  // Останавливаем Flask после тестов
        }
    }
}