pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    triggers {
        cron('H/5 * * * *')
    }

    parameters {
        choice(
            name: 'CENARIO',
            choices: ['SUCESSO', 'FALHA_COMPILACAO', 'TESTE_INSTAVEL'],
            description: 'Versao do fonte usada por este build.'
        )
        booleanParam(
            name: 'COBERTURA',
            defaultValue: false,
            description: 'Gera relatorios de cobertura para o cenario bonus.'
        )
    }

    stages {
        stage('Checkout do GitHub') {
            steps {
                deleteDir()
                checkout scm
            }
        }

        stage('Preparar ambiente') {
            steps {
                sh '''
                    set -eu
                    python3 -m venv .venv-jenkins
                    .venv-jenkins/bin/python -m pip install -r requirements-dev.txt
                    mkdir -p area_build relatorios

                    case "$CENARIO" in
                        SUCESSO)
                            cp conversor.py area_build/conversor.py
                            ;;
                        FALHA_COMPILACAO)
                            cp cenarios/falha_compilacao/conversor.py area_build/conversor.py
                            ;;
                        TESTE_INSTAVEL)
                            cp cenarios/falha_teste/conversor.py area_build/conversor.py
                            ;;
                        *)
                            echo "Cenario desconhecido: $CENARIO" >&2
                            exit 2
                            ;;
                    esac
                '''
            }
        }

        stage('Build (validar sintaxe)') {
            steps {
                sh '.venv-jenkins/bin/python -m py_compile area_build/conversor.py'
            }
        }

        stage('Testes') {
            steps {
                // Uma falha nos testes deixa o build UNSTABLE, como pede a tarefa.
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh '''
                        cd area_build
                        ../.venv-jenkins/bin/python -m pytest ../tests \
                            -v --rootdir=. --import-mode=importlib \
                            --junitxml=../relatorios/testes.xml
                    '''
                }
            }
        }

        stage('Cobertura') {
            when {
                expression { return params.COBERTURA }
            }
            steps {
                sh '''
                    cd area_build
                    ../.venv-jenkins/bin/python -m pytest ../tests \
                        --rootdir=. --import-mode=importlib \
                        --cov=conversor \
                        --cov-report=term-missing \
                        --cov-report=xml:../relatorios/cobertura.xml \
                        --cov-report=html:../relatorios/cobertura-html
                '''
                archiveArtifacts(
                    artifacts: 'relatorios/cobertura.xml,relatorios/cobertura-html/**',
                    fingerprint: true
                )
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'relatorios/testes.xml'
        }
        success {
            echo 'Build e testes concluidos com sucesso.'
        }
        unstable {
            echo 'O fonte compilou, mas pelo menos um teste falhou.'
        }
        failure {
            echo 'O build falhou. Consulte o estagio destacado em vermelho.'
        }
    }
}
