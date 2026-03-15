# Reflexão — Lab 05

Aluno: Víctor Gabriel Cruz Pereira

---

## 1. Stubs e Skeletons: Os Bastidores da Comunicação
Nos sistemas baseados em RPC, os stubs e skeletons são os grandes responsáveis por esconder a complexidade da rede. O stub do cliente funciona como um intermediário: ele pega uma chamada de função local e a traduz (serializa) em uma mensagem que pode viajar pela rede.

Do outro lado, o skeleton do servidor recebe esse pacote, faz a tradução inversa (desserialização) e entrega a tarefa para a função correta dentro do serviço. 

> O que aprendi na prática: Ao implementar o stub manualmente, ficou claro que, sem esse mecanismo, teríamos um trabalho braçal enorme. Precisaríamos gerenciar manualmente cada envio de dados, a interpretação de cada byte e o retorno de cada resultado, o que tornaria o desenvolvimento de sistemas distribuídos muito mais lento e propenso a erros.

---

## 2. REST vs. RPC: Ação ou Recurso?
A principal diferença aqui é a filosofia de trabalho. No modelo RPC, o foco é a ação. O cliente chama um procedimento remoto quase como se estivesse executando uma função dentro do seu próprio programa.

Já no REST, o foco muda para o recurso. A interação acontece através de endereços específicos (URIs) e as operações seguem os verbos padrão do HTTP (GET, POST, PUT, DELETE). 

Durante a implementação da API REST, percebi que o cliente não manda o servidor executar a função X, mas sim solicita uma interação com o recurso Y. Isso mostra que o REST é orientado a dados e estados, enquanto o RPC é orientado a procedimentos e comportamentos.

---

## 3. Contratos e a Evolução do Sistema
No gRPC, a segurança vem de um contrato formal: um arquivo de definição que especifica exatamente quais mensagens e serviços existem. Isso é uma mão na roda para a evolução do sistema, pois o uso de Protocol Buffers permite adicionar novos campos sem quebrar clientes antigos — as versões anteriores apenas ignoram o que não conhecem.

Em contrapartida, no REST (especialmente com JSON), a comunicação costuma ser mais flexível, mas também mais perigosa. Como geralmente não há um contrato rígido obrigatório, qualquer mudança na estrutura dos dados precisa ser feita com cautela redobrada para não derrubar as integrações existentes.

---

## 4. Escolha de Tecnologia: O Cenário Real
Ao projetar uma API de pagamentos, a escolha da tecnologia depende de quem vai usá-la:

* Para Parceiros Externos: O REST é a escolha ideal. Ele fala a língua da web, usa JSON e é fácil de integrar em qualquer linguagem, o que remove barreiras para quem vem de fora.
* Para Microsserviços Internos: O gRPC brilha. Como a comunicação é binária e altamente otimizada, ele garante uma performance superior e economiza recursos de rede, sendo perfeito para o diálogo intenso que acontece dentro da nossa própria infraestrutura.
