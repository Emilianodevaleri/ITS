from types_voli_aerei import RealG19

class volo:
    _nome:str
    _anno:RealG19

    def __init__(self, nome:str, anno:RealG19) -> None:
        self.set_nome(nome)
        self.set_anno(anno)

    def nome(self) -> str:
        return self._nome

    def anno(self) -> RealG19:
        return self._anno
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def anno(self, a: RealG19) -> None:
        self._anno= a
       
