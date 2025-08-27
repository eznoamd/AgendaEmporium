from model.TipoModel import TipoModel

err = TipoModel().criar_tipo(nome="Enzo", filtros="ajsdhasdhkajhsdkajdhakjshdakjsdhkjahsdkahsdjk")
if err is not None:
    print(err)
else:
    print("Tipo criado com sucesso")