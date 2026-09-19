# Guia Torre Evidence — Cloudflare

Guia digital multilíngue do Apartamento 904 da Torre Evidence, em Belém. Esta versão está preparada para execução em **Cloudflare Workers** com Vinext e integração contínua pelo GitHub.

## Recursos

- Informações rápidas de Wi-Fi, check-in, check-out e contato do anfitrião
- Guia completo do apartamento e das áreas do condomínio
- Mapa com pontos de interesse em Belém
- Conteúdo em português, inglês e espanhol
- Avaliação do hóspede armazenada em Cloudflare D1
- Interface responsiva para celular e computador

## Desenvolvimento

```bash
npm run dev
```

## Build

```bash
npm run build
```

## Publicação pelo Cloudflare

No fluxo **Workers & Pages → Import a repository**, use:

- Repositório: `AntonioLeitaoJr/guia_airbnb`
- Branch de produção: `main`
- Diretório raiz: `cloudflare-site`
- Comando de build: `pnpm build`
- Comando de deploy: `pnpm deploy`

O domínio personalizado somente deve ser associado depois que a primeira implantação estiver funcionando no endereço `workers.dev`.

## Avaliações dos hóspedes — D1

O site pode ser publicado antes da criação do banco. Nesse caso, todas as páginas funcionam, mas o formulário de avaliação ficará temporariamente indisponível.

Depois da primeira implantação:

1. Crie um banco D1 chamado `te904-feedback`.
2. Adicione ao Worker um binding D1 chamado `DB`.
3. Execute a migration `drizzle/0000_illegal_changeling.sql` no banco.
4. Faça uma nova implantação.

## Eventos ao vivo

Os eventos anuais funcionam sem configuração externa. Para incluir eventos atuais da cidade, configure `TICKETMASTER_API_KEY` como secret do Worker.
