# --- Professor ---
# Nome: Carlos, Idade: 40
# ...
# Disciplina: Matemática

# --- Aluno ---
# Nome: Maria, Idade: 16
# ...
# Matrícula: 2025A01

# --- Funcionário ---
# Nome: João, Idade: 35
# ...
# Cargo: Bibliotecário

from Aluno import Aluno
from Professor import Professor
from Funcionario import Funcionario

def main():
    pessoa001 = Professor ("Carlos", 40, "12345678901", "Rua Azul, 31" , "91111-1111", "Matemática")
    pessoa002 = Aluno ("Maria" , 16 , "12345678911" , "Rua Vermelha, 55" ,"92222-2222" , "2025A01")
    pessoa003 = Funcionario ("João" , 35 , "12345678922" , "Rua Amarela, 33" , "93333-3333" , "Bibliotecario")

    pessoa001.mostrar_detalhes()
    pessoa002.mostrar_detalhes()
    pessoa003.mostrar_detalhes()

if __name__ == "__main__":
    main()