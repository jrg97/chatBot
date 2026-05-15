class PromptMestre:

    def __init__(self):

        self.persona = """Descrição/Apresentação do chat"""

        self.tarefa = "Define a tarefa que o chat ira realizar"

        self.restricao = "Define os parametros que o chat não pode ignorar"

        self.formato = "Forma como a resposta deve ser entregue. No nosso caso é texto"

    def montar_system_prompt(self) -> str:
    
        system_prompt = f"""
        {self.persona}

        {self.tarefa}

        {self.restricao}

        {self.formato}"""

        return system_prompt.strip()

    def get_prompt(self) -> str:
        return self.montar_system_prompt()
    
if __name__ == "__main__":
    pm = PromptMestre()
    print("=" * 60)
    print("SYSTEM PROMPT GERADO:")
    print("=" * 60)
    print(pm.get_prompt())
