from model.StatusModel import StatusModel
from model.ClienteModel import ClienteModel
from model.TipoModel import TipoModel

def testar_status():
    print("=== Teste StatusModel ===")

    status_model = StatusModel()

    # testa criação
    resultado = status_model.criar_status(nome="Em teste", cor="#FF0000")
    print("Resultado criar_status:", resultado)

    # testa get_all
    lista = status_model.get_all()
    print("Resultado get_all (Status):", lista)

    # se houver algum id conhecido, você pode testar get_by_id aqui
    # por exemplo:
    # item = status_model.get_by_id(1)
    # print("Resultado get_by_id(1) (Status):", item)


def testar_cliente():
    print("=== Teste ClienteModel ===")

    cliente_model = ClienteModel()

    # testa criação
    resultado = cliente_model.criar_cliente(nome="Cliente Teste", codigo="CLI-001")
    print("Resultado criar_cliente:", resultado)

    # testa get_all
    lista = cliente_model.get_all()
    print("Resultado get_all (Cliente):", lista)

    # se houver algum id conhecido, você pode testar get_by_id aqui
    # por exemplo:
    # item = cliente_model.get_by_id(1)
    # print("Resultado get_by_id(1) (Cliente):", item)


def testar_tipo():
    print("=== Teste TipoModel ===")
    tipo_model = TipoModel()
    
    resultado = tipo_model.criar_tipo(nome="Tipo Teste", filtros="filtro1,filtro2")
    print("Resultado criar_tipo:", resultado)

    lista = tipo_model.get_all()
    print("Resultado get_all (Tipo):", lista)

if __name__ == "__main__":
    # rode este arquivo diretamente para testar os models
    testar_status()
    print("\n")
    testar_cliente()
    print("\n")
    testar_tipo()
    print("\n")