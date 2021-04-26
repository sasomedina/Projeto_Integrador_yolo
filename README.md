# Projeto_Integrador_yolo

**Este projeto foi desenvolvido como trabalho final no curso de Data Science oferecido e ministrado pela Digital House. Os dados utilizados neste projeto foram fornecidos generosamente pela empresa com a qual foi acordado previamente este projeto.**

*A explicação do projeto é simples e direta.*

O cliente para qual desenvolvemos o projeto é do ramo imobiliário procurando lançar um novo conceito no mercado utilizando sua pórpria pltaforma digital, visando acabar com a burocrácia e a necessidade de fiador e os pagamentos com boleto.
O crescimento rápido de empresas e setores deste ramo propiciam o surgimento de problemas operacionais como a classificação de inventários da base de imóveis, a fim de melhorar a descrição dos anúncios na plataforma e aumentar o número de variáveis explicativas de cada imóvel a ser comprado ou alugado.
As informações são subidas pra plataforma da seguinte forma:
- O proprietário envia as fotos do seu imóvel pela plataforma (site ou app);
- Nosso modelo lê e identifica as imagens;
- O resultado é enviado ao sistema ERP para cadastro no site, modelagem de precificação, inventário e aumento de confiança.

Assim que o algoritmo é rodado no banco de dado do cliente, é retornada a detecção dos objetos junto do nível de confiança de cada objeto detectado. As informações retiradas dos resultados são utilizadas para:
- Incrementar o banco de dados;
- Melhorar a descrição do imóvel com maior confiança;
- Aumentar a agilidade no cadastramento do inventário;
- Reduzir o custo com folha de pagamento (atualmente existem empresas terceirizadas especializadas que realizam inventários e cobram em torno de R$100,00 por imóvel);
- No projeto que conta com 123 apartamentos, o custo foi otimizado em R$12.300,00.
![Confianca_PI](https://user-images.githubusercontent.com/51931603/116142852-c8e77900-a6b0-11eb-96b4-7dbe975cebe0.jpg)
Grau de confiança das leituras. Com maioria dos outputs maior que 80%

Foi incluída uma outra melhoria baseada em geolocalização. Utilizando a base do site do cliente para analisar as informações das buscas realizadas pelos clientes, foi constatado que as maiores procuras são por imóveis próximos a estações de metrô.
Com a ajuda de uma API do Google, conseguimos mensurar radialmente a distância do imóvel cadastrado até a estação de metrô mais próxima.
![Geolocation_PI](https://user-images.githubusercontent.com/51931603/116143110-1b289a00-a6b1-11eb-82fa-e7013ef7680d.jpg)
