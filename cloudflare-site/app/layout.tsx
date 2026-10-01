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

const webPageStructuredData = {
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://te904.leitaolabs.com.br/#webpage",
  url: "https://te904.leitaolabs.com.br/",
  name: "Torre Evidence 904 | Hospedagem em Belém, Pará",
  description:
    "Apartamento por temporada na Torre Evidence, em Nazaré, região central de Belém. Piscina, academia, estacionamento e reserva pela Booking.com.",
  inLanguage: "pt-BR",
  primaryImageOfPage: {
    "@type": "ImageObject",
    url: "https://te904.leitaolabs.com.br/og-social.jpg?v=2",
  },
  about: {
    "@type": "Place",
    "@id": "https://te904.leitaolabs.com.br/#te904",
    name: "Apartamento 904 — Torre Evidence",
    alternateName: "TE904",
    description:
      "Apartamento por temporada na Torre Evidence, em Nazaré, região central de Belém, Pará.",
    url: "https://te904.leitaolabs.com.br/",
    image: "https://te904.leitaolabs.com.br/og-social.jpg?v=2",
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
    sameAs:
      "https://www.booking.com/hotel/br/apartamento-no-coracao-da-amazonia.pt-br.html",
  },
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
            __html: JSON.stringify(webPageStructuredData).replace(/</g, String.fromCharCode(92) + "u003c"),
          }}
        />
        {children}
      </body>
    </html>
  );
}
