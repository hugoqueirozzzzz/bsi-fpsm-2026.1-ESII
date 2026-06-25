 # Análise — as 3 responsabilidades da classe `Academia` (v1.0)

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?

A classe faz **regras de negócio** (calcular o valor do plano e contar
check-ins), **interface com o usuário** (ler entradas com `input` e exibir
resultados com `print`) e **notificação** (enviar avisos de boas-vindas e
confirmação de check-in diretamente ao aluno).

## 2. Aponte, no código, **uma linha** de cada responsabilidade

- **Regra de negócio** (cálculo / contagem): linha 13 — `valor = 100.0`
- **Tela** (interface com o usuário): linha 10 — `print("Planos: 1-Mensal  2-Trimestral  3-Anual")`
- **Notificação** (aviso ao aluno): linha 24 — `# TODO: troque o aviso de boas-vindas por uma chamada ao notificador.`

## 3. Como o SRP separa essas responsabilidades?

Após aplicar o SRP, cada responsabilidade passa a morar em seu próprio
componente: as regras de negócio ficam em `AcademiaService`, a persistência
e busca de alunos ficam em `AlunoRepo`, e os avisos ao aluno ficam em
`Notificador`. A classe principal para de acumular funções e passa a apenas
coordenar os componentes.

## 4. Por que ficou melhor? Cite **um** RNF

**Testabilidade:** com as responsabilidades separadas, é possível testar
`AcademiaService` sem depender de `input`/`print` nem de envio real de
mensagens — basta substituir `Notificador` por um objeto falso (mock) nos
testes. Na v1.0 isso era impossível sem executar a interface inteira.
