Problemas/Divergências

Problema 1 
UC01 - A documentação pede que ao registrar um empréstimo o atendente solicite um email, porém, o código aceita qualquer grafia de email podendo até mesmo conter erros, por exemplo  fulano_ahotmail.com, não necessariamente seguindo a norma "xxxx@xxx.com". É um problema pois pode ocasionar em empréstimos onde o usuário não será informado uma vez que o software pode conter o seu email errado.

Problema 2
UC01 - A documentação pede que ao registrar um empréstimo, o atendente solicite a quantidade de dias, contudo, o código aceita dias em números inteiros (negativos e positivos). É um problema pois por conta de erro humano, algum usuário pode vir a pagar mais do que o acordado. 

Problema 3
UC01 - A documentação pede que ao registrar um empréstimo o atendente solicite o nome do usuário, contudo, o código aceita números como entrada, ao invés de apenas letras. Éum problema pois pode apresentar erros com os usuários, além de não ser sintaticamente correto.

Problema 4
UC01 e UC02 - A documentação informa que o sistema solicita o identificador do empréstimo, contudo, o código não informa o id do empréstimo quando o registro é realizado. , apenas informa o email do usuário, e a data de devolução. O problema é que pode gerar inconvenientes devido a falta de informações como o id do equipamento e o id do empréstimo realizado.

Problema 5
UC03 - Documentação diz que caso "3" seja digitado no menu principal, e não exista pendências, o aplicativo deveria informar que "Nenhum empréstimo em atraso". No código não existe esse comando. É um problema pois não há feedback para o usuário.
