class Conta:
    """
    Classe que representa uma Conta Bancária.

    Attributes:
        titular (str): Nome do titular da conta.
        saldo (float): Saldo atual da conta.
        cpf (str): CPF do titular.
        endereco (str): Endereço do titular.
        telefone (str): Número de telefone do titular.
        agencia (str): Número da agência bancária.
        numero_conta (str): Número da conta bancária.
        tipo_conta (str): Tipo da conta (por exemplo, poupança ou corrente).
        data_abertura (str): Data de abertura da conta.
        ativa (bool): Indica se a conta está ativa ou não.

    Methods:
        __init__(titular, cpf, endereco, telefone, agencia, numero_conta, tipo_conta, saldo_inicial=0.0)
            Inicializa uma nova conta bancária.

        deposit(valor)
            Deposita uma quantia na conta.

        withdraw(valor)
            Realiza um saque da conta.

        get_balance()
            Retorna o saldo atual da conta.
    """

    def __init__(self, titular, cpf, endereco, telefone, agencia, numero_conta, tipo_conta, saldo_inicial=0.0):
        """
        Inicializa uma nova conta bancária.

        Args:
            titular (str): Nome do titular da conta.
            cpf (str): CPF do titular.
            endereco (str): Endereço do titular.
            telefone (str): Número de telefone do titular.
            agencia (str): Número da agência bancária.
            numero_conta (str): Número da conta bancária.
            tipo_conta (str): Tipo da conta (por exemplo, poupança ou corrente).
            saldo_inicial (float, opcional): Saldo inicial da conta. Padrão é 0.0.
        """
        self.titular = titular
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo = saldo_inicial
        self.data_abertura = "XX/XX/XXXX"  # Preencha com a data real de abertura
        self.ativa = True

    def deposit(self, value):
        """
        Deposita uma quantia na conta.

        Args:
            value (float): Valor a ser depositado na conta.

        Returns:
            str: Mensagem indicando o sucesso ou falha da operação.
        """
        if value > 0:
            self.saldo += value
            return f'Depósito de R${value:.2f} realizado com sucesso.'
        else:
            return 'O valor do depósito deve ser positivo.'

    def withdraw(self, value):
        """
        Realiza um saque da conta.

        Args:
            value (float): Valor a ser sacado da conta.

        Returns:
            str: Mensagem indicando o sucesso ou falha da operação.
        """
        if 0 < value <= self.saldo:
            self.saldo -= value
            return f'Saque de R${value:.2f} realizado com sucesso.'
        else:
            return 'Saldo insuficiente ou valor inválido de saque.'

    def get_balance(self):
        """
        Retorna o saldo atual da conta.

        Returns:
            str: Mensagem contendo o saldo atual da conta.
        """
        return f'Saldo atual: R${self.saldo:.2f}'
