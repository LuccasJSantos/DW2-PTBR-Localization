# Distant Worlds 2 - Tradução para Português

Esta é uma tradução quase completa do jogo Distant Worlds 2, baseada na versão 1.2.6.7, incluindo as traduções das três DLCs que adicionam quatro novas facções jogáveis ao jogo.

A tradução está disponível através deste [link](https://steamcommunity.com/sharedfiles/filedetails/?id=3273120841) na oficina da steam.

## Colaboração
Para aqueles interessados em contribuir com o projeto, sintam-se à vontade para clonar o repositório e fazer suas alterações.

### Orientações Importantes
1. Para realizar alterações, crie uma branch local, utilizando sempre `main` como base.
2. Após concluir suas alterações, faça um push da sua branch e crie um [pull request](https://github.com/LuccasJSantos/DW2-PTBR-Localization/pulls) com uma breve descrição do que foi modificado. Se sentir confortável, adicione seu ID da Steam para receber os devidos créditos na página do mod na Steam.
3. Eu, como mantenedor deste projeto, serei responsável por revisar e publicar suas alterações.
4. Estas orientações estão sujeitas a alterações sem aviso prévio, visando facilitar e/ou padronizar o processo de colaboração.

### Javascript (removed on 2024-04-11)

Foi desenvolvido um script para facilitar a extração de determinados textos originais dos arquivos XML, que podem ser traduzidos em batch por meio de ferramentas externas.

Sinta-se à vontade para utilizar e melhorar o script, seguindo as Orientações Importantes definidas acima durante o processo de atualização do repositório.

### Python (current)

Foram desenvolvidos scripts em Python para agilizar o processo de tradução em futuras atualizações, especialmente caso a estrutura dos arquivos XML seja modificada.

O script funcionará da seguinte forma:
- Ele utiliza os arquivos já traduzidos, localizados na pasta game-data/mod.
- Utiliza os arquivos originais, armazenados na pasta game-data/original.
- O processo identifica automaticamente cada item correspondente pelo 'Id' em cada XML e substitui os textos em inglês dos arquivos originais por suas versões em português, aproveitando as traduções já existentes.

Assim, o script facilita a manutenção das traduções, adaptando-se a possíveis mudanças na estrutura dos XMLs e garantindo que o conteúdo esteja sempre atualizado.

---

*Nota: Devido ao suporte ainda básico para implementar mods no jogo, alguns textos e a ordem das palavras não puderam ser traduzidos adequadamente, pois estão incorporados na lógica interna do código, não acessíveis por arquivos de texto. No entanto, 99% dos textos importantes para a jogabilidade foram traduzidos com máximo cuidado em relação ao contexto do jogo.*
