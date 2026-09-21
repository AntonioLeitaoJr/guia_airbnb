# Guia Torre Evidence — Cloudflare

Guia digital multilíngue do Apartamento 904 da Torre Evidence, em Belém. Esta versão está preparada para execução em **Cloudflare Workers** com Vinext e integração contínua pelo GitHub.

## Recursos

- Informações rápidas de Wi-Fi, check-in, check-out e contato do anfitrião
- Guia completo do apartamento e das áreas do condomínio
- Mapa com pontos de interesse em Belém
- Conteúdo em português, inglês e espanhol
- Avaliação do hóspede registrada na planilha Google Sheets do anfitrião
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

## Avaliações dos hóspedes — Google Sheets

As avaliações são encaminhadas ao Google Apps Script configurado pela variável protegida `GOOGLE_SHEETS_WEBHOOK_URL`. A implantação pública no Cloudflare usa como contingência o proxy protegido da versão hospedada no Sites, sem expor o endereço da planilha no navegador do hóspede.

## Eventos ao vivo

Os eventos anuais funcionam sem configuração externa. Para incluir eventos atuais da cidade, configure `TICKETMASTER_API_KEY` como secret do Worker.
