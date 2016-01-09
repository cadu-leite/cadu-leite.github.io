title: Django - Se você não gosta, é porque está usando errado.
Date: 2015-07-07
Modified: 2015-08-11
Category: django
Tags: python, django
Slug: django_nao_gosta_porque_esta_usando_errado
Authors: Carlos Leite
Summary: Django, se você não gosta é porque está usando no lugar errado.
status: published

Se já usou o framework Django e não gostou, você provavelmente o usou no problema errado !

No texto abaixo eu vou descrever algumas caracteísticas do framework Django, que EU julgo, sejam importantes levar em consideração antes de decidir usá-lo para sua solucão.

## 1. O que é Django ?

Django é um framework web para desenvolvimento de __aplicações WEB__ e foi escrito em __Python__.

O _slogan_ do django nos dá uma pista.

>Django: The web framework for perfectionists with deadlines.

Então o objectivo do framework Django é __OTIMIZAR o tempo__ de desenvolvimento de uma aplicação WEB - prototipagem rápida! Aliás, a jato ! 8P

Isso não quer dizer que todo o resto foi negligenciado, só que o objetivo principal era otimizar o tempo de _bootstrap_ - Início do projeto.

Para isso, os desenvolvedores do Django integraram ao framework, algumas ferramentas (ou bibliotecas python) que sempre eram usadas por estes ao iniciar uma aplicação WEB.

Embutidos no framework, estão bibliotecas que tratam requisições WEB, um _ORM_ para BD relacionais, uma linguagem de _templates_ entre outras ferramentas uo funcionalidades. Ex. framework de autenticação de usuários, sistema de permissões, cache, variáveis de ambiente e etc.
Tudo o que você precisa para uma __Aplicação WEB__.

###Bala de prata !?!

__NÃO__. O Django não é um framework para ser usado em qualquer aplicação WEB.

Aliás, o que é uma aplicação WEB ? aqui começa o problema para definir se sua solução requer ou exige a utilização do Django.

Aplicação WEB, pode ser qualquer coisa, um Blog pode ser publicado ou pode ter seu sistema de publicação sendo uma aplicação web, e o sistema de cadastramento do sistema de saúde do brasil com milhões de usuários também. Mas nem por isso tem soluções pareceidas.

Eu costumo fazer a seguinte pergunta:

>A Maior parte dos dados é tabular e são inseridos pelo usuário ?
... então é um projeto Django.

Se existe uma quantidade de dados grande que serão inseridos pelo usuário, 
eu preciso de formulários, validção e um local pra armazenar.

São as 3 funções, principais, que o django resolve !
1. entrada de dados (views/templates)
2. validação da entrada de dados (Forms)
3. armazenamento (ORM)

Não tão fácil - as vezes, responder essa pergunta não é o suficiente.

e mais, __a recíproca não é verdadeira__.

Mesmo que sua aplicação tenha muita interação com o usuário, banco de dados, perfis, permissões  etc, mesmo assim o Django __pode__ não ser a melhor soluçao.

Mas a pergunta faz sentido, dentro do meu contexto de desenvolvimento.

Porque a pergunta então ?

##Caraceterística importantes do Django.

Um dos pontos de ganho de produtividade que se pode ter em um time que está construindo um sistema, é diminuir a quantidade de decisões a serem tomadas durante o desenvolvimento.

Algumas são muito importantes mas ao mesmo tempo mais básicas.

    ex.: existe um framework que podemos usar para este projeto ? qual ?

Outras questões, podem ter respostas menos óbvias, e ao mesmo tempo terem tantas opções similares que é quase uma questão pessoal ou cultural.

    Ex.: que banco de dados utilizar na solução.

Na verdade qualquer um dos meus 2 exemplos, tem uma infinidade de fatores que podem influenciar. A Cultura, _know-how_ da equipe de desenvolvimento,  ou o conhecimento desta, cultura da empresa, o cliente etc etc etc. Mas o fato é :

Quanto menos decisões tivermos que tomar para cada novo projeto de software que fazemos, aumentamos a produtividade. (... só essa inha da um novo artigo.)

O que o Django faz para aumentar a produtividade é tomar algumas decisões de projeto de aplicação WEB.

1. O sistema ORM
2. A linguagem de templates.
3. FORMs
4. parte de como vc deve organizar o projeto.


##Onde utilizar o Django ?


Mas aqui também se aplica a regra: _"não existe almoço grátis"_.

>Sempre que há um bônus, existe também um ônus.

No caso do framework Django, o ônus é a "quase obrigatoriedade" de se resolver certos problemas da aplicação web com as ferramentas (bibliotecas)
 _embutidas_ no framework. __QUASE__!

Para que o desenvolvimento de uma aplicação Django seja rápido (rápida prototipação), os desenvolvedores do framework Django, fizeram algumas escolhas para embutir no framework soluções que resolvem problemas comuns ao desenvolvimento de aplicações WEB (comuns ao contexto que eles imaginaram ao desenvolver o framework) . Essa integração,

O outro lado desta moeda ou no caso, o _"custo desse almoço"_ é que para ganhar tempo, sua solucão terá que ser desenvolvida, e terá talvez que se adaptar em parte a essas ferramentas que compõem o framework Django.

Tentar alterar o comportamento de uma dessas ferramentas ou até _"trocá-las"_ pode lhe tirar todo o ganho que o framework Django lhe daria, e consequentemente, perde-se o sentido de utilizar o framework.

E aí ?! e o slogan ?

>The web framework for perfectionists with deadlines.

depende de qual é o seu problema, ou melhor ainda, qual a solução você quer dar ao seu problema.

###Como saber se uso ou não o framework Django


Alguns desenvolvedores, insistem em comparar __microframeworks__ com Django, e muitas vezes o fazem de maneira errada.

Vc pode querer comparar qualquer coisa com um framework web, até uma laranja, e vai chegar a conclusão que são coisas bem diferentes (ou não). Um microframework, está bem mais próximo de um framework, mas ainda sim como a laranja, atende necessidades diferentes de um framework.

POR EXEMPLO __Flask__ !
__Flask__ é um micro framework também desenvolvido em Python, para desenvolvimento de aplicações WEB. sem os plugins, ele é uma grande biblioteca para tratar requisições HTTP.
Vc também não precisa dele para fazer um blog, mas se vc quiser fazer um sistema de publicação enxuto, ele pode ser uma saida (mas antes tente algo como o projeto Pelikan por exemplo.)

Um exemplo de uso do FLASK, caso no qual o Django seria _"overkill"_ é se vc necessita somente desenvolver um serviço WEB, recebimento de dados (machine to machine), ou um validador de 1 formulário, ou coisas suscintas e objetivas com pouca ou nenhuma interação de usuários.

##Para que serve o Django então ?:

O framework Django é formado por 3 principais _"partes"_:

1. ORM
2. Linguagem de templates.
3. Tratamento de requisições HTTP (com extrema simplcidade).
4. ADMIN - um site pronto para que possa editar os modelos de dados do projeto.

...
para quem nao conhece nada de Django, ele ainda tem um sistema para autenticação de usuários, um framework para permisões entre vários outros plugins e bibliotecas que podem facilitar o desenvolvimento de uma applicação WEB. Existe até uma app para fazer com que o framework trabalhe com REST!

Isso quer dizer que, utilizando o framework, vc tem facilidades para acessar um banco de dados (ler, escrever), permite publicar dados dinâmicos em uma página web, possui rotinas para que tudo isso seja __acionado__ através de chamadas HTTP - requisições http.

>LOGO se vc não precisa de uma destas 3 "ferramentas", então vc não precisa do Django.

Se vc não precisa de um formulário web + controle de usuário + páginas html (talvez vc ainda queira o banco de dados), o Flask é realmente uma ótima opção..

O que os desenvolvedores (comunidade)  do Django, fizeram, foi tomar algumas decisões por você (programador) para que você foque no problema que vc quer resolver com a sua aplicação. Essas escolhas (ORM, templates ...) tornam o início do projeto extremamente rápido

 Eles definiram o ORM, a linguagem de templates e a maneira como vc interage com o usuário (ModelForms)  e colocaram dentro de um pacote que se integra. ...  e muito bem diga-se de passagem.

Se vc quer alterar um destas "ferramentas", faça um favor a você mesmo, e não use o Django !

Python tem talvez uma centena de bibliotecas e frameworks capazes de resolver requisições HTTP,  vc vai enontrar algo que se encaixe perfeitamente na suas necessidades ...  ou algo muito próximo.

