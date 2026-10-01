import type { Metadata } from "next";

import { SeoLanding } from "../seo-landing";

export const metadata: Metadata = {
  title: "Apartamento em Nazaré, Belém | TE904 Torre Evidence",
  description:
    "Conheça o Apartamento 904 na Torre Evidence, em Nazaré, Belém: localização central, estrutura do condomínio, pontos próximos, fotos e reserva.",
  alternates: { canonical: "/apartamento-em-nazare-belem" },
  robots: { index: true, follow: true },
  openGraph: {
    type: "website",
    locale: "pt_BR",
    url: "https://te904.leitaolabs.com.br/apartamento-em-nazare-belem",
    title: "Apartamento em Nazaré, Belém | TE904 Torre Evidence",
    description: "Apartamento por temporada na Torre Evidence, em Nazaré, Belém.",
    images: [{ url: "/apartamento/cobertura-vista.jpg", alt: "Vista de Belém a partir da cobertura da Torre Evidence" }],
  },
};

const structuredData = {
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://te904.leitaolabs.com.br/apartamento-em-nazare-belem#webpage",
  url: "https://te904.leitaolabs.com.br/apartamento-em-nazare-belem",
  name: "Apartamento em Nazaré, Belém | TE904 Torre Evidence",
  description: "Conheça o Apartamento 904 na Torre Evidence, em Nazaré, Belém.",
  inLanguage: "pt-BR",
  isPartOf: { "@id": "https://te904.leitaolabs.com.br/#webpage" },
  about: { "@id": "https://te904.leitaolabs.com.br/#te904" },
};

const sections = [
  {
    heading: "Nazaré: localização central sem perder a identidade do bairro",
    paragraphs: [
      "O Apartamento 904 fica na Avenida Alcindo Cacela, em Nazaré, um dos bairros mais conhecidos de Belém. A região combina serviços cotidianos, opções de alimentação e acesso a diferentes áreas da cidade.",
      "A localização é central, embora Nazaré seja um bairro próprio e não o bairro Centro. Para o visitante, isso significa proximidade com pontos importantes sem apresentar uma informação geográfica imprecisa.",
    ],
  },
  {
    heading: "O que conhecer a partir do apartamento",
    paragraphs: [
      "A Basílica de Nazaré e o Museu Emílio Goeldi estão entre as referências mais próximas. Também é possível seguir para a Estação das Docas, o mercado do Ver-o-Peso e o centro histórico, de acordo com o roteiro e o meio de transporte escolhido.",
      "O guia principal do TE904 oferece um mapa com esses pontos para ajudar o hóspede a organizar deslocamentos e aproveitar melhor a passagem por Belém.",
    ],
    points: [
      "Basílica Santuário de Nazaré e entorno do Círio",
      "Museu Paraense Emílio Goeldi",
      "Estação das Docas e orla da Baía do Guajará",
      "Mercado do Ver-o-Peso e centro histórico de Belém",
    ],
  },
  {
    heading: "Apartamento 904 e estrutura do condomínio",
    paragraphs: [
      "O TE904 é um studio de 47 m² preparado para estadias em Belém. O espaço possui cozinha integrada, ambiente de trabalho, ar-condicionado e área de estar, enquanto a Torre Evidence oferece piscina, academia 24 horas, estacionamento, lavanderia e cobertura.",
      "As fotografias exibidas no site mostram o apartamento e as áreas utilizadas pelos hóspedes. Horários e orientações do condomínio devem ser consultados no guia antes do uso.",
    ],
  },
  {
    heading: "Para quem essa localização funciona bem",
    paragraphs: [
      "O apartamento atende quem procura uma hospedagem em Belém com autonomia e acesso facilitado a serviços. Pode ser uma opção para turismo, viagens profissionais, visitas familiares e compromissos na região central.",
      "A disponibilidade e as condições da reserva variam conforme as datas. A confirmação final deve ser feita pela Booking.com ou pelo canal informado pelo anfitrião.",
    ],
  },
] as const;

export default function ApartamentoEmNazarePage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData).replace(/</g, String.fromCharCode(92) + "u003c") }} />
      <SeoLanding
        eyebrow="Apartamento em Nazaré, Belém"
        title="Apartamento em Nazaré, Belém: uma base central."
        intro="O Apartamento 904 fica na Torre Evidence, com acesso prático a serviços, cultura e pontos importantes de Belém."
        image="/apartamento/cobertura-vista.jpg"
        imageAlt="Vista da cidade de Belém a partir da cobertura da Torre Evidence"
        sections={sections}
        relatedHref="/hospedagem-em-belem"
        relatedTitle="Veja a hospedagem e a estrutura do TE904"
        relatedDescription="Confira as facilidades do apartamento, as áreas do condomínio e como consultar disponibilidade."
      />
    </>
  );
}
