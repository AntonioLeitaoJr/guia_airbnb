import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://te904.leitaolabs.com.br"),
  title: "Guia Torre Evidence | Apartamento 904",
  description:
    "Guia digital do Apartamento 904 da Torre Evidence em Belém: hospedagem, fotos, localização e informações essenciais.",
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

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
