class Denuncia:
    
    def __init__(self, cpf_motorista, cpf_passageiro, textDenuncia):
        self.passageiro_cpf = cpf_motorista
        self.motorista_cpf = cpf_passageiro
        self.textDenuncia = textDenuncia