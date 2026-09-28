# Guia Torre Evidence — Cloudflare

Guia digital multilíngue do Apartamento 904 da Torre Evidence, em Belém. Esta versão está preparada para execução em **Cloudflare Workers** com Vinext e integração contínua pelo GitHub.

## Recursos

- Informações rápidas de Wi-Fi, check-in, check-out e contato do anfitrião
- Guia completo do apartamento e das áreas do condomínio
- Mapa com pontos de interesse em Belém
- Conteúdo em português, inglês e espanhol
- Avaliação do hóspede registrada na planilha Google Sheets do anfitrião
- Interface responsiva para celular e computador
- Calendário de datas bloqueadas exportado da Booking.com, sem expor o endereço iCal

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

## Calendário da Booking.com

Configure `BOOKING_ICAL_URL` como **secret** do Worker `te904-guia` (Workers & Pages → te904-guia → Settings → Variables and Secrets → Add → Secret) e cole o URL completo da exportação iCal. Para configurar pelo terminal: `pnpm exec wrangler secret put BOOKING_ICAL_URL`. Nunca coloque o URL em `wrangler.jsonc`, no GitHub ou em uma variável pública. Sem o secret ou quando a origem falhar, o site mostra um aviso e um link para a Booking.com, sem apresentar datas possivelmente incorretas.

O servidor consulta o iCal e publica apenas os intervalos bloqueados, com cache de até 15 minutos. O dia de saída de cada reserva é tratado como disponível para nova entrada, sujeito a confirmação. Sincronize também os bloqueios de reservas diretas e outras plataformas na Booking.com; a exportação não representa atualização em tempo real.
