import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://te904.leitaolabs.com.br"),
  title: "Torre Evidence 904 | Hospedagem em Belém, Pará",
  description:
    "Apartamento por temporada na Torre Evidence, em Nazaré, região central de Belém. Piscina, academia, estacionamento e reserva pela Booking.com.",
  alternates: {
    canonical: "/",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
      "max-video-preview": -1,
    },
  },
  openGraph: {
    type: "website",
    locale: "pt_BR",
    url: "https://te904.leitaolabs.com.br",
    siteName: "Torre Evidence 904",
    title: "Guia Torre Evidence | Apartamento 904",
    description:
      "Tudo o que você precisa para uma estadia confortável na Torre Evidence, em Belém.",
    images: [
      {
        url: "/og-social.jpg?v=2",
        width: 1200,
        height: 630,
        alt: "Guia Torre Evidence — Apartamento 904 em Belém",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Guia Torre Evidence | Apartamento 904",
    description:
      "Tudo o que você precisa para uma estadia confortável na Torre Evidence, em Belém.",
    images: ["/og-social.jpg?v=2"],
  },
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

const vacationRentalStructuredData = {
  "@context": "https://schema.org",
  "@type": "VacationRental",
  "@id": "https://te904.leitaolabs.com.br/#vacation-rental",
  name: "Apartamento 904 — Torre Evidence",
  alternateName: "TE904",
  description:
    "Apartamento por temporada na Torre Evidence, em Nazaré, região central de Belém, Pará, com piscina, academia 24 horas, estacionamento e cozinha equipada.",
  url: "https://te904.leitaolabs.com.br/",
  mainEntityOfPage: "https://te904.leitaolabs.com.br/",
  image: [
    "https://te904.leitaolabs.com.br/og-social.jpg?v=2",
    "https://te904.leitaolabs.com.br/apartamento/sala.jpg",
    "https://te904.leitaolabs.com.br/apartamento/piscina-fachadas-claras.jpg",
  ],
  address: {
    "@type": "PostalAddress",
    streetAddress: "Av. Alcindo Cacela, 2304",
    addressLocality: "Belém",
    addressRegion: "PA",
    addressCountry: "BR",
  },
  containedInPlace: {
    "@type": "Place",
    name: "Torre Evidence",
  },
  floorSize: {
    "@type": "QuantitativeValue",
    value: 47,
    unitCode: "MTK",
  },
  checkinTime: "14:00",
  checkoutTime: "11:00",
  amenityFeature: [
    { "@type": "LocationFeatureSpecification", name: "Piscina", value: true },
    { "@type": "LocationFeatureSpecification", name: "Academia 24 horas", value: true },
    { "@type": "LocationFeatureSpecification", name: "Estacionamento", value: true },
    { "@type": "LocationFeatureSpecification", name: "Hidromassagem", value: true },
    { "@type": "LocationFeatureSpecification", name: "Lavanderia", value: true },
    { "@type": "LocationFeatureSpecification", name: "Cozinha equipada", value: true },
    { "@type": "LocationFeatureSpecification", name: "Ar-condicionado", value: true },
    { "@type": "LocationFeatureSpecification", name: "Portaria 24 horas", value: true },
  ],
  sameAs: [
    "https://www.booking.com/hotel/br/apartamento-no-coracao-da-amazonia.pt-br.html",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(vacationRentalStructuredData).replace(/</g, String.fromCharCode(92) + "u003c"),
          }}
        />
        {children}
      </body>
    </html>
  );
}
