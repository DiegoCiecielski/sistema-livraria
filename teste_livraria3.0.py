class Livro:
    def __init__(self, codigo, titulo, editora, categoria, ano, valor, estoque):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def __str__(self):
        return (f'>>>>>Cod#{self.codigo}\n'
                f'Título/Editora: {self.titulo}/{self.editora}\n'
                f'Categoria: {self.categoria}\n'
                f'Ano: {self.ano}\n'
                f'Valor: R${self.valor:.2f}\n'
                f'Estoque: {self.estoque} unidades\n'
                f'Valor total em estoque: R${self.valor * self.estoque:.2f}\n')

class Filial:
    def __init__(self, codigo, nome, endereco, contato):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.estoque = []

    def adicionar_livro(self, livro, quantidade):
        for item in self.estoque:
            if item['livro'].codigo == livro.codigo:
                item['quantidade'] += quantidade
                return
        self.estoque.append({'livro': livro, 'quantidade': quantidade})

    def listar_estoque(self):
        for item in self.estoque:
            livro = item['livro']
            print(f'>>>>>Cod#{livro.codigo}\n'
                  f'Título/Editora: {livro.titulo}/{livro.editora}\n'
                  f'Categoria: {livro.categoria}\n'
                  f'Ano: {livro.ano}\n'
                  f'Valor: R${livro.valor:.2f}\n'
                  f'Estoque: {item["quantidade"]} unidades\n'
                  f'Valor total em estoque: R${livro.valor * item["quantidade"]:.2f}\n')
        valor_total = sum(item['livro'].valor * item['quantidade'] for item in self.estoque)
        print(f'Valor total em estoque: R${valor_total:.2f}')

class Livraria:
    def __init__(self):
        self.filiais = {}
        self.livros = {}

    def criar_filial(self, codigo, nome, endereco, contato):
        if codigo not in self.filiais:
            self.filiais[codigo] = Filial(codigo, nome, endereco, contato)
            print(f'Filial {nome} criada com sucesso!')
        else:
            print('Código de filial já existente.')

    def carregar_estoque(self, arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as file:
                filial_atual = None
                for linha in file:
                    linha = linha.strip()
                    if linha.startswith('#'):
                        dados = linha[1:].split(',')
                        codigo = dados[0]
                        nome = dados[1]
                        endereco = dados[2]
                        contato = dados[3]
                        self.criar_filial(codigo, nome, endereco, contato)
                        filial_atual = self.filiais[codigo]
                    else:
                        if filial_atual:
                            dados = linha.split(',')
                            codigo = int(dados[0])
                            titulo = dados[1]
                            ano = int(dados[2])
                            categoria = dados[3]
                            editora = dados[4]
                            valor = float(dados[5].replace('R$', '').replace(',', '.'))
                            estoque = int(dados[6])
                            livro = self.livros.get(codigo)
                            if livro is None:
                                livro = Livro(codigo, titulo, editora, categoria, ano, valor, 0)
                                self.livros[codigo] = livro
                            filial_atual.adicionar_livro(livro, estoque)
            print('Estoque carregado com sucesso!')
        except FileNotFoundError:
            print('Arquivo não encontrado.')

    def listar_estoque_filial(self, codigo):
        if codigo in self.filiais:
            self.filiais[codigo].listar_estoque()
        else:
            print('Código de filial não encontrado.')

    def buscar_nome(self, nome, codigo_filial):
        if codigo_filial in self.filiais:
            filial = self.filiais[codigo_filial]
            for item in filial.estoque:
                livro = item['livro']
                if nome.lower() in livro.titulo.lower():
                    print(f'>>>>>Cod#{livro.codigo}\n'
                          f'Título/Editora: {livro.titulo}/{livro.editora}\n'
                          f'Categoria: {livro.categoria}\n'
                          f'Ano: {livro.ano}\n'
                          f'Valor: R${livro.valor:.2f}\n'
                          f'Estoque: {item["quantidade"]} unidades\n'
                          f'Valor total em estoque: R${livro.valor * item["quantidade"]:.2f}\n')
        else:
            print('Código de filial não encontrado.')

    def buscar_categoria(self, categoria, codigo_filial):
        if codigo_filial in self.filiais:
            filial = self.filiais[codigo_filial]
            for item in filial.estoque:
                livro = item['livro']
                if categoria.lower() in livro.categoria.lower():
                    print(f'>>>>>Cod#{livro.codigo}\n'
                          f'Título/Editora: {livro.titulo}/{livro.editora}\n'
                          f'Categoria: {livro.categoria}\n'
                          f'Ano: {livro.ano}\n'
                          f'Valor: R${livro.valor:.2f}\n'
                          f'Estoque: {item["quantidade"]} unidades\n'
                          f'Valor total em estoque: R${livro.valor * item["quantidade"]:.2f}\n')
        else:
            print('Código de filial não encontrado.')

    def buscar_preco(self, preco, codigo_filial):
        if codigo_filial in self.filiais:
            filial = self.filiais[codigo_filial]
            for item in filial.estoque:
                livro = item['livro']
                if livro.valor < preco:
                    print(f'>>>>>Cod#{livro.codigo}\n'
                          f'Título/Editora: {livro.titulo}/{livro.editora}\n'
                          f'Categoria: {livro.categoria}\n'
                          f'Ano: {livro.ano}\n'
                          f'Valor: R${livro.valor:.2f}\n'
                          f'Estoque: {item["quantidade"]} unidades\n'
                          f'Valor total em estoque: R${livro.valor * item["quantidade"]:.2f}\n')
        else:
            print('Código de filial não encontrado.')

    def buscar_quantidade(self, quantidade, codigo_filial):
        if codigo_filial in self.filiais:
            filial = self.filiais[codigo_filial]
            for item in filial.estoque:
                livro = item['livro']
                if item['quantidade'] > quantidade:
                    print(f'>>>>>Cod#{livro.codigo}\n'
                          f'Título/Editora: {livro.titulo}/{livro.editora}\n'
                          f'Categoria: {livro.categoria}\n'
                          f'Ano: {livro.ano}\n'
                          f'Valor: R${livro.valor:.2f}\n'
                          f'Estoque: {item["quantidade"]} unidades\n'
                          f'Valor total em estoque: R${livro.valor * item["quantidade"]:.2f}\n')
        else:
            print('Código de filial não encontrado.')

    def buscar_codigo(self, codigo):
        total_estoque = 0
        encontrado = False
        for filial in self.filiais.values():
            for item in filial.estoque:
                livro = item['livro']
                if livro.codigo == codigo:
                    if not encontrado:
                        print(f'>>>>> Cod#{livro.codigo}')
                        print(f'Título/Editora: {livro.titulo}/{livro.editora}')
                        print(f'Categoria: {livro.categoria}')
                        print(f'Ano: {livro.ano}')
                        encontrado = True
                    valor_total = livro.valor * item['quantidade']
                    print(f'Valor: R${livro.valor:.2f} >>> Filial {filial.nome}, estoque: {item["quantidade"]} unidades')
                    total_estoque += valor_total
        if encontrado:
            print(f'Valor total em estoque: R${total_estoque:.2f}')
        else:
            print('Código de livro não encontrado em nenhuma filial.')

    def atualizar_estoque(self, arquivo):
        with open(arquivo, 'w', encoding='utf-8') as file:
            for filial in self.filiais.values():
                file.write(f'#{filial.codigo},{filial.nome},{filial.endereco},{filial.contato}\n')
                for item in filial.estoque:
                    livro = item['livro']
                    file.write(
                        f'{livro.codigo},{livro.titulo},{livro.ano},{livro.categoria},{livro.editora},R${livro.valor:.2f},{item["quantidade"]}\n')
        print('Estoque atualizado com sucesso!')

livraria = Livraria()

while True:
    print(f'1 - Cadastrar novo livro')
    print(f'2 - Listar livros')
    print(f'3 - Buscar livros por nome')
    print(f'4 - Buscar livros por categoria')
    print(f'5 - Buscar livros por preço')
    print(f'6 - Busca por quantidade em estoque')
    print(f'7 - Valor total no estoque')
    print(f'8 - Carregar estoque')
    print(f'9 - Atualizar arquivo de estoque')
    print(f'10 - Criar filial')
    print(f'11 - Listar estoque de filial')
    print(f'12 - Buscar livros por código')
    print(f'0 - Encerrar atividades')

    opcao = input('Opção:')

    if opcao == '1':
        titulo = input('Título: ')
        codigo = int(input('Código: '))
        editora = input('Editora: ')
        area = input('Área: ')
        ano = int(input('Ano: '))
        valor = float(input('Valor: '))
        estoque = int(input('Estoque: '))
        filial_codigo = input('Código da filial: ')
        if filial_codigo in livraria.filiais:
            livro = Livro(codigo, titulo, editora, area, ano, valor, estoque)
            livraria.filiais[filial_codigo].adicionar_livro(livro, estoque)
            print('Livro cadastrado na filial!')
        else:
            print('Filial não encontrada.')
    elif opcao == '2':
        for filial in livraria.filiais.values():
            print(f'Filial {filial.nome}:')
            filial.listar_estoque()
    elif opcao == '3':
        nome = input('Nome do livro: ')
        filial_codigo = input('Código da filial: ')
        livraria.buscar_nome(nome, filial_codigo)
    elif opcao == '4':
        categoria = input('Categoria do livro: ')
        filial_codigo = input('Código da filial: ')
        livraria.buscar_categoria(categoria, filial_codigo)
    elif opcao == '5':
        preco = float(input('Preço máximo: '))
        filial_codigo = input('Código da filial: ')
        livraria.buscar_preco(preco, filial_codigo)
    elif opcao == '6':
        quantidade = int(input('Quantidade mínima em estoque: '))
        filial_codigo = input('Código da filial: ')
        livraria.buscar_quantidade(quantidade, filial_codigo)
    elif opcao == '7':
        valor_total = 0
        for filial in livraria.filiais.values():
            print(f'Filial {filial.nome}:')
            filial.listar_estoque()
    elif opcao == '8':
        arquivo = input('Nome do arquivo: ')
        livraria.carregar_estoque(arquivo)
    elif opcao == '9':
        arquivo = input('Informe o nome do arquivo do estoque: ')
        livraria.atualizar_estoque(arquivo)
    elif opcao == '10':
        codigo = input('Código da filial: ')
        nome = input('Nome da filial: ')
        endereco = input('Endereço: ')
        contato = input('Contato: ')
        livraria.criar_filial(codigo, nome, endereco, contato)
    elif opcao == '11':
        codigo = input('Código da filial: ')
        livraria.listar_estoque_filial(codigo)
    elif opcao == '12':
        codigo = int(input('Código do livro: '))
        livraria.buscar_codigo(codigo)
    elif opcao == '0':
        atualizar = input('Deseja atualizar o arquivo de estoque? (s/n): ')
        if atualizar.lower() == 's':
            pass
        break
    else:
        print('Opção inválida! Tente novamente.')


