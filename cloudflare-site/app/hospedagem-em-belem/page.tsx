import type { Metadata } from "next";

import { SeoLanding } from "../seo-landing";

export const metadata: Metadata = {
  title: "Hospedagem em Belém | Apartamento 904 na Torre Evidence",
  description:
    "Hospedagem em Belém no Apartamento 904 da Torre Evidence, em Nazaré. Studio de 47 m² com piscina, academia 24h, estacionamento e cozinha equipada.",
  alternates: { canonical: "/hospedagem-em-belem" },
  robots: { index: true, follow: true },
  openGraph: {
    type: "website",
    locale: "pt_BR",
    url: "https://te904.leitaolabs.com.br/hospedagem-em-belem",
    title: "Hospedagem em Belém | Apartamento 904 na Torre Evidence",
    description: "Apartamento por temporada em Nazaré, região central de Belém.",
    images: [{ url: "/apartamento/sala.jpg", alt: "Sala do Apartamento 904 na Torre Evidence, em Belém" }],
  },
};

const structuredData = {
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://te904.leitaolabs.com.br/hospedagem-em-belem#webpage",
  url: "https://te904.leitaolabs.com.br/hospedagem-em-belem",
  name: "Hospedagem em Belém | Apartamento 904 na Torre Evidence",
  description: "Hospedagem em Belém no Apartamento 904 da Torre Evidence, em Nazaré.",
  inLanguage: "pt-BR",
  isPartOf: { "@id": "https://te904.leitaolabs.com.br/#webpage" },
  about: { "@id": "https://te904.leitaolabs.com.br/#te904" },
};

const sections = [
  {
    heading: "Uma hospedagem prática para viver Belém",
    paragraphs: [
      "O TE904 é um apartamento por temporada na Torre Evidence, na Avenida Alcindo Cacela, em Nazaré. A localização oferece uma base conveniente para quem visita Belém a lazer, a trabalho ou para compromissos na região central da cidade.",
      "O studio tem 47 m² e riúne área de descanso, espaço de trabalho, sala, cozinha equipada e ar-condicionado. A proposta é combinar a autonomia de um apartamento com a estrutura de um condomínio completo.",
    ],
  },
  {
    heading: "Estrutura do apartamento e da Torre Evidence",
    paragraphs: [
      "Durante a estadia, o hóspede encontra ambientes organizados e facilidades úteis para uma rotina curta ou prolongada. As regras, os horários e as orientações de acesso ficam reunidos no guia digital do TE904.",
    ],
    points: [
      "Piscina, hidromassagem e sauna no andar de lazer",
      "Academia disponível 24 horas",
      "Estacionamento com vaga definida",
      "Cozinha equipada, ar-condicionado e Smart TV",
      "Lavanderia no condomínio e portaria 24 horas",
      "Pista de cooper e vista da cidade na cobertura",
    ],
  },
  {
    heading: "Nazaré e os principais pontos de Belém",
    paragraphs: [
      "Nazaré é um bairro tradicional e bem localizado. A partir do apartamento, é possível acessar serviços, gastronomia e pontos conhecidos como a Basílica de Nazaré, o Museu Emílio Goeldi, a Estação das Docas e o Ver-o-Peso.",
      "A Torre Evidence fica em uma região central de Belém, mas não no bairro oficialmente chamado Centro. Essa distinção torna a informação mais precisa para quem está comparando onde ficar na cidade.",
    ],
  },
  {
    heading: "Reserva e disponibilidade",
    paragraphs: [
      "Preços, condições e datas disponíveis devem ser confirmados no canal de reserva indicado. A página do TE904 reúne fotos, calendário informativo e acesso à Booking.com para a consulta final antes da contratação.",
    ],
  },
] as const;

export default function HospedagemEmBelemPage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData).replace(/</g, String.fromCharCode(92) + "u003c") }} />
      <SeoLanding
        eyebrow="Hospedagem em Belém"
        title="Hospedagem em Belém com conforto e praticidade."
        intro="Um studio de 47 m² na Torre Evidence, em Nazaré, com estrutura para descansar, trabalhar e conhecer Belém."
        image="/apartamento/sala.jpg"
        imageAlt="Sala integrada do Apartamento 904 na Torre Evidence em Belém"
        sections={sections}
        relatedHref="/apartamento-em-nazare-belem"
        relatedTitle="Como é ficar em Nazaré, Belém"
        relatedDescription="Conheça a localização, os pontos próximos e as vantagens práticas do bairro para sua estadia."
      />
    </>
  );
}
