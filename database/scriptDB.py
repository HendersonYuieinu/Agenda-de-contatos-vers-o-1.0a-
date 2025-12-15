from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#configurando o data base
database = create_engine("sqlite:///database/BancoDados.db")

#criando a Session para usar depois
Session = sessionmaker(bind=database)

#criando a base
base = declarative_base()

#tabela contatos
class contato(base):
    __tablename__ = "contatos"                                          #define o nome da tabela            
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)    #cria a coluna id como chave primaria e autoincrementada    
    nome = Column("nome", String)                                       #cria a coluna nome
    sobrenome = Column("sobrenome", String)                             #cria a coluna sobrenome
    nota = Column("nota", String)                                       #cria a coluna nota
    telefones = relationship("telefone", back_populates="contato", cascade="all, delete-orphan")
    emails = relationship("email", back_populates="contato", cascade="all, delete-orphan")
    
    def __init__(self, nome, sobrenome, nota=""):                       #construtor padrao de classes do python
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota
    

#tabela telefone
class telefone(base):
    __tablename__ = "telefones"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_contato = Column("id_contato", Integer, ForeignKey("contatos.id"))   #chave estrangeira do contato
    numero = Column("numero", String(20), nullable=False)                   #numero é o unico campo obrigatorio do banco de dados
    contato = relationship("contato", back_populates="telefones")
    
    def __init__(self, id_contato, numero):
        self.id_contato = id_contato
        self.numero = numero
        
#tabela email
class email(base):
    __tablename__ = "email"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_contato = Column("id_contato", Integer, ForeignKey("contatos.id"))
    endereco = Column("endereco", String)
    contato = relationship("contato", back_populates="emails")
    def __init__(self, id_contato, endereco):
        self.id_contato = id_contato
        self.endereco = endereco


if __name__ == "__main__":
    
    base.metadata.create_all(bind=database)                                 #criando as tabelas