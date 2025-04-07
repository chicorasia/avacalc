# Avacalc - Calculador de Avaliações de Imóveis

**Avacalc** é uma aplicação desenvolvida para facilitar o cálculo de valores de avaliação de imóveis com base em critérios da Caixa Econômica Federal. Com uma interface gráfica (GUI) funcional e bem estruturada, o projeto oferece cálculos automatizados e suporte para diferentes configurações de códigos de sistema.

---

## **Recursos Principais**

- **Interface gráfica (GUI)**:
  - Desenvolvida em Tkinter, oferecendo usabilidade e interatividade.
  - Radiobuttons para selecionar tipos de objetos de serviço.
  - Formulário de entrada simples e intuitivo para inserir parâmetros necessários.

- **Estrutura Lógica**:
  - Utiliza classes abstratas e concretas para implementar os diferentes códigos de sistema.
  - Sistema genérico de estados para gerenciar seleções dinâmicas no programa.
  - Foco na extensibilidade e manutenção futura.

---

## Screenshots

![Screenshot](\screenshots\screenshot_001.png)

## **Tecnologias Utilizadas**

- **Python 3.10+**
- **Tkinter**: Interface gráfica integrada ao Python.
- **Enum e Typing**: Tipagem avançada e uso de generics.
- **POO (Programação Orientada a Objetos)**: Design modular e extensível.

---

## **Estrutura do Projeto**

avacalc/ ├── avacalc.py                 # Lógica central para cálculo e manipulação de estados 
		 ├── gui.py                     # Interface gráfica 
		 ├── objeto_servico.py       	# Enumeração dos objetos de serviço 
		 ├── codigo_sistema.py       	# Classes abstratas e concretas para diferentes códigos 
		 ├── resultado_calculo.py    	# Classe para encapsular os resultados do cálculo 
​		  └── README.md                  # Documentação do projeto

## Funcionamento

1. Insira os seguintes parâmetros:
   - **Número de unidades habitacionais (**`n`**)**.
   - **Número de tipologias por categoria (**`nt`**)**.
   - **Tipo de objeto de serviço**: Utilize os radiobuttons para selecionar o tipo apropriado.
2. Clique no botão **Calcular** para obter os resultados.

## **Exemplo de Entrada e Saída**

### Entrada:

- **Número de unidades habitacionais (**`n`**):** 75
- **Número de tipologias (**`nt`**):** 2
- **Objeto de Serviço:** Terreno com área até 2000 m²

### Saída:

```bash
---- RESULTADO ----
Descrição:
Terreno com área até 2000 m². Avaliação simplificada.

Valor Laudo Simplificado: R$ 2.500,00
Valor Laudo Completo: R$ 3.500,00
-------------------
```

## **Regras de Negócio e Configurações**

O cálculo dos valores está baseado nos diferentes **códigos de sistema**, como `A030`, `A032`, entre outros. Para cada código, há configurações específicas, como descrições, valores base e limites máximos. As configurações estão centralizadas na classe `CodigoSistema`, e cada código tem suas próprias implementações para cálculos.

### **Estrutura da Classe**

- **Classe Abstrata** `CodigoSistema`:
  - Define os métodos padrão para cálculo (simplificado e completo).
  - Centraliza descrições e configurações em dicionários.
- **Classes Concretas**:
  - Implementam regras de cálculo específicas para cada código, como `A030`, `A032`, etc.

## **Personalizações**

- Adicione novos códigos de sistema criando subclasses de `CodigoSistema` e registrando configurações apropriadas.
- Modifique o layout da GUI, adaptando os estilos e estruturas para atender a diferentes requisitos.

## **Contribuindo**

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório.

2. Crie uma branch para sua contribuição:

   bash

   ```
   git checkout -b minha-contribuicao
   ```

3. Envie suas alterações:

   bash

   ```
   git add .
   git commit -m "Descrição das alterações"
   git push origin minha-contribuicao
   ```

4. Abra um Pull Request.

## **Licença**

Este projeto está licenciado sob a licença Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). Para mais informações, visite [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/).

### **Desenvolvedores**

- **Chico Rasia e Simone Dias** - 2025